# Author: Ronaldlee Ejalu
# Course DSC 540
# Assignment module 7 
# reading a collection of tweets data

import urllib.request
import json
import re
import sqlite3
import os
import csv

os.chdir("C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/Week7")

tweetdata = """https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt"""

createTbl1 = """
CREATE TABLE UserTweets 
(
    Id VARCHAR2(100),
    name VARCHAR2(100),
    screen_name VARCHAR2(300),
    description VARCHAR2(500),
    friends_count NUMBER,
    CONSTRAINT UserTweets_PK Primary Key(Id)
);
"""

createTbl2 = """
CREATE TABLE Tweets 
(	CREATED_AT DATE, 
	ID VARCHAR2(100), 
	TEXT VARCHAR2(300), 
	SOURCE VARCHAR2(100), 
	IN_REPLY_TO_USER_ID VARCHAR2(100), 
	IN_REPLY_TO_SCREEN_NAME VARCHAR2(100), 
	IN_REPLY_TO_STATUS_ID VARCHAR2(100), 
	RETWEET_COUNT NUMBER, 
	CONTRIBUTORS VARCHAR2(100),
    User_Id VARCHAR2(100),
    CONSTRAINT TWEETS_FK FOREIGN KEY(User_Id) REFERENCES UserTweets(Id)
);
"""

conn = sqlite3.connect('dsc450.db')                                                                        # open the connection
cur = conn.cursor()                                                                                        # instantiate a cursor object

# Drop the tables if they exist
cur.execute("DROP TABLE IF EXISTS UserTweets;")
cur.execute("DROP TABLE IF EXISTS Tweets;")

# execute the DDL to create the corresponding tables
cur.execute(createTbl1)
cur.execute(createTbl2)

webFD = urllib.request.urlopen(tweetdata)

# read the file by using readline(), which reads only one line assuming there are multiple lines
tweetLine = webFD.readlines()

csvf = open("ErrorFile.csv", 'w', newline='') 
for i in range(0, len(tweetLine)):
# for item in tweetLine:

    # tweetLine is a byte object which needs to be decoded. 
    # the loads() function in the json object lets you convert the string into the json object which acts like a dictionary. 
    # then decode the line that come back from the web into a string. 
    try:
        tDict  = json.loads(tweetLine[i].decode('utf-8'))                                                     # then decode the line that come back from the web into a string
        cur.execute("INSERT OR IGNORE INTO UserTweets VALUES (?, ?, ?, ?, ?);", 
                                                                            (
                                                                                tDict['user']['id'], 
                                                                                tDict['user']['name'], 
                                                                                tDict['user']['screen_name'], 
                                                                                tDict['user']['description'], 
                                                                                tDict['user']['friends_count']
                                                                                )
                                                                )

        cur.execute("INSERT OR IGNORE INTO Tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", 
                                                                                        (
                                                                                            tDict["created_at"], 
                                                                                            tDict["id_str"], 
                                                                                            tDict["text"], 
                                                                                            tDict["source"], 
                                                                                            tDict["in_reply_to_user_id"], 
                                                                                            tDict["in_reply_to_screen_name"], 
                                                                                            tDict["in_reply_to_status_id"], 
                                                                                            tDict["retweet_count"], 
                                                                                            tDict["contributors"], 
                                                                                            tDict['user']['id']
                                                                                        )
                                                            )
    except ValueError:
        csvf.write(str(tweetLine[i]))                                          # write the problematic tweet to a file

userTweetItemsData = cur.execute("SELECT COUNT(*) FROM UserTweets;").fetchall()
tweetItemsData = cur.execute("SELECT COUNT(*) FROM Tweets limit 100;").fetchall()


print("The number of records in the userTweets table are %s"%(userTweetItemsData))
print("The number of records in the Tweets table are %s" %(tweetItemsData))

csvf.close()
conn.commit()
conn.close()