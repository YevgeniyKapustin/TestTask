FROM python:3.10

ARG DEBIAN_FRONTEND=noninteractive

ENV PYTHONUNBUFFERED=1

RUN apt update

WORKDIR /kapusta

COPY . .

RUN pip install -r requirements.txt

CMD python manage.py runserver
