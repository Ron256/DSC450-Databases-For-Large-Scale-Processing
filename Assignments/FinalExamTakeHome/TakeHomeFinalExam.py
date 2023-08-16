# Author: Ronaldlee Ejalu
# Course DSC 450
# 1a
"""
a.Use python to download tweets from the web and save to a local text file (not into a database yet, just to a text file). 
This is as simple as it sounds, all you need is a for-loop that reads lines and writes them into a file, just don’t forget to add ‘\n’ at the end so they are, in fact, on separate lines.
NOTE: Do not call read() or readlines(). 
That command will attempt to read the entire file which is too much data. Clicking on the link in the browser would cause the same prob
"""

""" 
import urllib.request
import json
import os
import csv
import time

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')

tweetdata = """http://dbgroup.cdm.depaul.edu/DSC450/OneDayOfTweets.txt"""
startTime = time.time()                                                     # start time of processing the file in web

webFD = urllib.request.urlopen(tweetdata)
# csvf = open('OneDayOfTweets.csv', 'w', newline = '\n', encoding = 'utf-8')
csvf = open('OneDayOfTweets.csv', 'wb')

for i in range(500000):
    if i % 5000 == 0: # Print a message every 500th tweet read
        print ("Processed " + str(i) + " tweets")
    try:
        itemResponse = webFD.readline()                                     # read one line at a time
        # strItemResponse = itemResponse.decode('utf-8')                      # decode the line that comes back from the web into a string.
        csvf.write(itemResponse)
    
    except Exception:
        continue
    
csvf.close()                                                                 # close the file
# csve.close()                                                                 # close the error file
endTime = time.time()                                                        # end time of processing of writing the tweets data to a file. 
print('The processing of the tweets data took %s seconds' %(endTime-startTime))
print('The number of operations per second is %s seconds' %(500000/(endTime-startTime)))
# end 1a

# Author Ronaldlee Ejalu
# Course DSC 450
# 1b
import pandas as pd
import os
import csv
import time
import json
# 1b

fileName = 'C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome/OneDayOfTweets.csv'

def extractLine():
    """Reading the file in chunks"""
    with open(fileName, 'rb') as f:
        for item in f:
            yield item

startTime = time.time()
chunkSize = 500000
generatedLines = extractLine()                              # invoke a helper extractLine
screenNameDict = {}
chunk = [i for i, j in zip(generatedLines, range(chunkSize))]

inReplytoUserIdL = [] # hold in_reply_to_user_id id values

inReplyToScreenNameL = [] # hold in_reply_to_screen_name values


for i in range(500000):
    if i % 5000 == 0: # Print a message every 500th tweet read
        print ('Processed ' + str(i) + ' tweets')
    fileDict = json.loads(chunk[i].decode('utf-8')) # using decode() and loads to convert each item to a dictionary
    if fileDict['user']['screen_name'] not in screenNameDict.values():
        screenNameDict[i] = fileDict['user']['screen_name']

    if fileDict['in_reply_to_user_id'] not in inReplytoUserIdL:
        inReplytoUserIdL.append(fileDict['in_reply_to_user_id'])

    if fileDict['in_reply_to_screen_name'] not in inReplyToScreenNameL:
        inReplyToScreenNameL.append(fileDict['in_reply_to_screen_name'])

# print(screenNameDict)       # for debugging purposes

screenNameDf = pd.DataFrame(screenNameDict.values(), columns=['ScreenName'])                    # generate the ScreenName DataFrame
inReplytoUserIdDf = pd.DataFrame(inReplytoUserIdL, columns=['in_reply_to_user_id'])              # generate the inReplytoUserIdDf
inReplyToScreenNameDf = pd.DataFrame(inReplyToScreenNameL, columns=['in_reply_to_screen_name'])

