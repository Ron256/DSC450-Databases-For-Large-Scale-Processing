# import numpy as np
# data = np.random.randn(2,3)

# print(data * 10)
# print(data.shape)
# print(data.dtype)

# data1 = [6, 7.5, 8, 0, 1]
# arr1 = np.array(data1)
# print(arr1.shape)

# data2 = [[1,2,3,4],[5,6,7,8]]
# arra2 = np.array(data2)
# print(arra2.shape)

# y = np.zeros((3, 6))
# print(y)

# x = np.empty((2, 3, 2))
# print(x)
# y = list(np.random.randint(3, 8, 10))
# print(y)
# int_array = np.arange(10)
# print(int_array)

# calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
# int_array = int_array.astype(calibers.dtype)
# print(int_array)

# empty_uint32 = np.empty(8, dtype='u4')
# print(empty_uint32)

# arr = np.array([[1., 2., 3.], [4., 5., 6.]])
# print(arr)
# print(arr * arr)

# arr2 = np.array([[0., 4.0, 1.0], [7., 2., 12.]])
# print(arr2)

# print(arr2 > arr)

# arr = np.arange(10)
# print(arr)
# arr[5:8] = 12
# arr_slice = arr[5:8]
# print(arr_slice)

# print("**********")
# arr_slice[1] = 12345
# print(arr)

# print("***************")
# arr_slice[:] = 64
# print(arr)

# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]])
# print(arr2d)
# print("*************")
# print(arr2d[2])

# print("*******")
# print(arr2d[0][2])
# print("********")
# print(arr2d[0, 2])

# arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr3d)

# print("********")
# # print(arr3d[0])

# old_values = arr3d[0].copy()
# # print(old_values)
# arr3d[0] = 42

# # print(arr3d)

# print("*****************")
# arr3d[0] = old_values
# # print(arr3d[1,0])
# x = arr3d[1]
# print(x)
# print("********")
# print(x[0])

# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]])
# # print(arr2d[:2])

# # print(arr2d[:2, 1:])

# # print(arr2d[:2, 2])
# arr2d[:2, 1:] = 0
# print(arr2d)

# names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# print(names)

# data = np.random.randn(7,4)
# print(data)

# print(names== 'Bob')
# print(data[names == 'Bob'])

# print(data[~(names == 'Bob')])

import urllib.request
import json
import re


tweetdata = """https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt"""
webFD = urllib.request.urlopen(tweetdata)

# read the file by using readline(), which reads only one line assuming there are multiple lines
tweetLine = webFD.readline()

# tweetLine is a byte object which needs to be decoded. 
# the loads() function in the json object lets you convert the string into the json object which acts like a dictionary. 
# then decode the line that come back from the web into a string. 
tDict = json.loads(tweetLine.decode())                                                              # we assign it to the json object


# accessing the id and user
# print(tDict['id_str'])

# convert the line that comes back from the web into a string
tweetSting = tweetLine.decode()
print(tweetSting)

# declare a regular expression that simply has the created_at string
# this is looking for a string exact match

regex1 = re.compile('created_at')
# print(regex1)

# find all instances of this regular expression in my tweet.
res = regex1.findall(tweetSting)
# print(res)
# print(tDict ['created_at'])
# print(tDict ['user']['created_at'])

# if you look carefully you will see that created_at is surrounded by double quotes
#^" describes not a duble quote. - acts as a negation.
# the asterik modifies it to zero to many numbers
# beacuse we are looking for everything that fits within the opening and closing quotes
regex2 = re.compile('created_at":"[^"]*"')
res2 = regex2.findall(tweetSting)


# extracting out the actual values when you include parenthesis around
regex3 = re.compile('created_at":"([^"]*)"')
# print(regex3.findall(tweetSting))


# lets continue building on the same regular regular expression
#other than looking for the created at field, I need to look for all fields
# you replace this with the word character with plus meaning one or more
# you remove the parenthesis so that we match the whole thing.
regex4 = re.compile('"\w+":"[^"]*"')
res4 = regex4.findall(tweetSting)                                              # I get all the fields surrounded by double quotes

# if I would like to find all fields with null values
regex5 = re.compile('"\w+":null')
res5 = regex5.findall(tweetSting)                                               # this should capture all fields that happen to contain no null available.

print(res5)