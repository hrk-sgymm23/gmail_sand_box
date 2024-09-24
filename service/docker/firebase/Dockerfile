FROM node:20.14.0-alpine3.20

RUN apk update \
 && apk --no-cache add openjdk17-jre-headless \
 && rm -rf /var/cache/apk/*

RUN npm install -g firebase-tools