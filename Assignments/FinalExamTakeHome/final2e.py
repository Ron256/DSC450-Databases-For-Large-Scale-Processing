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
        dataL.append(
            (regexUserRes[0], regexTypeRes[0], str(regexCoordinatesRes).split(',')[0].replace("'",'').replace('[',''), str(regexCoordinatesRes).split(',')[1].replace("'",'').replace(']',''))
        )
# print(dataL)
# print(len(dataL))

# transform the list of tuples into a data frame.
df = pandas.DataFrame(dataL, columns=['User_Id', 'Type', 'longitude', 'latitude'])

startTime = time.time()
for i in range(100): # processing the query 100 times
# Group records by User_id, perform min on longitude and min on latitude
    resAgg = df.groupby('User_Id', as_index=False).agg({'longitude':'min', 'latitude':min})


endTime = time.time()

print('The top 20 rows are \n %s' %(resAgg.head(20)))
print('the number of records computed are %s' %(resAgg.shape[0]))
print('The processing of the minimum longitude and latitude for each user took %s seconds' %(endTime-startTime))
