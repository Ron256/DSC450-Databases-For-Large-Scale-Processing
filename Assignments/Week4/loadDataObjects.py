import sqlite3
import os
import csv

fileName = "data_module4_part2.txt"
os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/Week4')            # Change the directory to point to OneDrive.
# print(os.getcwd())

def readFileRows(fileName):
    """Read the contents of the file return the list of items"""
    fileContentsL = []
    fd = open(fileName, 'r')                                 # open the file.
    fileContents = fd.readlines()                            # returns a list containing each line in the file as a list item and assigns it to the list object

    fd.close()                                               # close the file.

    return fileContents                                      # return the list of list of objects

    

createTable1 = """
CREATE TABLE Employees
(
    First VARCHAR2(50),
    Last  VARCHAR2(50),
    Address VARCHAR2(100),
    CONSTRAINT Employees_PK PRIMARY KEY(FIRST, LAST)
);
"""

createTable2 = """
CREATE TABLE Jobs
(
    Job VARCHAR2(25),
    Salary NUMBER,
    Assistant VARCHAR(50),
    CONSTRAINT Jobs_PK PRIMARY KEY(Job)
);
"""

createTable3 = """
CREATE TABLE EmployeeJobs
(
    First VARCHAR2(50),
    Last  VARCHAR2(50),
    Job   VARCHAR2(25),
    CONSTRAINT EmployeeJobs_PK PRIMARY KEY(First, Last, Job),
    CONSTRAINT EmployeeJobsEmployees_FK Foreign Key(First, Last) REFERENCES Employees(First, Last),
    CONSTRAINT EmployeeJobs_Jobs_FK Foreign Key(Job) REFERENCES Jobs(Job)

);
"""

insertScript1 = """
INSERT OR IGNORE INTO Employees 
VALUES('%s', '%s', '%s');
"""

insertScript2 = """
INSERT OR IGNORE INTO Jobs 
VALUES('%s', '%s', '%s');
"""

insertScript3 = """INSERT OR IGNORE INTO EmployeeJobs 
VALUES('%s', '%s', '%s');
"""

conn = sqlite3.connect('dsc450.db')                                             # open the connection
cur = conn.cursor()                                                          # instantiate a cursor object


# Drop the tables if they exist
cur.execute("DROP TABLE IF EXISTS EmployeeJobs;")
cur.execute("DROP TABLE IF EXISTS Employees;")
cur.execute("DROP TABLE IF EXISTS Jobs;")

# execute the DDL to create the respective tables.
cur.execute(createTable1)
cur.execute(createTable2)
cur.execute(createTable3)

# Read the file contents

fileContents = readFileRows(fileName)                                       # helper function that returns the list of items of the file

for row in fileContents:
    itemValue = row.strip().split(',')
    cur.execute(insertScript1 %(itemValue[0].strip(), itemValue[1].strip(), itemValue[2].strip()))        # I am using the strip() to remove all white space characters
    cur.execute(insertScript2 %(itemValue[3].strip(), itemValue[4].strip(), itemValue[5].strip()))
    cur.execute(insertScript3 %(itemValue[0].strip(), itemValue[1].strip(), itemValue[3].strip()))

empRes = cur.execute("SELECT * FROM Employees;")
empResIObj = empRes.fetchall()                                               # create an iterator object by calling the fetchall() of the cursor object


jobRes = cur.execute("SELECT * FROM Jobs;")
jobResIObj = jobRes.fetchall()                                                # create an iterator object by calling the fetchall() of the cursor object


employeeJobsRes = cur.execute("SELECT * FROM EmployeeJobs;")
employeeJobsResIObj = employeeJobsRes.fetchall()                              # create an iterator object by calling the fetchall() of the cursor object

print("SELECT * FROM Employees \n %s \n" %(empResIObj))
print("SELECT * FROM Jobs \n %s \n" %(jobResIObj))
print("SELECT * FROM EmployeeJobs \n %s" %(employeeJobsResIObj))
conn.commit()
conn.close()


