FROM python:3.7
RUN mkdir /app
WORKDIR /app

RUN pip install poetry
RUN poetry config settings.virtualenvs.create false

COPY poetry.lock /app/
COPY pyproject.toml /app/
COPY . /app/
COPY ../protobufs /app/

RUN poetry install
RUN protoc --python_out=./generated --twirpy_out=./generated --proto_path=../protobufs ../protobufs/*.proto

EXPOSE 3001
CMD [ "poetry ", "run", "uvicorn", "server:app", "--port=3001" ]