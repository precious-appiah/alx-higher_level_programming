-- create two table with PK constraints
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE btn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE AUTO GENERATED PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
