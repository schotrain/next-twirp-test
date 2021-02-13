FROM python:3.9-alpine
ENV PORT 3001
RUN mkdir /app
WORKDIR /app

RUN apk add --no-cache protoc gcc build-base libffi-dev openssl-dev postgresql-dev rust

RUN pip install poetry
RUN poetry config virtualenvs.create false --local

COPY . /app

RUN poetry install

EXPOSE $PORT
CMD poetry run uvicorn server.server:app --host 0.0.0.0 --port=$PORT