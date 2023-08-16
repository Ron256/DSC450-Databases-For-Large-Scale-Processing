/*
ALTER TABLE WrittenBooks
DROP CONSTRAINT WrittenBooks_PK;

ALTER TABLE WrittenBooks
DROP CONSTRAINT WrittenBooks_FK1;

ALTER TABLE WrittenBooks
DROP CONSTRAINT WrittenBooks_FK2;

DROP TABLE WrittenBooks;

ALTER TABLE Books
DROP CONSTRAINT Books_PK;

ALTER TABLE Books
DROP CONSTRAINT Books_FK;

DROP TABLE Books;


ALTER TABLE Publishers
DROP CONSTRAINT Publishers_PK;

DROP TABLE Publishers;

ALTER TABLE Authors
DROP CONSTRAINT Authors_PK;

DROP TABLE Authors;

--Part 1-1
CREATE TABLE Authors
( 
    ID NUMBER(10,0), 
    FirstName VARCHAR2(50), 
    LastName VARCHAR2(50), 
    BirthDate DATE,
    CONSTRAINT Authors_PK PRIMARY KEY(ID)
);

CREATE TABLE Publishers
(
    PubNumber NUMBER(10,0), 
    Name VARCHAR2(25), 
    Address VARCHAR2(50), 
    CONSTRAINT Publishers_PK PRIMARY KEY(PubNumber)
);

CREATE TABLE Books
(
    ISBN VARCHAR2(50), 
    Title VARCHAR2(50), 
    PubNumber NUMBER(10,0),
    CONSTRAINT Books_PK PRIMARY KEY(ISBN),
    CONSTRAINT Books_FK FOREIGN KEY (PubNumber) 
    REFERENCES Publishers(PubNumber)
);

CREATE TABLE WrittenBooks
(
    ID NUMBER(10,0), 
    ISBN VARCHAR2(50), 
    AuthorPosition NUMBER(10,0),
    CONSTRAINT WrittenBooks_PK PRIMARY KEY(ID, ISBN), 
    CONSTRAINT WrittenBooks_FK1 FOREIGN KEY(ISBN) REFERENCES Books(ISBN), 
    CONSTRAINT WrittenBooks_FK2 FOREIGN KEY(ID) REFERENCES Authors(ID)
);

--Part 1-2

INSERT INTO Authors(FirstName, LastName, ID, BirthDate)
Values('King', 'Stephen', 2, TO_DATE('September 9 1947', 'Month dd YYYY'));

INSERT INTO Authors(FirstName, LastName, ID, BirthDate)
VALUES('Asimov', 'Isaac', 4, TO_DATE('January 2 1921', 'Month dd YYYY'));

INSERT INTO Authors(FirstName, LastName, ID, BirthDate)
VALUES('Verne', 'Jules', 7, TO_DATE('February 8 1828', 'Month dd YYYY'));

INSERT INTO Authors(FirstName, LastName, ID, BirthDate)
VALUES('Rowling', 'Joanne', 37, TO_DATE('July 31 1965', 'Month dd YYYY'));


INSERT INTO Publishers(Name, PubNumber, Address)
VALUES('Bloomsbury Publishing', 17, 'London Borough of Camden');

INSERT INTO Publishers(Name, PubNumber, Address)
VALUES('Arthur A. Levine Books', 18, 'New York City');

INSERT INTO Books(ISBN, Title, PubNumber)
VALUES('1111-111', 'Databases from outer space', 17);

INSERT INTO Books(ISBN, Title, PubNumber)
VALUES('2222-222', 'Revenge of SQL', 17);

INSERT INTO Books(ISBN, Title, PubNumber)
VALUES('3333-333', 'The night of the living databases', 18);


INSERT INTO WrittenBooks(ID, ISBN, AuthorPosition)
VALUES('2', '1111-111', 1);

INSERT INTO WrittenBooks(ID, ISBN, AuthorPosition)
VALUES('4', '1111-111', 2);

INSERT INTO WrittenBooks(ID, ISBN, AuthorPosition)
VALUES('4', '2222-222', 2);

INSERT INTO WrittenBooks(ID, ISBN, AuthorPosition)
VALUES('7', '2222-222', 1);

INSERT INTO WrittenBooks(ID, ISBN, AuthorPosition)
VALUES('37', '3333-333', 1);

INSERT INTO WrittenBooks(ID, ISBN, AuthorPosition)
VALUES('2', '3333-333', 2);

*/
--SELECT * FROM Authors;
--SELECT * FROM Publishers;

--SELECT * FROM Books;
--SELECT * FROM WrittenBooks;

--Part 3



/*
ALTER TABLE Students
DROP CONSTRAINT Students_PK;

ALTER TABLE Students
DROP CONSTRAINT Students_FK;

DROP TABLE Students;

ALTER TABLE Advisors
DROP CONSTRAINT Advisors_PK;

ALTER TABLE Advisors
DROP CONSTRAINT Advisors_FK;

DROP TABLE Advisors;


ALTER TABLE Departments
DROP CONSTRAINT Departments_PK;

DROP TABLE Departments;
*/

--Part 1-3
CREATE TABLE Departments
(
    Name VARCHAR2(50), 
    Chair VARCHAR2(50), 
    Endowment VARCHAR2(50), 
    CONSTRAINT Departments_PK PRIMARY KEY(Name)
);


CREATE TABLE Advisors
(
    ID NUMBER(10, 0),
    Name VARCHAR2(50), 
    Address VARCHAR2(50), 
    ResearchArea VARCHAR2(100), 
    DepartmentName VARCHAR2(50),
    CONSTRAINT Advisors_PK PRIMARY KEY(ID),
    CONSTRAINT Advisors_FK FOREIGN KEY(DepartmentName) 
    REFERENCES Departments(Name)
);

CREATE TABLE Students
(
    StudentID NUMBER(10, 0), 
    FirstName VARCHAR2(50), 
    LastName VARCHAR2(50), 
    DOB DATE, 
    Telephone VARCHAR2(25), 
    AID NUMBER(10, 0), 
    CONSTRAINT Students_PK PRIMARY KEY(StudentID), 
    CONSTRAINT Students_FK FOREIGN KEY(AID) REFERENCES Advisors(ID)
);

