CREATE DATABASE chatbot;

\c chatbot

CREATE TABLE commands (
    command VARCHAR(20),
    server_url VARCHAR(200)
);