# print(screenNameDf.head(10))   
print('The length of the longest string in the file for the in_reply_to_user_id column is %s'%(inReplytoUserIdDf.in_reply_to_user_id.fillna(method='ffill').astype(str).str.len().max()))                        # use pandas.fillna() yo get rid of the NaNs and before deriving the min and max lengths trasnform each value into a string
print('The length of the longest string in the file for the in_reply_to_screen_name column is %s'%(inReplyToScreenNameDf.in_reply_to_screen_name.fillna(method='ffill').astype(str).str.len().max()))
print('The length of the longest string in the file for the ScreenName column is %s'%(screenNameDf.ScreenName.fillna(method='ffill').astype(str).str.len().max())) 
endTime = time.time()
print('The processing of the tweets data took %s seconds' %(endTime-startTime))

#end 1b

# Author: Ronaldlee Ejalu
# Course DSC 540
# Final Take home exam
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

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')

tweetdata = """http://dbgroup.cdm.depaul.edu/DSC450/OneDayOfTweets.txt"""


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


def transformExtraneousValues(tDictkey):
   
    valuestr = ''
    if tDictkey =='null' or tDictkey =='' or tDictkey =='[]':
        valuestr = None
    else:
        valuestr = tDictkey
    return valuestr
            
startTime = time.time()
webFD = urllib.request.urlopen(tweetdata)

newUserRows = [] # hold individual values of to-be-inserted row
newGeoRows = [] # hold individual values of to-be-inserted row
newTweetRows = [] # hold individual values of to-be-inserted row

