###
# Build image
###
FROM node:15-alpine AS build

ARG NEXT_PUBLIC_TWIRP_ENDPOINT

RUN mkdir /build
WORKDIR /build

RUN apk add --no-cache python make g++

# Do npm ci before we copy code so the builds can be cahced in deps don't changge
COPY package*.json ./

# Generate the production node_modules
RUN npm ci --production
RUN mv node_modules /production_node_modules

# Generate the regular node_modules
RUN npm ci 

COPY . /build
RUN npm run build


###
# Run image
###
FROM node:15-alpine
ENV PORT 3000
RUN mkdir /app
WORKDIR /app

# Do npm ci before we copy code so the builds can be cahced in deps don't changge
COPY --from=build /build/package*.json ./
COPY --from=build /production_node_modules ./node_modules
COPY --from=build /build/public ./public
COPY --from=build /build/.next ./.next


EXPOSE $PORT
CMD npx next start -p $PORT
