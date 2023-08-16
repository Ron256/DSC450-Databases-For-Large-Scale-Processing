/*
CREATE TABLE Student
(
    SID NUMBER,
    sname VARCHAR2(50),
    sstatus VARCHAR2(50),
    CONSTRAINT Student_PK Primary Key(SID)
);

CREATE TABLE Course
(
    CourseId NUMBER,
    CourseDesc VARCHAR2(50),
    CourseUnits NUMBER,
    CONSTRAINT CoursePK PRIMARY KEY(CourseId)
);

CREATE TABLE Enrollment
(
    SID NUMBER,
    CourseId NUMBER,
    CONSTRAINT EnrollmentPK PRIMARY KEY(SID, CourseId),
    CONSTRAINT EnrollmentCourse_FK Foreign Key(CourseId) REFERENCES Course(CourseId),
    CONSTRAINT EnrollmentStudent_FK Foreign Key(SID) REFERENCES Student(SID)
);
*/
/*
INSERT INTO Student VALUES(1, 'Jack', 'Grad');
INSERT INTO Student VALUES(2, 'Jane', 'UGrad');
INSERT INTO Student VALUES(3, 'Jack', 'Grad');
INSERT INTO Student VALUES(4, 'Karen', 'UGrad');
*/

--SELECT * FROM Student;

/*
INSERT INTO Course VALUES(100, 'Intro to Databases', 4);
INSERT INTO Course VALUES(200, 'Research Colloquium', 2);
INSERT INTO Course VALUES(300, 'Database Systems For Analytics', 4);
*/

/*
INSERT INTO Enrollment VALUES(1, 100);
INSERT INTO Enrollment VALUES(3, 200);
INSERT INTO Enrollment VALUES(2, 100);
INSERT INTO Enrollment VALUES(4, 300);
*/

SELECT * FROM Enrollment;

SELECT student.sid, student.sname, student.sstatus, enrollment.courseid 
FROM Student LEFT OUTER JOIN Enrollment
ON student.sid = enrollment.sid;


CREATE TABLE Chauffeurs
(
    LicenseNumber NUMBER,
    Renewed VARCHAR2(50),
    Status VARCHAR2(50),
    StatusDate DATE,
    DriverType VARCHAR2(25),
    LicenseType VARCHAR2(25),
    OriginalIssue DATE,
    NAME VARCHAR2(100),
    Sex VARCHAR2(10),
    ChauffeurCity VARCHAR2(50),
    ChauffeurState VARCHAR2(50),
    RecordNumber VARCHAR(50),
    CONSTRAINT Chauffeurs_PK PRIMARY KEY (LicenseNumber)
);


CREATE TABLE Tweets
(
    Created_at DATE,
    id  VARCHAR2(100),
    text VARCHAR2(300),
    source VARCHAR2(100),
    in_reply_to_user_id VARCHAR2(100),
    in_reply_to_screen_name VARCHAR2(100),
    in_reply_to_status_id VARCHAR2(100),
    retweet_count NUMBER,
    contributors VARCHAR2(100)
);
