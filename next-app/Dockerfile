FROM node:15-alpine AS build
ARG NEXT_PUBLIC_TWIRP_ENDPOINT
RUN mkdir /build
WORKDIR /build
RUN apk add --no-cache python make g++
COPY . /build
RUN npm ci 
RUN npm run build
RUN npm ci --production


FROM node:15-alpine
RUN mkdir /app
WORKDIR /app
COPY --from=build /build /app
EXPOSE $PORT
CMD npx next start -p $PORT