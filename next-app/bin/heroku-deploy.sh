#!/bin/bash
. bin/build-protobufs.sh
cd ..
git subtree push --prefix next-app heroku-next-app master