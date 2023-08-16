import urllib.request
import json
import requests
import sqlite3
import os

tweetData = "https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt"

response = requests.get(tweetData)                                              # create a response object called response, which has all the information I need
# print(type(response))                                                         # This is for debugging purposes

web = response.content.decode('utf-8')                                          # Convert bytes to strings
print(web)

# Result = web.split(' ')
# for i in web:
#     print(i)

regex4 = re.compile('"\w+":"[^"]*"')
res4 = regex4.findall(tweetSting)                                              # I get all the fields surrounded by double quotes