# Author: Ronaldlee Ejalu
# Course DSC 540
# Assignment module 9
# reading a collection of tweets data
# extending the schema by adding Geo table 
# also, added a foreign key relationship between Geo and Tweets. 
# Part 1 c

import urllib.request
import json
import re
import sqlite3
import os
import csv
import time


os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/Week9')

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
    GeoId VARCHAR2(1000),
    CONSTRAINT TWEETS_FK1 FOREIGN KEY(User_Id) REFERENCES UserTweets(Id),
    CONSTRAINT TWEETS_FK2 FOREIGN KEY(GeoId) REFERENCES Geo(Id)
);
"""

createTbl3 = """
CREATE TABLE Geo
(
    Id VARCHAR2(1000),
    Type VARCHAR2(50),
    longitude NUMBER,
    latitude NUMBER,
    CONSTRAINT Geo_PK Primary Key (Id)
); 
"""

conn = sqlite3.connect('dsc450.db')                                                                        # open the connection
cur = conn.cursor()                                                                                        # instantiate a cursor object

# Drop the tables if they exist
cur.execute('DROP TABLE IF EXISTS UserTweets;')
cur.execute('DROP TABLE IF EXISTS Tweets;')
cur.execute('DROP TABLE IF EXISTS Geo;')

# execute the DDL to create the corresponding tables
cur.execute(createTbl1)
cur.execute(createTbl3)
cur.execute(createTbl2)


webFD = urllib.request.urlopen(tweetdata)

# read the file by using readlines(), which reads only one line assuming there are multiple lines
tweetLine = webFD.readlines()

csvf = open('ErrorFile.csv', 'w', newline='') 
count = 0
for i in range(0, len(tweetLine)):
    try:
        if tweetLine[i]:    # check if the item is empty before hand
            # tweetLine is a byte object which needs to be decoded. 
            # the loads() function in the json object lets you convert the string into the json object which acts like a dictionary. 
            # then decode the line that come back from the web into a string. 

            tDict  = json.loads(tweetLine[i].decode('utf-8'))                   # then decode the line that come back from the web into a string
            # print(type(tDict))

            cur.execute('INSERT OR IGNORE INTO UserTweets VALUES (?, ?, ?, ?, ?);', 
                                                                            (
                                                                                tDict['user']['id'], 
                                                                                tDict['user']['name'], 
                                                                                tDict['user']['screen_name'], 
                                                                                tDict['user']['description'], 
                                                                                tDict['user']['friends_count']
                                                                                )
                                                                )
            

            geoV = tDict['geo']
            if geoV is not None and (not isinstance(geoV, str) or geoV.strip()): # Check if the key is not None neither is it a string or blanck string
                geoValue = tDict['geo']['type'] + str(tDict['geo']['coordinates'][0]) + str(tDict['geo']['coordinates'][1])

                cur.execute('INSERT OR IGNORE INTO Geo VALUES (?, ?, ?, ?);', 
                                                        (
                                                            geoValue, 
                                                            tDict['geo']['type'], 
                                                            tDict['geo']['coordinates'][0], 
                                                            tDict['geo']['coordinates'][1])
                                                            )

                cur.execute('INSERT OR IGNORE INTO Tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', 
                                                                                        (
                                                                                            tDict['created_at'], 
                                                                                            tDict['id_str'], 
                                                                                            tDict['text'], 
                                                                                            tDict['source'], 
                                                                                            tDict['in_reply_to_user_id'], 
                                                                                            tDict['in_reply_to_screen_name'], 
                                                                                            tDict['in_reply_to_status_id'], 
                                                                                            tDict['retweet_count'], 
                                                                                            tDict['contributors'], 
                                                                                            tDict['user']['id'],
                                                                                            geoValue
                                                                                        )
                                                            )

                
                count = count + 1
            else:     # for the rest of the line items where the dictionary key, 'geo' is None
                cur.execute('INSERT OR IGNORE INTO Tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', 
                                                                                        (
                                                                                            tDict['created_at'], 
                                                                                            tDict['id_str'], 
                                                                                            tDict['text'], 
                                                                                            tDict['source'], 
                                                                                            tDict['in_reply_to_user_id'], 
                                                                                            tDict['in_reply_to_screen_name'], 
                                                                                            tDict['in_reply_to_status_id'], 
                                                                                            tDict['retweet_count'], 
                                                                                            tDict['contributors'], 
                                                                                            tDict['user']['id'],
                                                                                            None
                                                                                        )
                                                            )

    except ValueError:
        csvf.write(str(tweetLine[i]))                                          # write the problematic tweet to a file
    

userTweetItemsData = cur.execute('SELECT COUNT(*) FROM UserTweets;').fetchall()
tweetItemsData = cur.execute('SELECT count(*) FROM Tweets limit 10;').fetchall()
geoItemsData = cur.execute('SELECT COUNT(*) FROM Geo;').fetchall()
# this is for debugging purposes
# geoTweetsData = cur.execute('SELECT * FROM Tweets WHERE GeoId IS NOT NULL OR GeoId <> "None" Limit 10;').fetchall()


print('The number of records in the userTweets table are %s'%(userTweetItemsData))
print('The number of records in the Tweets table are %s' %(tweetItemsData))
print('The number of records in the Geo table are %s' %(geoItemsData))
# print('The Records in Tweets Object where GeoId is NOT NULL are /n %s' %(geoTweetsData))

# Part 1a
start = time.time()
# do something
determinedTweets = cur.execute("SELECT * FROM Tweets WHERE Id LIKE '%888%' OR Id LIKE '%77%';").fetchall()
end = time.time()
str(end - start) 

# print("The run time of the query which finds tweets where id_str contains '888' or '77' anywhere in the column is %s seconds" %(str(end - start)))

# Part 1C
startTime = time.time()             # derive the start time
# do something
# uniqueInReplyUserIds = cur.execute("SELECT COUNT(DISTINCT IN_REPLY_TO_USER_ID) FROM Tweets;").fetchall()
# endTime = time.time()               # derive the end time. 
# print("The runtime of finding unique values in the 'in_reply_to_user_id' column using SQL is %s seconds" %(str(endTime - startTime)))
# print('The number of unique in_reply_to_user_id column values are %s' %(uniqueInReplyUserIds))

csvf.close()
conn.commit()
conn.close()