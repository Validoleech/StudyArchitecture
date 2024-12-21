FROM postgres:latest

ENV POSTGRES_DB=auth_service
ENV POSTGRES_USER=auth_admin
ENV POSTGRES_PASSWORD=auth_password

COPY db.sql /docker-entrypoint-initdb.d/
COPY create_db.sh /docker-entrypoint-initdb.d/