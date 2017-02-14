FROM python:3-slim

RUN mkdir -p /app/scripts

WORKDIR /app/scripts

RUN mkdir -p /app/config

VOLUME /app/config/

COPY requirements.txt /app/scripts/requirements.txt
COPY config.json.example /app/config/config.json.example
RUN pip3 install -r requirements.txt

ADD doormatic/ /app/scripts/
