#!/usr/bin/python
#-*-coding:utf-8-*-

"""
Starlette ASGI server that can classify an image as Black, Grizzly or Teddy bear.
Just following Lesson 2 of FastAI Course1 v3...

Examples:
https://localhost:8008/classify?url=https://upload.wikimedia.org/wikipedia/commons/3/33/Jasper_Dwayne_Reilander-4.jpg

Author: https://github.com/bguan
License: http://unlicense.org
"""

from fastai.vision import load_learner, open_image
from io import BytesIO
from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse

import aiohttp
import asyncio
import sys
import uvicorn


# Useful constants
MB = 1024*1024
MAX_READ_BYTES = 5*MB


# util func to read bytes using async http
async def get_bytes(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            buffer = b""
            async for data in response.content.iter_chunked(MAX_READ_BYTES):
                buffer += data
                if response.content.at_eof():
                    return buffer
                elif len(buffer) > MAX_READ_BYTES:
                    raise RuntimeError(f"Attempt to read more than { MAX_READ_BYTES//MB } MB")


# util func to predict bytes as image
def predict_image_from_bytes(bytes):
    img = open_image(BytesIO(bytes))
    _,_,losses = bear_learner.predict(img)
    return JSONResponse({
        "predictions": sorted(
            zip(bear_learner.data.classes, map(float, losses)),
            key=lambda p: p[1],
            reverse=True
        )
    })


# initialize Starlette App and load pre-trained FastAI learner
app = Starlette()
bear_learner = load_learner(".", file="bears.pkl")


@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    bytes = await (data["file"].read())
    return predict_image_from_bytes(bytes)


@app.route("/classify", methods=["GET"])
async def classify_url(request):
    bytes = await get_bytes(request.query_params["url"])
    return predict_image_from_bytes(bytes)


@app.route("/")
def form(request):
    return HTMLResponse(
        """
        <h1>My Black, Grizzly or Teddy Bear Classifier</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
            Select image to upload:
            <input type="file" name="file">
            <input type="submit" value="Upload Image">
        </form>
        Or submit a URL:
        <form action="/classify" method="get">
            <input type="url" name="url">
            <input type="submit" value="Fetch and analyze image">
        </form>
    """)


@app.route("/form")
def redirect_to_homepage(request):
    return RedirectResponse("/")


if __name__ == "__main__":
    if "serve" in sys.argv:
        uvicorn.run(app, host="0.0.0.0", port=8008)
