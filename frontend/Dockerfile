FROM ubuntu:latest
# Frontend Dockerfile
FROM node:20

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm install

RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "dev"]
