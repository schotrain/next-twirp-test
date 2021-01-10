FROM node:15-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
COPY package-lock.json /usr/src/app/

RUN npm ci 

COPY . /usr/src/app/
COPY ../protobufs /usr/src/app/

RUN protoc --plugin=./node_modules/.bin/protoc-gen-ts --ts_out ./generated --proto_path ./protobufs ./protobufs/*.proto

RUN npm run build

EXPOSE 3000
CMD [ "npm", "start" ]