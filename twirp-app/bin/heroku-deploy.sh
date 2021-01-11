#!/bin/bash
. bin/build-protobufs.sh
cd ..
git subtree push --prefix twirp-app heroku-twirp-app master