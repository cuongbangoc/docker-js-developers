FROM node:alpine
MAINTAINER Cuong Ba

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN node -v && npm -v

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install
RUN mv /usr/src/app/node_modules /usr/src/node_modules

RUN npm install -g nodemon

# Bundle app source
COPY . /usr/src/app

EXPOSE 8080
EXPOSE 5858
# CMD ["node", "--debug=5858", "server.js"]
# CMD ["pm2", "start", "-x", "--no-daemon", "server.js", "--watch"]
# CMD ["nodemon", "--debug=5858", "-L", "server.js"]
CMD ["nodemon", "-L", "server.js"]
