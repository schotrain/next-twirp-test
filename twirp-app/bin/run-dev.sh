#!/bin/bash
. bin/build-protobufs.sh
poetry run uvicorn server.server:app --port=3001