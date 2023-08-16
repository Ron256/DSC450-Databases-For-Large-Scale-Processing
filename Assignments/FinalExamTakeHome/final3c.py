# Author: Ronaldlee Ejalu
# Course DSC 540
# Final Exam
# Export the contents of the Materialized view into a csv file.
# Part 3c
import json
import sqlite3
import os
import time
import csv

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')

fileName = 'C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome/OneDayOfTweets.csv'

def writeTableRowsToFile(result, colNames):
  """Function that writes the list of tuples to a csv file"""

  # use newline='' to avoid redudant blank lines inn the file. 
  with open('tweetsCsv.csv', "w", newline='', encoding= 'utf-8') as csvf:
    csvWriter = csv.writer(csvf)
    print(colNames)
    csvWriter.writerow([colNames])
    for item in result:                               # Loop through the items of the list
      csvWriter.writerow(item)                        # write the tuples of the list to a csv file.
startTime = time.time()

sqlScipt = """
SELECT * FROM TweetsMv;
"""
conn = sqlite3.connect('dsc450.db')                                                                        # open the connection
cur = conn.cursor()                                                                                        # instantiate a cursor object

# create the table 
cur.execute(sqlScipt)
rows = [rec for rec in cur]                                 # derive a list of rows
rowL = []
colNames = ''
                                  
colNames = ','.join([col[0] for col in cur.description]) # derive a list of columns

# write the rows to the file 
writeTableRowsToFile(rows, colNames)

endTime = time.time()
print('The processing of the tweets data took %s seconds' %(endTime-startTime))

conn.close()