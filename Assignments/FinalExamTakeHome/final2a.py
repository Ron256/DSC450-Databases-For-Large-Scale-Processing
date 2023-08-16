# Author: Ronaldlee Ejalu
# Course DSC 540
# Final Exam 
# a SQL query that finds the smallest 
# longitude and latitude value for each user ID
# Part 2a
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
userIdRes = cur.execute(sqlScript).fetchall()
print('The results of query %s are: /n %s ' %(sqlScript, userIdRes))
print('%s rows are returned' %(len(userIdRes)))
cur.close()


