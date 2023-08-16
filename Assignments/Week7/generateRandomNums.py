# Author: Ronaldlee Ejalu
# Course: DSC 450
import numpy as np
import pandas as p

def xRandomNumbers(xRandom):
    """A function that generates a list of x random numbers """
    xRandomL = list(np.random.randint(low = 31, high = 100, size = xRandom))
    return xRandomL                                                                                 # return a list of x random numbers

# 1b 
# using a list of 60 random numbers with the above function
# and using pandas.Series to determine how many of the numbers are below 37
series1 = p.Series(xRandomNumbers(60))


filter = series1 < 37                                                                               # create a filter 
# print(filter)
numsLessThan37 = series1[filter]                                                                    # use a filter to perform sub selection/ 
# print("There are %s numbers, which are below 37" %(numsLessThan37.size))                            # use the size attribute to determine the number of elements in the underlying data

# list of 60 random numbers
sixtyRandomNumsL = xRandomNumbers(60) 
# print(sixtyRandomNumsL)


arr = np.array(sixtyRandomNumsL)                                                                    # creating a numpy array
print(arr)
print("********************************************************************************************")

arr6by10 = np.reshape(arr, (6, 10))                                                                 # modiying the numpy array and creating a 6 by 10   numpy array              
print(arr6by10)

arrFilter = arr6by10 >= 50                                                                          # creating a filter for values greater than or equal to 50 
arr6by10[arrFilter] = 50                                                                            # doing a sub-selection and replacing all the values greater than or equal to 50 by 50. 

print(arr6by10)                                                                                     # printing the original numpy array