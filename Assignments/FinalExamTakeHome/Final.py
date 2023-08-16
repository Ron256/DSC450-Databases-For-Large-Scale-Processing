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

