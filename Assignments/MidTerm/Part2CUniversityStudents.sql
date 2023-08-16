

DROP TABLE Student CASCADE CONSTRAINTS;
DROP TABLE Course CASCADE CONSTRAINTS;
DROP TABLE Grade CASCADE CONSTRAINTS;
Create table Student
(
    StudentID VARCHAR2(25),
    Name VARCHAR2(50),
    Address VARCHAR2(100),
    GradYear NUMBER(4),
    CONSTRAINT Student_PK Primary Key (StudentID)
);

Create table Course
    (
    CName VARCHAR2(50),
    Department VARCHAR2(50),
    Credits NUMBER(4),
    CONSTRAINT Course_PK Primary Key (CName)
);

Create table Grade
(
CName VARCHAR2(50), 
StudentID VARCHAR2(25), 
CGrade NUMBER(4),
CONSTRAINT Grade_PK Primary Key(CName, StudentID),
CONSTRAINT Grade_FK1 Foreign Key(CName) REFERENCES Course(CName),
CONSTRAINT Grade_FK2 Foreign Key(StudentID) REFERENCES Student(StudentID)
);

INSERT INTO Student VALUES('001', 'Ronaldlee Ejalu', '4352 One Ford Place Detroit MI', 2023);
INSERT INTO Student VALUES('002', 'Abby Keller', '134 HollyWood Dr Seattle WA', 2022);
INSERT INTO Student VALUES('003', 'Pinki Sharma', '12 Michigan Avenue Chicago IL', 2021);
INSERT INTO Student VALUES('004', 'Felicia Zuri', '14 Michigan Avenue Chicago IL', 2021);

INSERT INTO Course VALUES('Databases for Large Scale Analytics', 'CDM', 4);
INSERT INTO Course VALUES('Natural Language Processing', 'Computer Science', 4);
INSERT INTO Course VALUES('Neural Networks and Deep Learning', 'Computer Science', 4);
INSERT INTO Course VALUES('Python Programming', 'Computer Science', 4);

INSERT INTO Grade VALUES('Databases for Large Scale Analytics','002',80);
INSERT INTO Grade VALUES('Natural Language Processing','002',90);
INSERT INTO Grade VALUES('Python Programming','002',75);
INSERT INTO Grade VALUES('Natural Language Processing','003',90);
INSERT INTO Grade VALUES('Python Programming','003',75);
INSERT INTO Grade VALUES('Databases for Large Scale Analytics','003',87);
INSERT INTO Grade VALUES('Python Programming','004',75);
INSERT INTO Grade VALUES('Natural Language Processing','004',85);


CREATE VIEW StudentRecs 
AS
SELECT Student.StudentID, 
Student.Name, 
Student.Address, 
Student.GradYear, 
Course.CName, 
Course.Department, 
Course.Credits, 
Grade.CGrade
FROM Student LEFT OUTER JOIN Grade 
ON Student.StudentID = Grade.StudentID
LEFT OUTER JOIN Course ON course.cname = grade.cname;

SELECT * FROM StudentRecs;

