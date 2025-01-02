FROM ubuntu:latest
# Frontend Dockerfile
FROM node:20

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ARG BACKEND_URL
ENV BACKEND_URL=$BACKEND_URL

RUN npm run build

EXPOSE 3000

CMD ["node", ".output/server/index.mjs"]
