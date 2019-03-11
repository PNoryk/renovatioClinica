FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY Pipfile.lock /code/
RUN pip install pipenv
RUN pipenv install
COPY . /code/