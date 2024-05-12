CREATE SEQUENCE sequenc;
CREATE TABLE USERS (
  userID INTEGER PRIMARY KEY DEFAULT nextval('sequenc'),
  username varchar(63) NOT NULL UNIQUE,
  passwordhashed varchar(1023) NOT NULL,
  admin BOOLEAN DEFAULT false
);
CREATE TABLE STUDENTS (
  studentID INTEGER PRIMARY KEY NOT NULL,
  name varchar(63) NOT NULL,
  age INTEGER NOT NULL,
  studentLevel INTEGER NOT NULL,
  CGPA NUMERIC(3, 2) NOT NULL CONSTRAINT range CHECK (CGPA >= 0 AND CGPA <= 4),
  department varchar(63) NOT NULL
);

INSERT INTO USERS (username, passwordhashed) VALUES ('Sara', '3a6d64c24cf80b69ccda37650406467e8266667b50cfd0b984beb3651b129ed7');
INSERT INTO USERS (username, passwordhashed) VALUES ('2203173', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918');
INSERT INTO USERS (username, passwordhashed) VALUES ('22010442', '62cb81b5904a262ffaeed02abef36bfc540b09f964b8b0b636662f77ffce6714');
UPDATE USERS SET admin = true where username = 'Sara';
INSERT INTO STUDENTS VALUES 
  (2203173, 'Ahmed Mohamed Gaber', 19,2,4,'Intelligent Systems'),
  (2203177, 'Moataz Ali Ramadan', 20,2, 3.82,'Intelligent Systems'),
  (2203175, 'Hazem Ahmed Abdelfatah', 20,2, 4,'Intelligent Systems'),
  (22010442, 'Youssef Salah Mostafa', 19,2, 3.76,'Intelligent Systems'),
  (2202140, 'Abdelrahman Islam Gad', 20,2, 4,'Business Analytics');
  
  
 