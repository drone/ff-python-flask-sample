FROM python:3.8

RUN apt-get update && apt-get install -y python3-dev
RUN ["pip3", "install", "pipenv"]
ENV PIPENV_VENV_IN_PROJECT 1
WORKDIR /usr/src/app
COPY ./app ./app
COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN ["pipenv", "install"]

COPY ./uWSGI .
EXPOSE 5000
CMD ["pipenv", "run", "uwsgi", "--ini", "app.ini"]
