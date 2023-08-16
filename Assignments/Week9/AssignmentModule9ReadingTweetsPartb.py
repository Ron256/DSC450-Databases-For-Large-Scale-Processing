# Author: Ronaldlee Ejalu
# Course DSC 540
# Assignment module 9
# Part 1 b
import urllib.request
import json
import os
import csv
import time
os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/Week9')

tweetdata = """https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt"""

webFD = urllib.request.urlopen(tweetdata)

# read the file by using readlines(), which reads only one line assuming there are multiple lines
tweetLine = webFD.readlines()
csvf = open('ErrorFile.csv', 'w', newline='') 
startTime = time.time()                             # get the start time
filteredItems = []

for i in range(0, len(tweetLine)):
    try:
        tDict  = json.loads(tweetLine[i].decode('utf-8'))                   # then decode the line that come back from the web into a string
        if '888' in tDict['id_str'] or '77' in tDict['id_str']:             # search for the id_str dictionary value where it either contains '888' or '77'
            # derive a tuple of items 
            searchedItems = (
                                tDict['created_at'], 
                                tDict['id_str'], 
                                tDict['text'], 
                                tDict['source'], 
                                tDict['in_reply_to_user_id'], 
                                tDict['in_reply_to_screen_name'], 
                                tDict['in_reply_to_status_id'], 
                                tDict['retweet_count'], 
                                tDict['contributors'], 
                                tDict['user']['id']
                            )
            filteredItems.append(searchedItems)                                 # add the defined tuple of items to the list.
    except ValueError:
        csvf.write(str(tweetLine[i]))                                          # write the problematic tweet to a file
endTime = time.time()                                                           #derive the end time

print("The run time of the process which finds tweets where id_str contains '888' or '77' \nany where in the column using python without using SQL is %s seconds" %(str(endTime - startTime)))
csvf.close()
