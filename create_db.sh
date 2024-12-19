psql -U postgres
CREATE DATABASE auth_service;
CREATE USER auth_admin WITH PASSWORD 'auth_password';
GRANT ALL PRIVILEGES ON DATABASE auth_service TO auth_admin;