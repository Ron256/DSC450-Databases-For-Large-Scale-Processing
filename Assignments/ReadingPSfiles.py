"""
Author: Ronaldlee Ejalu
Goal: reading Pathology Staging data from Json files
"""

import json
import os

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/testFiles')

with open('JSONLog 2018-05-01 213110033.json', 'rb') as file:
    data = json.load(file)
print('*'*20)
# print(type(data['dataset']['data']))
# print(len(data['dataset']['data'])-39)
for i in range(len(data['dataset']['data'])-38):
    # print(type(i))
    # print(type(data['dataset']['data'][i]))
    print(data['dataset']['data'][i]['question']['label'])
    print(data['dataset']['data'][i]['question']['type'])
    print(data['dataset']['data'][i]['question']['ckey'])
    print(data['dataset']['data'][i]['question']['itemType'])
    print(data['dataset']['data'][i]['question']['title'])
    print(type(data['dataset']['data'][i]['question']['answer']['items']))
    for i in range(len(data['dataset']['data'][i]['question']['answer']['items'])):
        print(data['dataset']['data'][i]['question']['answer']['items'][i]['value'])
        print(data['dataset']['data'][i]['question']['answer']['items'][i]['TextValue'])
        print(data['dataset']['data'][i]['question']['answer']['items'][i]['xsType'])
        print(data['dataset']['data'][i]['question']['answer']['items'][i]['itemType'])
        print(data['dataset']['data'][i]['question']['answer']['items'][i]['ckey'])
        print(data['dataset']['data'][i]['question']['answer']['items'][i]['title'])
    print('*****'*20)