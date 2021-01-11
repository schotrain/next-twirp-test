#!/bin/bash
. bin/build-protobufs.sh
poetry run uvicorn server:app --port=3001