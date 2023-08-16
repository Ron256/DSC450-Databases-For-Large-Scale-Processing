# Author: Ronaldlee Ejalu
# Course DSC 540
# Assignment module 9
# Part 1 d
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
# do something 
uniqueItems = {}                                    # declare a dictionary of unique items         
count = 0
for i in range(0, len(tweetLine)):
    try:
        tDict  = json.loads(tweetLine[i].decode('utf-8'))                   # then decode the line that come back from the web into a string
        if tDict['in_reply_to_user_id']:                                    # check if the key value is not None
            if tDict['in_reply_to_user_id'] not in uniqueItems:             # check if dictionary key value is not in the declared dictionary, uniqueItems. 
                uniqueItems[tDict['in_reply_to_user_id']] = 1
                count += 1
    except ValueError:
        csvf.write(str(tweetLine[i]))                                          # write the problematic tweet to a file
endTime = time.time()                                                           #derive the end time

# dictValues = uniqueItems.values()
# print(type(dictValues))                                                       # This is for debugging purposes
print("The run time of finding unique values in the 'in_reply_to_user_id' column\n in python by reading it from a file without using SQL is %s seconds" %(str(endTime - startTime)))
# print('The number of unique values are %s' %(sum(uniqueItems.values())))                            # print the sumed value of the dictionary unique values 
# print(count)
csvf.close()
