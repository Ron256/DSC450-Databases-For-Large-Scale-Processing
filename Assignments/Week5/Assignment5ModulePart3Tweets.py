# Author: Ronaldlee Ejalu
# Course DSC 450
# Assignment 5 Module Part 3

import urllib.request
import json
import requests
import sqlite3
import os

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/Week5')

createTbl = """
CREATE TABLE Tweets
(
    Created_at VARCHAR2(100),
    id  VARCHAR2(100),
    text VARCHAR2(300),
    source VARCHAR2(100),
    in_reply_to_user_id VARCHAR2(100),
    in_reply_to_screen_name VARCHAR2(100),
    in_reply_to_status_id VARCHAR2(100),
    retweet_count NUMBER,
    contributors VARCHAR2(100),
    CONSTRAINT Tweets_PK PRIMARY KEY(id)
);
"""

tweetData = "http://dbgroup.cdm.depaul.edu/DSC450/Assignment4.txt"

response = requests.get(tweetData)                                              # create a response object called response, which has all the information I need
# print(type(response))                                                         # This is for debugging purposes

web = response.content.decode('utf-8')                                          # Convert bytes to strings
# print(type(web))

# Since the file is one string with multiple tweets, we need to split it into a List of tweets
Result = web.split('EndOfTweet')                                                

conn = sqlite3.connect('dsc450.db')                                              # open the connection
cur  = conn.cursor()                                                             # instantiate a cursor object

# Drop the table if it exists
cur.execute("DROP TABLE IF EXISTS Tweets;")

# execute the DDL to create the Tweet table
cur.execute(createTbl)

# iterate through the list of tweets, Result
for item in Result:
    # Convert each item of the list into json 
    # tweetItems is a dictionary object
    tweetItems = json.loads(item)  

    cur.execute("INSERT INTO Tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (tweetItems["created_at"], 
                                                                            tweetItems["id_str"], 
                                                                            tweetItems["text"], 
                                                                            tweetItems["source"], 
                                                                            tweetItems["in_reply_to_user_id"], 
                                                                            tweetItems["in_reply_to_screen_name"], 
                                                                            tweetItems["in_reply_to_status_id"], 
                                                                            tweetItems["retweet_count"], 
                                                                            tweetItems["contributors"]
                                                                            )
                )

    # print(tweetItems["created_at"], tweetItems["id_str"], tweetItems["source"], tweetItems["in_reply_to_status_id"], tweetItems["in_reply_to_screen_name"], tweetItems["retweet_count"], tweetItems["contributors"])                         # This is for debugging purposes

# distinct Ids
# This is for debugging purposes
# disctintId = cur.execute("SELECT COUNT(DISTINCT id) FROM Tweets;")
# print("Distinct Ids are: %s"%(disctintId.fetchall()))

tweetItemsData = cur.execute("SELECT COUNT(*) FROM Tweets;")
tweetItemsIObj = tweetItemsData.fetchall()

print("The number of records in the tweets table are  %s." %(tweetItemsIObj))


conn.commit()
conn.close()