# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /promptmaster

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && flask init-db && flask migrate

COPY . .

CMD [ "python3", "wsgi.py" ]

