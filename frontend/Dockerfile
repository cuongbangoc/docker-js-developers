FROM node:alpine

MAINTAINER Cuong Ba

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

#Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN npm install -g bower grunt-cli

#Install app dependencies
COPY package.json /usr/src/app/
COPY bower.json /usr/src/app/
RUN npm install

# RUN bower install
RUN bower --allow-root install

#Bundle app source
ADD . /usr/src/app
EXPOSE 9000
EXPOSE 35729
CMD ["grunt", "serve", "--force"]

