FROM postgres:latest

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD admin
ENV POSTGRES_DB Students

WORKDIR /project

COPY Students.sql /docker-entrypoint-initdb.d/