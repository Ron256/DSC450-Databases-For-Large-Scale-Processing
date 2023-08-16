
CREATE TABLE Employees
(
    First VARCHAR2(50),
    Last  VARCHAR2(50),
    Address VARCHAR2(100),
    CONSTRAINT Employees_PK PRIMARY KEY(FIRST, LAST)
);


CREATE TABLE Jobs
(
    Job VARCHAR2(25),
    Salary NUMBER,
    Assistant VARCHAR(50),
    CONSTRAINT Jobs_PK PRIMARY KEY(Job)
);

CREATE TABLE EmployeeJobs
(
    First VARCHAR2(50),
    Last  VARCHAR2(50),
    Job   VARCHAR2(25),
    CONSTRAINT EmployeeJobs_PK PRIMARY KEY(First, Last, Job),
    CONSTRAINT EmployeeJobsEmployees_FK Foreign Key(First, Last) REFERENCES Employees(First, Last),
    CONSTRAINT EmployeeJobs_Jobs_FK Foreign Key(Job) REFERENCES Jobs(Job)

);