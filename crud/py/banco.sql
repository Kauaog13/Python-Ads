CREATE DATABASE facsenac;
USE facsenac;

CREATE TABLE usuarios (
  cod INT PRIMARY KEY AUTO INCREMENT,
  nome VARCHAR(50) NOT NULL,
  cidade VARCHAR(30),
  uf CHAR(2),
  data DATE
);