FROM ubuntu:20.04

RUN apt update -y && apt install -y python3
ADD . /app

CMD python3
