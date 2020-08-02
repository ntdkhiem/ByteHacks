FROM python:3.8.1-slim-buster as base

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

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

# CMD [ "gunicorn", "-b :5000" , "--workers=2", "--threads=4", "--worker-class=gthread", "app:create_app()" ]