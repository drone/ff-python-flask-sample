# Flask app using harness feature flags

this project is an example of how to use the harnes-featureflags in a simple flask application

## Install

You will need docker and docker-compose

## Run

for running sample application you can use docker-compose:
```
docker-compose up --build
```

or just run command:

```
make start
```

## Test urls

```
http://localhost:8081/api/flags
```

## Stop application servers

```
make stop
```
