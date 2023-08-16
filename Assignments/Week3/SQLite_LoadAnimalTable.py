
# Author : Ronaldlee Ejalu
# Course: DSC 450
# Assigment Module 2 Part a

def writeTableRowsToFile(result):
  """Function that writes the list of tuples to a csv file"""

  # use newline='' to avoid redudant blank lines inn the file. 
  with open("Animal.txt", "w", newline='') as csvf:
    csvWriter = csv.writer(csvf)
    csvWriter.writerow(['AID', 'AName', 'ACategory', 'TimeToFeed'])
    for item in result:                               # Loop through the items of the list
      csvWriter.writerow(item)                        # write the tuples of the list to a csv file.



def readFileRows(fileName):
    with open(fileName, 'r') as readObject:
        csvReaderObj = reader(readObject)                                   # pass the file object as an argument to the reader() method to generate the reader object, which is an iterator

        
        listOfRecords = list(csvReaderObj)                                  # generate  a list of lists by passing the reader object, csvReaderObj, as an argument to the list() method and each list represents a row of csv and each corresponding item represents a cell / column in that row. 
        # print(listOfRecords)
    
    return listOfRecords                                                    # return a list of lists object 

    

createtbl = """
CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR2(30) NOT NULL,
  ACategory VARCHAR2(18),

  TimeToFeed NUMBER(4,2),

  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);
"""

createtblb = """
CREATE TABLE Animalb
(
  AID       NUMBER(3, 0),
  AName      VARCHAR2(30) NOT NULL,
  ACategory VARCHAR2(18),

  TimeToFeed NUMBER(4,2),

  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);
"""
inserts = ["INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);", "INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);", "INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);", "INSERT INTO Animal VALUES(4, 'Grizzly bear', 'common', 3.0);", "INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.5);", "INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.75);", "INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.25);", "INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.75);", "INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.5);", "INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.25);", "INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.5);"]
# print(inserts)
import sqlite3
import os
import csv
from csv import reader
os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/Week3')            # Change the directory to point to OneDrive.
print(os.getcwd())


conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()

cursor.execute(createtbl)   # create the Animal table
for ins in inserts:         # insert the rows
    cursor.execute(ins)

conn.commit()   # finalize inserted data

result = cursor.execute('SELECT * FROM Animal');
outPut = result.fetchall()                                    # Return the list of tuples and store them into an object. 
# print(outPut)                                               # This is for debugging purposes. 
writeTableRowsToFile(outPut)                                  # helpfer function to write the list of tuples to a csv file. 



# part 2b
cursor.execute(createtblb);                                   # create a table in the sql lite database

listOfAnimalRecs = readFileRows("Animal.txt")                 # use a helper function to read the read the generated file and returns a list of list object


recValues = listOfAnimalRecs[1:]                              # lets ignore the header columns

# print("Debugging %s" %recValues)
cursor.executemany("INSERT INTO Animalb VALUES (?, ?, ?, ?);", recValues);      # using executemany to load the data into Animals table
conn.commit()

res = cursor.execute('SELECT COUNT(*) FROM Animalb');
numOfRows = res.fetchone()

print("The number of rows loaded were %s" %numOfRows)
conn.close()                                                # close the connection



