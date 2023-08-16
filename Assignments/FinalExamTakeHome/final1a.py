# Author: Ronaldlee Ejalu
# Course DSC 450
# 1a
"""
a.Use python to download tweets from the web and save to a local text file (not into a database yet, just to a text file). 
This is as simple as it sounds, all you need is a for-loop that reads lines and writes them into a file, just don’t forget to add ‘\n’ at the end so they are, in fact, on separate lines.
NOTE: Do not call read() or readlines(). 
That command will attempt to read the entire file which is too much data. Clicking on the link in the browser would cause the same prob
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

for i in range(250000):
    if i % 10000== 0: # Print a message every 500th tweet read
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
print('The number of operations per second is %s seconds' %(250000/(endTime-startTime)))