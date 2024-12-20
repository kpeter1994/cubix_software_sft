FROM mongo:latest

COPY ./init-scripts/ /docker-entrypoint-initdb.d/

ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=admin

EXPOSE 27017
