#!/bin/bash
rotoc --plugin=$GOPATH/bin/protoc-gen-twirpy --python_out=./generated --twirpy_out=./generated --proto_path=../protobufs ../protobufs/*.proto