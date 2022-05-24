FROM node:latest

WORKDIR /frontend

COPY package*.json ./
RUN npm install

COPY . $WORKDIR

RUN npm run build
RUN npm install -g serve