count = 0
for i in range(50000):
    if i % 5000 == 0: # Print a message every 500th tweet read
        print ("Processed " + str(i) + " tweets")
    tweetLine = webFD.readline() # read the file by using readline(), which reads only one line assuming there are multiple lines   
    try:
        if tweetLine:    # check if the item is empty before hand
            # tweetLine is a byte object which needs to be decoded. 
            # the loads() function in the json object lets you convert the string into the json object which acts like a dictionary. 
            # then decode the line that come back from the web into a string. 

            tDict = json.loads(tweetLine.decode('utf-8'))    # using decode() and loads to convert each item to a dictionary

            newUserRows.append(
                (
                    transformExtraneousValues(tDict['user']['id']), transformExtraneousValues(tDict['user']['name']), 
                    transformExtraneousValues(tDict['user']['screen_name']), transformExtraneousValues(tDict['user']['description']), 
                    transformExtraneousValues(tDict['user']['friends_count'])
                )
            )   # append the tranformed rows to the tuple then to the list
            
            geoV = tDict['geo']
            
            NoneType=type(None)
        
            
            if geoV: # check if geoV is not null
                if (not isinstance(geoV, str) or geoV.strip()) or type(geoV) is not NoneType: # Check if the key is not None neither is it a string or blanck string
                    geoValue = tDict['geo']['type'] + str(tDict['geo']['coordinates'][0]) + str(tDict['geo']['coordinates'][1])
            
                newGeoRows.append(
                    (
                        tDict['geo']['type'] + str(tDict['geo']['coordinates'][0]) + str(tDict['geo']['coordinates'][1]), 
                        tDict['geo']['type'], tDict['geo']['coordinates'][0], tDict['geo']['coordinates'][1])

                )

                newTweetRows.append(
                    (
                        transformExtraneousValues(tDict['created_at']), 
                        transformExtraneousValues(tDict['id_str']), 
                        transformExtraneousValues(tDict['text']),
                        transformExtraneousValues(tDict['source']),
                        transformExtraneousValues(tDict['in_reply_to_user_id']), 
                        transformExtraneousValues(tDict['in_reply_to_screen_name']), 
                        transformExtraneousValues(tDict['in_reply_to_status_id']), 
                        transformExtraneousValues(tDict['retweet_count']), 
                        transformExtraneousValues(tDict['contributors']), 
                        transformExtraneousValues(tDict['user']['id']), 
                        geoValue
                    )
                )
     
                # count = count + 1
            else: # for the rest of the line items where the dictionary key, 'geo' is None
                # print('No result, it is none')
                # pass
                newTweetRows.append(
                    (
                        transformExtraneousValues(tDict['created_at']), 
                        transformExtraneousValues(tDict['id_str']), 
                        transformExtraneousValues(tDict['text']),
                        transformExtraneousValues(tDict['source']),
                        transformExtraneousValues(tDict['in_reply_to_user_id']), 
                        transformExtraneousValues(tDict['in_reply_to_screen_name']), 
                        transformExtraneousValues(tDict['in_reply_to_status_id']), 
                        transformExtraneousValues(tDict['retweet_count']), 
                        transformExtraneousValues(tDict['contributors']), 
                        transformExtraneousValues(tDict['user']['id']), 
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
print('The number of operations per second is %s seconds' %(500000/(endTime-startTime)))


conn.commit()
conn.close()
# end 1c

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
# end 1d

# Author: Ronaldlee Ejalu
# Course DSC 540
# Take home exam
# reading a collection of tweets data from a file
# and using a batch size of 2000 to perform bulk inserts 
# into the sqlite database
# extending the schema by adding Geo table 
# also, added a foreign key relationship between Geo and Tweets. 
# Part 1 e

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


def transformExtraneousValues(fileDictkey):
    """A function that takes a dictionary key and 
    checks if the value is null, an empty string or [] 
    and it replaces it with None otherwise it assigns 
    the actual value to a variable which is returned
    """
   
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
generatedLines = extractLine()                              # invoke a helper extractLine to read  the file in chunks
screenNameDict = {}
fileItemsL = [i for i, j in zip(generatedLines, range(chunkSize))]

newUserRows = [] # hold individual values of to-be-inserted row
newGeoRows = [] # hold individual values of to-be-inserted row
newTweetRows = [] # hold individual values of to-be-inserted row

batchUserRows = [] # hold the batch size of rows to be inserted
batchGeoRows = []
batchTweetRows = []

tweetCounter = 0
geoCounter = 0
userCounter = 0
for i in range(50000):
    if i % 2000 == 0: # Print a message every 500th tweet read
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
            userCounter += 1
            
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

                geoCounter += 1 

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
                tweetCounter += 1
     
                
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
                tweetCounter += 1
    
    except ValueError:
        continue

    # Using a batch size of 2000 to peform bulk inserts 
    if userCounter > 2000:
        cur.executemany('INSERT OR IGNORE INTO UserTweets VALUES (?, ?, ?, ?, ?);',newUserRows)
        # rows = len(newUserRows)        # enable this for debugging purposes
        newUserRows = []      # cleaning up the list
        userCounter = 0         # reset the counter
        # print('Inserted %s rows' %(rows))
    
    if geoCounter > 2000:
        cur.executemany('INSERT OR IGNORE INTO Geo VALUES (?, ?, ?, ?);', newGeoRows)
        newGeoRows = []     # cleaning up the list before the next tuples of data are added
        geoCounter = 0

    if tweetCounter > 2000:
        cur.executemany('INSERT OR IGNORE INTO Tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', newTweetRows)
        newTweetRows = []
        tweetCounter = 0
# execute the remaining data the list when the batch size is less than 2000
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
# end 1e


# Ronaldlee Ejalu
# DSC 450
# Final Take home exam
# plotting the resulting runtime (# of tweets versus run times)
# using matplotlib for 1-a, 1-c, 1-d, and 1-e
# 1f
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')

# deriving the data structures for the runtimes of the number of tweets for the 
# questions 1a, 1c, 1d, and 1e
dataForA = [(500, 1016.9364602565765), (50, 288.94251561164856)]
dataForC = [(500, 3012.9960594177246), (50, 279.7146816253662)]
dataForD = [(500, 172.24891209602356), (50, 14.039840698242188)]
dataForE = [(500, 173.3715558052063), (50, 8.637104034423828)]

# derive the different data frames
dfRunTimeA = pd.DataFrame(dataForA, columns=['NumberOfTweets', 'RunTimeinSecs'])
dfRunTimeC = pd.DataFrame(dataForC, columns=['NumberOfTweets', 'RunTimeinSecs'])
dfRunTimeD = pd.DataFrame(dataForD, columns=['NumberOfTweets', 'RunTimeinSecs'])
dfRunTimeE = pd.DataFrame(dataForE, columns=['NumberOfTweets', 'RunTimeinSecs'])
print(dfRunTimeE)

fig = plt.figure()                                          # create a blank figure

# add a varierty of sub plots to it,
# the first two parameters describe the size of the grid
# that corresponds to the sub figures being added.
# 2 by 2 means we have a grid of four different sub plots
# and we are going to use that to compare and contrast the styles of the different figures. 
# the last parameter refers to which of the sub plots we are adding to.
# so one refers to the top left of the first out of the four subplots in the figure

sp = fig.add_subplot(2, 2, 1)                                    # Add a grid of 4 subplots
fig.set_size_inches(15, 15)                                      # set the figure size in inches. 

sp.plot(dfRunTimeA['NumberOfTweets'], dfRunTimeA['RunTimeinSecs'], '--')
sp.set_ylim(bottom=0)
sp.set_title("# of Tweets versus runtime for 1a", fontsize = 12)
sp.set_xlabel('NumberOfTweets (in thousands)', fontsize = 12)
sp.set_ylabel('Run Time in Seconds', fontsize = 12)


# creating a nother sub plot and we are using a 2 by 2 grid.
# in this case we are adding the secondor  top-right subplot to the figure 
# you can use different grading within the same figure but that does potentially 
# create overlay which you may or may not want to have in practice. 
# just note that is it possible but we will keep consistent grading into two-by-two
sp2 = fig.add_subplot(2, 2, 2) # so this addes the second sub plot to the top right
sp2.plot(dfRunTimeC['NumberOfTweets'], dfRunTimeC['RunTimeinSecs'], '-')
sp2.set_ylim(bottom=0)
sp2.set_title("# of Tweets versus runtime for 1c", fontsize = 12)                               # add the title to the plot                         
sp2.set_xlabel('NumberOfTweets (in thousands)', fontsize = 12)                                  # adding the x-axis label                     
sp2.set_ylabel('Run Time in Seconds', fontsize = 12)                                            # adding y-axis label

# next we add a third subplot and we are adding in the botton left, through the subplot
sp3 = fig.add_subplot(2, 2, 3) 
sp3.plot(dfRunTimeD['NumberOfTweets'], dfRunTimeD['RunTimeinSecs'],'-.') 
sp3.set_ylim(bottom=0)
sp3.set_title("# of Tweets versus runtime for 1d", fontsize = 12)                               # add the title to the plot                         
sp3.set_xlabel('NumberOfTweets (in thousands)', fontsize = 12)                                  # adding the x-axis label                     
sp3.set_ylabel('Run Time in Seconds', fontsize = 12)                                            # adding y-axis label
# sp3.set_ylim([15, 180])

# lets continue with fourth subplot
# Again, two by two adding to the fourth location over here
sp4 = fig.add_subplot(2, 2, 4)
sp4.plot(dfRunTimeE['NumberOfTweets'], dfRunTimeE['RunTimeinSecs']) 
sp4.set_ylim(bottom=0)
sp4.set_title("# of Tweets versus runtime for 1e", fontsize = 12)                               # add the title to the plot                         
sp4.set_xlabel('NumberOfTweets (in thousands)', fontsize = 12)                                  # adding the x-axis label                     
sp4.set_ylabel('Run Time in Seconds', fontsize = 12)                                            # adding y-axis label
#fig
fig.savefig('1e.pdf', bbox_inches='tight')                                  # save the file in pdf
# end 1f

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
# end 2a

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
for i in range(100): # executing the query 100 times
    cur.execute(sqlScript)

endTime = time.time()
print('The processing of the query 10 times takes %s seconds to run'%(endTime - startTime))
cur.close()

# end 2b

# Author: Ronaldlee Ejalu
# Course DSC 540
# Final Exam 
# Rewriting the equivalance of python logic finds the smallest 
# longitude and latitude value for each user ID
# without using SQL
# Part 2c

import urllib.request
import json
import re
import sqlite3
import os
import csv
import time
import pandas as pd

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')

fileName = 'C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome/OneDayOfTweets.csv'

def transformExtraneousValues(fileDictkey):
    """A function that takes a dictionary key and 
    checks if the value is null, an empty string or [] 
    and it replaces it with None otherwise it assigns 
    the actual value to a variable which is returned
    """
   
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
chunkSize = 500000
generatedLines = extractLine()                              # invoke a helper extractLine to read  the file in chunks
screenNameDict = {}
fileItemsL = [i for i, j in zip(generatedLines, range(chunkSize))]

newGeoRows = [] # hold individual values of to-be-inserted row
newTweetRows = [] # hold individual values of to-be-inserted row


tweetCounter = 0
geoCounter = 0
for i in range(500000):
    if i % 250000 == 0: # Print a message every 500th tweet read
        print ("Processed " + str(i) + " tweets")
    try:
        if fileItemsL[i]:    # check if the item is empty before hand
            # tweetLine is a byte object which needs to be decoded. 
            # the loads() function in the json object lets you convert the string into the json object which acts like a dictionary. 
            # then decode the line that come back from the web into a string. 

            fileDict = json.loads(fileItemsL[i].decode('utf-8'))    # using decode() and loads to convert each item to a dictionary
            

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

                geoCounter += 1 

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
                tweetCounter += 1
     
                
            else: # for the rest of the line items where the dictionary key, 'geo' is None
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
                tweetCounter += 1
    
    except ValueError:
        continue

# derive the tweet and geo data frames
tweetDF = pd.DataFrame(newTweetRows, columns=['CREATED_AT','ID','TEXT','SOURCE','IN_REPLY_TO_USER_ID',
                                                'IN_REPLY_TO_SCREEN_NAME','IN_REPLY_TO_STATUS_ID',
                                                'RETWEET_COUNT','CONTRIBUTORS','User_Id','GeoId'])
# print(tweetDF.head(10))
geoDF = pd.DataFrame(newGeoRows, columns=['Id','Type','longitude','latitude'])

# print(geoDF.head(10))

# joining the two data sets
joinedDF = pd.concat([tweetDF, geoDF], axis=1, join="inner")

# data columns description
# print(joinedDF.describe())
# print(joinedDF.shape[0])
# perform multiple aggregations

# Group records by User_id, perform min on longitude and min on latitude
resAgg = joinedDF.groupby('User_Id', as_index=False).agg({'longitude':'min', 'latitude':min})
print('The top 20 rows are /n %s' %(resAgg.head(20)))
print('the number of records computed are %s' %(resAgg.shape[0]))
endTime = time.time()

print('The processing of the tweets data took %s seconds' %(endTime-startTime))
print('The number of operations per second is %s seconds' %(500000/(endTime-startTime)))

# end 2c

# Author: Ronaldlee Ejalu
# Course DSC 540
# Final Exam 
# Rewriting the equivalance of python logic finds the smallest 
# longitude and latitude value for each user ID
# without using SQL
# Part 2d

import os
import csv
import time
import pandas as pd

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')

fileName = 'C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome/OneDayOfTweets.csv'

def transformExtraneousValues(fileDictkey):
    """A function that takes a dictionary key and 
    checks if the value is null, an empty string or [] 
    and it replaces it with None otherwise it assigns 
    the actual value to a variable which is returned
    """
   
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

chunkSize = 500000
generatedLines = extractLine()                              # invoke a helper extractLine to read  the file in chunks
screenNameDict = {}
fileItemsL = [i for i, j in zip(generatedLines, range(chunkSize))]

newGeoRows = [] # hold individual values of to-be-inserted row
newTweetRows = [] # hold individual values of to-be-inserted row


tweetCounter = 0
geoCounter = 0
for i in range(500000):
    if i % 250000 == 0: # Print a message every 500th tweet read
        print ("Processed " + str(i) + " tweets")
    try:
        if fileItemsL[i]:    # check if the item is empty before hand
            # tweetLine is a byte object which needs to be decoded. 
            # the loads() function in the json object lets you convert the string into the json object which acts like a dictionary. 
            # then decode the line that come back from the web into a string. 

            fileDict = json.loads(fileItemsL[i].decode('utf-8'))    # using decode() and loads to convert each item to a dictionary
            

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

                geoCounter += 1 

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
                tweetCounter += 1
     
                
            else: # for the rest of the line items where the dictionary key, 'geo' is None
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
                tweetCounter += 1
    
    except ValueError:
        continue

# derive the tweet and geo data frames
tweetDF = pd.DataFrame(newTweetRows, columns=['CREATED_AT','ID','TEXT','SOURCE','IN_REPLY_TO_USER_ID',
                                                'IN_REPLY_TO_SCREEN_NAME','IN_REPLY_TO_STATUS_ID',
                                                'RETWEET_COUNT','CONTRIBUTORS','User_Id','GeoId'])
# print(tweetDF.head(10))
geoDF = pd.DataFrame(newGeoRows, columns=['Id','Type','longitude','latitude'])

# print(geoDF.head(10))

# joining the two data sets
joinedDF = pd.concat([tweetDF, geoDF], axis=1, join="inner")

# data columns description
# print(joinedDF.describe())
# print(joinedDF.shape[0])
# perform multiple aggregations
startTime = time.time()
# Group records by User_id, perform the minimum on longitude and minimum on latitude
for i in range(100): # executing the query 100 times
    resAgg = joinedDF.groupby('User_Id', as_index=False).agg({'longitude':'min', 'latitude':min})
    # print('The top 20 rows are /n %s' %(resAgg.head(20)))
    # print('the number of records computed are %s' %(resAgg.shape[0]))
endTime = time.time()

print('The processing of the tweets data 10 times took %s seconds' %(endTime-startTime))

# end 2d

# Author: Ronaldlee Ejalu
# Course DSC 540
# Final Exam 
# Rewriting the equivalance of python logic finds the smallest 
# longitude and latitude value for each user ID
# without using SQL
# Part 2e

import os
import csv
import time
import re

import pandas

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')

fileName = 'C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome/OneDayOfTweets.csv'


def transformExtraneousValues(fileDictkey):
    """A function that takes a dictionary key and 
    checks if the value is null, an empty string or [] 
    and it replaces it with None otherwise it assigns 
    the actual value to a variable which is returned
    """
   
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

chunkSize = 500000
generatedLines = extractLine()                              # invoke a helper extractLine to read  the file in chunks
screenNameDict = {}
fileItemsL = [i for i, j in zip(generatedLines, range(chunkSize))]
dataL = []
for i in range(500000):
    regexUser = re.compile('"user":{"id":(\d+)')
    regexUserRes = regexUser.findall(fileItemsL[i].decode())
    # print(regexUserRes[0])                              # print the user Id object

    regexGeo = re.compile('"geo":\{(.*?)\}\,')
    regexGeoRes = regexGeo.findall(fileItemsL[i].decode())                       # derive the geo object

    regexType = re.compile('type\":"(.*?)\","')
    regexTypeRes = regexType.findall(str(regexGeoRes))      # pass the converted list of the geo object as parameter to extract the type value
    # if len(regexTypeRes) == 0:
    #     continue
    # # else:
    # #     print(regexTypeRes)

    regexCoordinates = re.compile('"coordinates\":\[(.*?)\]') # re.compile('coordinates\":\[(\d+),(\d+)\]')
    regexCoordinatesRes = regexCoordinates.findall(str(regexGeoRes))
    if len(regexCoordinatesRes) == 0:
        continue
    else:
        # print(regexUserRes[0])                              # print the user Id object
        # print(str(regexCoordinatesRes))
        # print(regexTypeRes)
        dataL.append((regexUserRes[0], regexTypeRes[0], str(regexCoordinatesRes).split(',')[0].replace("'",'').replace('[',''), str(regexCoordinatesRes).split(',')[1].replace("'",'').replace(']','')))
# print(dataL)
# print(len(dataL))

# transform the list of tuples into a data frame.
df = pandas.DataFrame(dataL, columns=['User_Id', 'Type', 'longitude', 'latitude'])

startTime = time.time()
for i in range(100): # processing the query 100 times
# Group records by User_id, perform min on longitude and min on latitude
    resAgg = df.groupby('User_Id', as_index=False).agg({'longitude':'min', 'latitude':min})


endTime = time.time()

print('The top 20 rows are /n %s' %(resAgg.head(20)))
print('the number of records computed are %s' %(resAgg.shape[0]))
print('The processing of the minimum longitude and latitude for each user took %s seconds' %(endTime-startTime))

# end 2e

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

# end 3a

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

# end 3b

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
# end 3c
"""


