FROM node:15-alpine AS build

ARG NEXT_PUBLIC_TWIRP_ENDPOINT

RUN mkdir /build
WORKDIR /build

RUN apk add --no-cache python make g++

# Do npm ci before we copy code so the builds can be cahced in deps don't changge
COPY package*.json ./
RUN npm ci 

COPY . /build
RUN npm run build


FROM node:15-alpine
ENV PORT 3000
RUN mkdir /app
WORKDIR /app
COPY --from=build /build /app
EXPOSE $PORT
CMD npx next start -p $PORT