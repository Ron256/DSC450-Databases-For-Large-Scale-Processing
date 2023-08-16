# Author: Ronaldlee Ejalu
# Course: DSC 450
# HomeWork Assignment 5 Module part 2
import os
import csv
import urllib.request
import sqlite3

os.chdir("C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/Week5")

createtbl = """

CREATE TABLE Chauffeurs
(
    LicenseNumber NUMBER,
    Renewed VARCHAR2(50),
    Status VARCHAR2(50),
    StatusDate DATE,
    DriverType VARCHAR2(25),
    LicenseType VARCHAR2(25),
    OriginalIssue DATE,
    CName VARCHAR2(100),
    Sex VARCHAR2(10),
    ChauffeurCity VARCHAR2(50),
    ChauffeurState VARCHAR2(50),
    RecordNumber VARCHAR(50)--,
    --CONSTRAINT Chauffeurs_PK PRIMARY KEY (LicenseNumber)
);
"""

insertScript = """
INSERT  INTO Chauffeurs VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
"""
conn = sqlite3.connect('dsc450.db')                                                                             # open the connection
cur = conn.cursor()                                                                                             # instanciate a cursor object

# Drop the table if it exist
cur.execute("DROP TABLE IF EXISTS Chauffeurs;")

# execute the ddl to cretate the respective tables.
cur.execute(createtbl)


url_link = "http://dbgroup.cdm.depaul.edu/DSC450/Public_Chauffeurs_Short_hw3.csv"
response = urllib.request.urlopen(url_link)

# decode urlopen's response, which is in bytes, into a valid local encoding
responseLines = [row.decode('utf-8') for row in response.readlines()]
csvRow = csv.reader(responseLines)                                          # use the reader method to return a reader object which we iterate over lines in the given csv file

# extracting the field names 
fields = next(csvRow)

for row in csvRow:
    # if row[7] == 'CORONA,  JUAN M' or row[7] == 'HUSSAIN, TARIQ':                                                  # This is for debugging purposes
    if len(row[7].split(', ')) == 2:
        # print("The length of %s is %s" %(row[7].split(', '), len(row[7].split(', '))))                             # This is for debugging purposes
        cleansedRow = row[7].split(', ')
        # print(cleansedRow)                                                                                         # This is for debugging purposes
        cName = cleansedRow[1] + ' '+ cleansedRow[0]
        # print(cName)
        cur.execute(insertScript %(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], cName, row[8], row[9], row[10], row[11]))

    # elif len(row[7].split(', ')) == 1 and row[7] == "PATRICK J. O'BRIEN":                                                                  # This is for debugging purposes
    #     cur.execute(insertScript %(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7].replace("'",""), row[8], row[9], row[10], row[11]))
    else:
        cur.execute(insertScript %(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7].replace("'","''"), row[8], row[9], row[10], row[11]))

outPutRes = cur.execute("SELECT COUNT(*) FROM Chauffeurs;")
outPutResIObj = outPutRes.fetchall()

print("SELECT COUNT(*) FROM Chauffeurs is \n %s" %(outPutResIObj))



conn.commit()
conn.close()
