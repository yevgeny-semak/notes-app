# pull base
FROM python:3.9-slim-buster

# set env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# create workdir
WORKDIR /code

# copy requirements
COPY Pipfile Pipfile.lock /code/

# install requirements
RUN pip install pipenv && mkdir .venv && pipenv install --system 

# copy project files
COPY . /code/

# open port
EXPOSE 8000