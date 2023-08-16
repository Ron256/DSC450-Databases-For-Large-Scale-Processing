# Author: Ronaldlee Ejalu
# Course DSC 540
# Final Exam
# Export the contents of the Materialized view into a json structure.
# Part 3b
import json
import sqlite3
import os
import time

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')

# tweetdata = """http://dbgroup.cdm.depaul.edu/DSC450/OneDayOfTweets.txt"""
fileName = 'C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome/OneDayOfTweets.csv'

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
tableColumns = [col[0] for col in cur.description]                                   # derive a list of columns

for tablerow in rows:
    tDict = {}
    for tCol, tRow in zip(tableColumns, tablerow):  # using zip() which an iterator to conserve memory. 
        tDict[tCol] = tRow
        rowL.append(tDict)
# print(rowL)
# jsonStr = json.dumps(rowL)      # derive a string representation of your table schema as a json object
# write the json object to a file
with open('tableJson.json', 'w') as outfile:
    json.dump(rowL, outfile)

endTime = time.time()
print('The processing of the tweets data took %s seconds' %(endTime-startTime))

conn.close()