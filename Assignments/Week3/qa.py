# Python3 code to convert tuple 
# into string
from csv import reader
def readFileRows():
    with open('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/Week3/Animal.txt', 'r') as readObject:
        csvReaderObj = reader(readObject)                                   # pass the file object as an argument to the reader() method to generate the reader object

        
        listOfRecords = list(csvReaderObj)                                  # generate  a list of lists by passing the reader object, csvReaderObj, as an argument to the list() method
        print(listOfRecords)
    
    return listOfRecords                                                    # return a list of list of formatted records 

readFileRows()
