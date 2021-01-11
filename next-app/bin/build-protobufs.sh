#!/bin/bash
protoc --plugin=./node_modules/.bin/protoc-gen-ts --ts_out ./generated --proto_path ../protobufs ../protobufs/*.proto