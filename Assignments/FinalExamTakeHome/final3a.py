# Author: Ronaldlee Ejalu
# Course DSC 540
# Final Exam
# Using a database of 500,000 tweets
# create a new table that corresponds to the materialized view
# joining all the three tables.
# Part 3a
import sqlite3
import os
import time

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')

# tweetdata = """http://dbgroup.cdm.depaul.edu/DSC450/OneDayOfTweets.txt"""
fileName = 'C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome/OneDayOfTweets.csv'

startTime = time.time()

conn = sqlite3.connect('dsc450.db')                                                                        # open the connection
cur = conn.cursor()                                                                                        # instantiate a cursor object

sqlSciptView = """
CREATE TABLE TweetsMv AS 
SELECT Tweets.CREATED_AT, 
Tweets.ID, 
Tweets.TEXT, 
Tweets.SOURCE, 
Tweets.IN_REPLY_TO_USER_ID, 
Tweets.IN_REPLY_TO_SCREEN_NAME, 
Tweets.IN_REPLY_TO_STATUS_ID, 
Tweets.RETWEET_COUNT, 
Tweets.CONTRIBUTORS, 
Tweets.User_Id, 
Tweets.GeoId,  
UserTweets.name, 
UserTweets.screen_name, 
UserTweets.description, 
UserTweets.friends_count, 
Geo.Type, 
Geo.longitude, 
Geo.latitude
FROM Tweets 
    LEFT JOIN UserTweets 
        ON Tweets.User_Id = UserTweets.Id
    LEFT JOIN Geo
        ON Geo.Id = Tweets.GeoId;
"""

# Drop the tables if it exists
cur.execute('DROP TABLE IF EXISTS TweetsMv;')

# create the table 
cur.execute(sqlSciptView)

mvRes = cur.execute('SELECT * FROM TweetsMv limit 10;').fetchall()

print('The first top ten records of the view are: \n %s'%(mvRes))

# webFD = urllib.request.urlopen(tweetdata)

endTime = time.time()
print('The processing of the tweets data took %s seconds' %(endTime-startTime))

conn.commit()
conn.close()