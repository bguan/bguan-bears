FROM python:3.6-slim-stretch

RUN apt update
RUN apt install -y python3 gcc

# Install pytorch and fastai
RUN pip install torch
RUN pip install fastai

# Install starlette and uvicorn
RUN pip install starlette uvicorn python-multipart aiohttp

ADD bears.py bears.py
ADD bears.pkl bears.pkl

EXPOSE 8008

# Start the server
CMD ["python", "bears.py", "serve"]
