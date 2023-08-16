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
