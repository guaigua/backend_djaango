FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
COPY entrypoint.sh .

RUN ["chmod", "+x", "./entrypoint.sh"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .