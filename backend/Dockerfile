FROM node:alpine

MAINTAINER Cuong Ba
#Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#Install app dependencies
COPY package.json /usr/src/app/
RUN npm install

#Bundle app source
COPY . /usr/src/app
EXPOSE 8080
EXPOSE 5858
CMD ["node", "--debug=5858", "server.js"]

