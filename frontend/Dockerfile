FROM node:latest

WORKDIR /frontend
COPY . /frontend

RUN npm run build
RUN npm install -g serve
