FROM python:3.8

WORKDIR /cinema_project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /cinema_project/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /cinema_project/requirements.txt

COPY . /cinema_project/
