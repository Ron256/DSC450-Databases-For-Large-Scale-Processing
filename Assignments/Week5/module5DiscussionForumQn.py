# Author : Ronaldlee Ejalu
# Course: DSC 450
# Assigment: module 5 Discussion forum

import sqlite3
import os
import collections
import json

createtbla = """
CREATE TABLE Student
(
    SID NUMBER,
    sname VARCHAR2(50),
    sstatus VARCHAR2(50),
    CONSTRAINT Student_PK Primary Key(SID)
);
"""

createtblb = """
CREATE TABLE Course
(
    CourseId NUMBER,
    CourseDesc VARCHAR2(50),
    CourseUnits NUMBER,
    CONSTRAINT CoursePK PRIMARY KEY(CourseId)
);
"""

createtblc = """
CREATE TABLE Enrollment
(
    SID NUMBER,
    CourseId NUMBER,
    CONSTRAINT EnrollmentPK PRIMARY KEY(SID, CourseId),
    CONSTRAINT EnrollmentCourse_FK Foreign Key(CourseId) REFERENCES Course(CourseId),
    CONSTRAINT EnrollmentStudent_FK Foreign Key(SID) REFERENCES Student(SID)
);
"""

insertScript1 = """INSERT OR IGNORE INTO Student VALUES('%s', '%s', '%s');"""
insertScript2 = """INSERT OR IGNORE INTO Course VALUES('%s', '%s', '%s');"""
insertScript3 = """INSERT OR IGNORE INTO Enrollment VALUES('%s', '%s');"""

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/Week5')            # Change the directory to point to OneDrive.
print(os.getcwd())

conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()

# Drop the tables if they exist
cursor.execute("DROP TABLE IF EXISTS Student;")
cursor.execute("DROP TABLE IF EXISTS Course;")
cursor.execute("DROP TABLE IF EXISTS Enrollment;")

# Execute the DDL to create the respective tables
cursor.execute(createtbla)
cursor.execute(createtblb)
cursor.execute(createtblc)

# insert the data into the respective tables
cursor.execute(insertScript1 %(1, 'Jack', 'Grad'))
cursor.execute(insertScript1 %(2, 'Jane', 'UGrad'))
cursor.execute(insertScript1 %(3, 'Jack', 'Grad'))
cursor.execute(insertScript1 %(4, 'Karen', 'UGrad'))

cursor.execute(insertScript2 %(100, 'Intro to Databases', 4))
cursor.execute(insertScript2 %(200, 'Research Colloquium', 2))
cursor.execute(insertScript2 %(300, 'Database Systems For Analytics', 4))

cursor.execute(insertScript3 %(1, 100))
cursor.execute(insertScript3 %(3, 200))
cursor.execute(insertScript3 %(2, 100))
cursor.execute(insertScript3 %(4, 300))

# querying the data from the database tables
# For debugging purposes
# studentRes = cursor.execute("SELECT * FROM Student;")
# studentResIObj = studentRes.fetchall()                                  # create an iterator object by calling the fetchall() of the cursor object
# print("SELECT * FROM Student; \n %s \n" %(studentResIObj))

# courseRes = cursor.execute("SELECT * FROM Course;")
# courseResIObj = courseRes.fetchall()                                    # create an iterator object by calling the fetchall() of the cursor object
# print("SELECT * FROM Course; \n %s \n" %(courseResIObj))

# enrollmentRes = cursor.execute("SELECT * FROM Enrollment;")
# enrollmentResIObj = enrollmentRes.fetchall()
# print("SELECT * FROM Enrollment; \n %s \n" %(enrollmentResIObj))        # create an iterator object by calling the fetchall() of the cursor object

studentEnrollmentScript = """
SELECT student.sid, student.sname, student.sstatus, enrollment.courseid 
FROM Student LEFT OUTER JOIN Enrollment
ON student.sid = enrollment.sid;"""

# executing the denomalized script combining both Student and enrollment
studEnroll = cursor.execute(studentEnrollmentScript)

studEnrollIObj = studEnroll.fetchall()                                  # create an iterator object by calling the fetchall() of the cursor object

# transform the query to objects of key value pairs
objectList = []                                                          # declare an empty list
for item in studEnrollIObj:
    dict = {}
    dict['SID'] = item[0]
    dict['SName'] = item[1]
    dict['SStatus'] = item[2]
    dict['CourseId'] = item[3]
    objectList.append(dict)                                         # append the dict to a list

jsonRep = json.dumps({'studentEnrollment':objectList})                                           # convert the list of dictionaries into a json object

print("The Json representation of the denormalized schema of Student and enrollment is %s" %(jsonRep))

studentEnrollmentDict = json.loads(jsonRep)   # converts the content of the Json object to a dictionary
# print(type(studentEnrollmentDict))

# get the list and iterate through the loop
studentEnrollment = studentEnrollmentDict["studentEnrollment"]
print("\nThe Courses taken by the student called Jack are:")

for studentRow in studentEnrollment:
    if 'Jack' in studentRow["SName"]:
        print(studentRow["CourseId"])




conn.commit()
conn.close()