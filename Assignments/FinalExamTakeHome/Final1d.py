# Author: Ronaldlee Ejalu
# Course DSC 540
# Take Home Exam
# reading a collection of tweets data from the local file system
# extending the schema by adding Geo table 
# also, added a foreign key relationship between Geo and Tweets. 
# Part 1 d
import urllib.request
import json
import re
import sqlite3
import os
import csv
import time

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')

fileName = 'C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome/OneDayOfTweets.csv'

createTbl1 = """
CREATE TABLE UserTweets 
(
    Id VARCHAR2(100),
    name VARCHAR2(100),
    screen_name VARCHAR2(15),
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
	IN_REPLY_TO_USER_ID VARCHAR2(12), 
	IN_REPLY_TO_SCREEN_NAME VARCHAR2(15), 
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


# webFD = urllib.request.urlopen(tweetdata)

def transformExtraneousValues(fileDictkey):
   
    valuestr = ''
    if fileDictkey =='null' or fileDictkey =='' or fileDictkey =='[]':
        valuestr = None
    else:
        valuestr = fileDictkey
    return valuestr
            

def extractLine():
    """Reading the file in chunks"""
    with open(fileName, 'rb') as f:
        for item in f:
            yield item

startTime = time.time()
chunkSize = 50000
generatedLines = extractLine()                              # invoke a helper extractLine
screenNameDict = {}
fileItemsL = [i for i, j in zip(generatedLines, range(chunkSize))]

newUserRows = [] # hold individual values of to-be-inserted row
newGeoRows = [] # hold individual values of to-be-inserted row
newTweetRows = [] # hold individual values of to-be-inserted row



count = 0
for i in range(50000):
    if i % 5000 == 0: # Print a message every 500th tweet read
        print ("Processed " + str(i) + " tweets")
    try:
        if fileItemsL[i]:    # check if the item is empty before hand
            # tweetLine is a byte object which needs to be decoded. 
            # the loads() function in the json object lets you convert the string into the json object which acts like a dictionary. 
            # then decode the line that come back from the web into a string. 

            fileDict = json.loads(fileItemsL[i].decode('utf-8'))    # using decode() and loads to convert each item to a dictionary

            newUserRows.append(
                (
                    transformExtraneousValues(fileDict['user']['id']), transformExtraneousValues(fileDict['user']['name']), 
                    transformExtraneousValues(fileDict['user']['screen_name']), transformExtraneousValues(fileDict['user']['description']), 
                    transformExtraneousValues(fileDict['user']['friends_count'])
                )
            )   # append the tranformed rows to the tuple then to the list
            
            geoV = fileDict['geo']
            
            NoneType=type(None)
        
            
            if geoV: # check if geoV is not null
                if (not isinstance(geoV, str) or geoV.strip()) or type(geoV) is not NoneType: # Check if the key is not None neither is it a string or blanck string
                    geoValue = fileDict['geo']['type'] + str(fileDict['geo']['coordinates'][0]) + str(fileDict['geo']['coordinates'][1])
            
                newGeoRows.append(
                    (
                        fileDict['geo']['type'] + str(fileDict['geo']['coordinates'][0]) + str(fileDict['geo']['coordinates'][1]), 
                        fileDict['geo']['type'], fileDict['geo']['coordinates'][0], fileDict['geo']['coordinates'][1])

                )

                newTweetRows.append(
                    (
                        transformExtraneousValues(fileDict['created_at']), 
                        transformExtraneousValues(fileDict['id_str']), 
                        transformExtraneousValues(fileDict['text']),
                        transformExtraneousValues(fileDict['source']),
                        transformExtraneousValues(fileDict['in_reply_to_user_id']), 
                        transformExtraneousValues(fileDict['in_reply_to_screen_name']), 
                        transformExtraneousValues(fileDict['in_reply_to_status_id']), 
                        transformExtraneousValues(fileDict['retweet_count']), 
                        transformExtraneousValues(fileDict['contributors']), 
                        transformExtraneousValues(fileDict['user']['id']), 
                        geoValue
                    )
                )
     
                # count = count + 1
            else: # for the rest of the line items where the dictionary key, 'geo' is None
                # print('No result, it is none')
                # pass
                newTweetRows.append(
                    (
                        transformExtraneousValues(fileDict['created_at']), 
                        transformExtraneousValues(fileDict['id_str']), 
                        transformExtraneousValues(fileDict['text']),
                        transformExtraneousValues(fileDict['source']),
                        transformExtraneousValues(fileDict['in_reply_to_user_id']), 
                        transformExtraneousValues(fileDict['in_reply_to_screen_name']), 
                        transformExtraneousValues(fileDict['in_reply_to_status_id']), 
                        transformExtraneousValues(fileDict['retweet_count']), 
                        transformExtraneousValues(fileDict['contributors']), 
                        transformExtraneousValues(fileDict['user']['id']), 
                        None
                    )
                )
    
    except ValueError:
        continue

# execute the bulk insert queries.
cur.executemany('INSERT OR IGNORE INTO UserTweets VALUES (?, ?, ?, ?, ?);',newUserRows)
cur.executemany('INSERT OR IGNORE INTO Geo VALUES (?, ?, ?, ?);', newGeoRows)
cur.executemany('INSERT OR IGNORE INTO Tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', newTweetRows)

            
userTweetItemsData = cur.execute('SELECT COUNT(*) FROM UserTweets;').fetchall()
tweetItemsData = cur.execute('SELECT count(*) FROM Tweets limit 10;').fetchall()
geoItemsData = cur.execute('SELECT COUNT(*) FROM Geo;').fetchall()
# this is for debugging purposes
# geoTweetsData = cur.execute('SELECT * FROM Tweets WHERE GeoId IS NOT NULL OR GeoId <> "None" Limit 10;').fetchall()


print('The number of records in the userTweets table are %s'%(userTweetItemsData))
print('The number of records in the Tweets table are %s' %(tweetItemsData))
print('The number of records in the Geo table are %s' %(geoItemsData))
# print('The Records in Tweets Object where GeoId is NOT NULL are /n %s' %(geoTweetsData))
endTime = time.time()
print('The processing of the tweets data took %s seconds' %(endTime-startTime))
print('The number of operations per second is %s seconds' %(50000/(endTime-startTime)))


conn.commit()
conn.close()