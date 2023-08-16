# Author: Ronaldlee Ejalu
# Course DSC 540
# Final Exam 
# using a for loop to execute 
# a SQL query that finds the smallest 
# longitude and latitude value for each user ID
# 10 times and 100 times
# and then measure the total run time
# Part 2b
import re
import sqlite3
import os
import time

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')
# connect to the database file to open a connection
conn = sqlite3.connect('dsc450.db')                                  # open the connection
cur = conn.cursor()                                                    # instantiate a cursor object
# construct a sql query and assign it to a string variable
sqlScript = """ 
SELECT Tweets.User_Id, 
MIN(Geo.longitude), 
MIN(latitude) 
FROM Tweets, Geo 
WHERE Tweets.GeoId = Geo.Id 
GROUP BY Tweets.User_Id; 
"""
startTime = time.time()
for i in range(100):
    cur.execute(sqlScript)

endTime = time.time()
print('The processing of the query 10 times takes %s seconds to run'%(endTime - startTime))
cur.close()


