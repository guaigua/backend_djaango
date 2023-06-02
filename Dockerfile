FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY . .

RUN ["chmod", "+x", "./entrypoint.sh"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["/code/entrypoint.sh"]

