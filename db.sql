CREATE DATABASE auth_service;

\c auth_service

CREATE USER auth_admin WITH PASSWORD 'auth_password';

GRANT ALL PRIVILEGES ON DATABASE auth_service TO auth_admin;

CREATE TABLE users (
    login VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    score REAL DEFAULT 0.0
);