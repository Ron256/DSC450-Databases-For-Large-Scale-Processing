import os
import csv
from csv import reader

fileName = "animal.txt"
os.chdir("C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/Week4")
# print(os.getcwd())




def readFileContents(fileName):
    """Return the list of the file contents after reading the file"""
    fname = open(fileName, 'r')                             # open the file.
    fileContents = fname.readlines()                        # returns a list containing each line in the file as a list item and assigns it to the list object

    fname.close()                                           # close the file

    return fileContents                                     # return the list of the file contents.




def notTiger():
    """print the names of the animals that are not related to the tiger"""
    fileContents = readFileContents(fileName)
    print("\nThe names of the animal that are not related to the tiger:")
    for item in fileContents:
        row =  item.strip()                                     # used strip to remove all white space characters
        # print(row)                                            # used for debugging purposes                                      
        # print("debugging %s"%(row.split(',')[2].strip()))     # used for debugging purposes

        # names of the animals that are not related to the tiger
        if 'tiger' not in row.split(',')[1]:
            print(row.split(',')[1])



def notComAnimalRtdTiger():
    """Print the names of animals that are related to the tiger and are not common from the file"""
    fileContents = readFileContents(fileName)
    print("Names of the animals that are related to the tiger and are not common:")

    for item in fileContents:
        row = item.strip()
        # names of the animals that are related to the tiger and are not common.
        if 'tiger' in row.split(',')[1] and 'common' != row.split(',')[2].strip():
            print(row.split(',')[1])




notComAnimalRtdTiger()

notTiger()
