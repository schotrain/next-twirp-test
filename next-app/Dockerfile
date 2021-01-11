FROM node:15-alpine

ARG NEXT_PUBLIC_TWIRP_ENDPOINT

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN npm ci 

RUN npm run build

EXPOSE $PORT
CMD npx next start -p $PORT