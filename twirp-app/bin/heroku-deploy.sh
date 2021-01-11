#!/bin/bash
. bin/build-protobufs.sh
git subtree push --prefix web heroku-twirp-app master