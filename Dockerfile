# pull base
FROM python:3.9

# create workdir
WORKDIR /code

# set env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# copy requirements
COPY Pipfile Pipfile.lock /code/

# install requirements
RUN pip install pipenv && mkdir .venv && pipenv install --system

# copy project files
COPY . /code/