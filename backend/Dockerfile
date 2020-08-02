FROM python:3.8.1-slim-buster as base

WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN python -m pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


###
# DEBUG
###
# FROM base as debug 
# RUN pip install ptvsd

COPY . /usr/src/app 
# WORKDIR /usr/src/app

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]