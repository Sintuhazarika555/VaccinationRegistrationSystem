CREATE DATABASE practical;

USE practical;

CREATE TABLE vaccine (
    certificateid INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    id VARCHAR(50),
    idnumber BIGINT,
    vaccinename VARCHAR(50),
    doseno INT,
    gmail VARCHAR(100),
    contactno BIGINT
);
