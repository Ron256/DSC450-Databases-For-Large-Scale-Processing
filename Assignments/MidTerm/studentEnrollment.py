# Author: Ronaldlee Ejalu
# DSC 450 MidTerm Exam.
# Part 4e1
import sqlite3
import os
import csv

fileName = "StudentEnrollments.txt"
os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/MidTerm')                                                                 # Change the directory to point to OneDrive.

createTable1 = """
Create table Student
(
    StudentID VARCHAR2(25),
    Name VARCHAR2(50),
    Address VARCHAR2(100),
    GradYear NUMBER(4),
    CONSTRAINT Student_PK Primary Key (StudentID)
);
"""

createTable2 = """
Create table Course
    (
    CName VARCHAR2(50),
    Department VARCHAR2(50),
    Credits NUMBER(4),
    CONSTRAINT Course_PK Primary Key (CName)
);
"""

createTable3 = """
Create table Grade
(
CName VARCHAR2(50), 
StudentID VARCHAR2(25), 
CGrade NUMBER(4,2),
CONSTRAINT Grade_PK Primary Key(CName, StudentID),
CONSTRAINT Grade_FK1 Foreign Key(CName) REFERENCES Course(CName),
CONSTRAINT Grade_FK2 Foreign Key(StudentID) REFERENCES Student(StudentID)
);
"""

studentInsertScriptsL = ["INSERT INTO Student VALUES('001', 'Ronaldlee Ejalu', '4352 One Ford Place Detroit MI', 2023);", 
"INSERT INTO Student VALUES('002', 'Abby Keller', '134 HollyWood Dr Seattle WA', 2022);", 
"INSERT INTO Student VALUES('003', 'Pinki Sharma', '12 Michigan Avenue Chicago IL', 2021);", 
"INSERT INTO Student VALUES('004', 'Felicia Zuri', '14 Michigan Avenue Chicago IL', 2021);"]

courseInsertScriptsL = ["INSERT INTO Course VALUES('Databases for Large Scale Analytics', 'CDM', 4);", 
"INSERT INTO Course VALUES('Natural Language Processing', 'Computer Science', 4);", 
"INSERT INTO Course VALUES('Neural Networks and Deep Learning', 'Computer Science', 4);", 
"INSERT INTO Course VALUES('Python Programming', 'Computer Science', 4);"]

gradeInsertScriptsL = ["INSERT INTO Grade VALUES('Databases for Large Scale Analytics','002',4.0);", 
"INSERT INTO Grade VALUES('Natural Language Processing','002',4.0);", 
"INSERT INTO Grade VALUES('Python Programming','002',3.1);", 
"INSERT INTO Grade VALUES('Natural Language Processing','003',4.0);", 
"INSERT INTO Grade VALUES('Python Programming','003',3.1);", 
"INSERT INTO Grade VALUES('Databases for Large Scale Analytics','003',3.6);", 
"INSERT INTO Grade VALUES('Python Programming','004',3.1);", 
"INSERT INTO Grade VALUES('Natural Language Processing','004',3.5);"]


createViewScript = """
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
LEFT OUTER JOIN Course ON course.cname = grade.cname
UNION 
SELECT * FROM (
SELECT Student.StudentID, 
Student.Name, 
Student.Address, 
Student.GradYear, 
Course.CName, 
Course.Department, 
Course.Credits, 
Grade.CGrade
FROM  Course LEFT OUTER JOIN Grade 
ON course.cname = grade.cname
LEFT OUTER JOIN Student ON Student.StudentID = Grade.StudentID
EXCEPT
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
LEFT OUTER JOIN Course ON course.cname = grade.cname
)A;
"""

selectQuery = """SELECT * FROM StudentRecs;"""

dropTable1 = """DROP TABLE IF EXISTS Student;"""
dropTable2 = """DROP TABLE IF EXISTS Course;"""
dropTable3 = """DROP TABLE IF EXISTS Grade;"""

dropTableScriptsL = [dropTable1, dropTable2, dropTable3]
createTableSciptsL = [createTable1, createTable2, createTable3]

conn = sqlite3.connect('dsc450.db')                                                     # open the connection
cur = conn.cursor()                                                                     # instantiate a cursor object
def executeScripts(cur, sqlScriptL):
    """ A function that executes the SQLite DDL scripts"""
    for itemScript in sqlScriptL:
        cur.execute(itemScript)

def insertTableData(cur, tableInsertScript):
    """ A function that executes the SQLInsertScripts to insert data into the sqlite database"""
    for insertScript in tableInsertScript:
        cur.execute(insertScript)

def writeContentsToFile(fileName, IObj):
    """ Function that writes the list of tuples to a csv file"""

    # use newline = '' to avoid redudant blank lines in the file
    with open(fileName, 'w', newline='') as csvf:
        csvWriter = csv.writer(csvf)
        for rowItem in IObj:
            csvWriter.writerow(rowItem)
    csvf.close()                                                                    # close the file 
    

# drop the tables if they exist
executeScripts(cur,dropTableScriptsL)                                               # helper function to execute the SQLite DDL scripts


# create the respective tables:
executeScripts(cur, createTableSciptsL)                                             # helper function to execute the SQLite DDL scripts   

# insert data into the respective tables
insertTableData(cur, studentInsertScriptsL)                                         # a helper function to execute the list of insert scripts.
insertTableData(cur, courseInsertScriptsL)
insertTableData(cur, gradeInsertScriptsL)

# drop the view if exists
cur.execute("DROP VIEW IF EXISTS StudentRecs;")

# create the view
cur.execute(createViewScript)

# query the data from the view
studentRecordsRes= cur.execute(selectQuery)
studentRecsIObj = studentRecordsRes.fetchall()                                      # create an iterator object by calling the fetchall() of the cursor object

# print("The contents of the view: SELECT * FROM StudentRecs is \n %s" %(studentRecsIObj))

writeContentsToFile(fileName, studentRecsIObj)                                      # helper function to write the list of tuples to a file. 

avgGradYearScript = """
SELECT Department, AVG(GradYear) AS AverageGradYear 
FROM studentrecs WHERE GradYear IS NOT NULL
AND Department IS NOT NULL
GROUP BY Department;"""

departmentAvgRes = cur.execute(avgGradYearScript)
departmentAvgResIObj = departmentAvgRes.fetchall()                               # create an iterator object by calling the fetchall() of the cursor object

print("The results of %s  \n %s"%(avgGradYearScript, departmentAvgResIObj))
conn.commit()
conn.close()
