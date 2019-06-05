FROM python:3.6-alpine

RUN apk add --no-cache --update \
  build-base

RUN adduser -D hello_app

WORKDIR /home/hello_app

COPY ./requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY ./app app
COPY ./hello_app.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP hello_app.py

RUN chown -R hello_app:hello_app ./
USER hello_app

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

