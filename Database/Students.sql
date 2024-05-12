CREATE SEQUENCE sequenc;
CREATE TABLE USERS (
  userID INTEGER PRIMARY KEY DEFAULT nextval('sequenc'),
  username varchar(63) NOT NULL UNIQUE,
  passwordhashed varchar(1023) NOT NULL,
  admin BOOLEAN DEFAULT false
);
CREATE TABLE STUDENTS (
  studentID varchar(16) PRIMARY KEY NOT NULL,
  name varchar(63) NOT NULL,
  age INTEGER NOT NULL,
  studentLevel INTEGER NOT NULL  CONSTRAINT levelrange CHECK (studentLevel >= 1),
  CGPA NUMERIC(3, 2) NOT NULL CONSTRAINT range CHECK (CGPA >= 0 AND CGPA <= 4),
  department varchar(63) NOT NULL
);

INSERT INTO USERS (username, passwordhashed) VALUES ('Sara', '3a6d64c24cf80b69ccda37650406467e8266667b50cfd0b984beb3651b129ed7');
INSERT INTO USERS (username, passwordhashed) VALUES ('2203173', 'b9475867111b893effeeec0a2cf993b8a9d64b871d8a859e54121a9fe53d03f9');
INSERT INTO USERS (username, passwordhashed) VALUES ('2203175', '212971f1fc007256f551d8676c2ae6e78982ac133ced0f3110db8db85d8d268d');
INSERT INTO USERS (username, passwordhashed) VALUES ('2203177', '2c50bdef40581b20d931d47f1545a05b1bc964e83dc9fcd7becd4d284fc7bb68');
INSERT INTO USERS (username, passwordhashed) VALUES ('2202140', 'b6a4ad19f5f316d8f3061521e2ca40d3d0be16889be4014f8b606e1a103e74e0');
INSERT INTO USERS (username, passwordhashed) VALUES ('22010442', 'f420b60d5c0c9af7670c37d3f4cea7f8a02c3bddbcae910f6855e8844bdaca07');
UPDATE USERS SET admin = true where username = 'Sara';
INSERT INTO STUDENTS VALUES 
  ('2203173', 'Ahmed Mohamed Gaber', 19,2,3.18,'Intelligent Systems'),
  ('2203177', 'Moataz Ali Ramadan', 20,2, 3.82,'Intelligent Systems'),
  ('2203175', 'Hazem Ahmed Abdelfatah', 20,2, 3.64,'Intelligent Systems'),
  ('22010442', 'Youssef Salah Mostafa', 19,2, 3.76,'Intelligent Systems'),
  ('2202140', 'Abdelrahman Islam Gad', 20,2, 3.91,'Business Analytics');
  
  
 