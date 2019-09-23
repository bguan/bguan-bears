FROM python:3.6-slim-stretch

RUN apt update
RUN apt install -y gcc
RUN pip install fastai starlette uvicorn python-multipart aiohttp

ADD bears.py bears.py
ADD bears.pkl bears.pkl

EXPOSE 8008

# Start the server
CMD ["python", "bears.py", "serve"]
