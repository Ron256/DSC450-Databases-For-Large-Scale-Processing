# Author: Ronaldlee Ejalu
# DSC 450 MidTerm Exam
# Part  4e2

import os
import csv

fileName = "StudentEnrollments.txt"
os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/MidTerm')

def readFileRows(fileName):
    """Function that reads a file and returns a list of objects"""
    with open(fileName, 'r') as readObject:
        csvReaderObj = csv.reader(readObject)                                   # pass the file object as an argument to the reader() method to generate the reader object, which is an iterator

        
        listOfRecords = list(csvReaderObj)                                  # generate  a list of lists by passing the reader object, csvReaderObj, as an argument to the list() method and each list represents a row of csv and each corresponding item represents a cell / column in that row. 
        # print(listOfRecords)
    readObject.close()
    
    return listOfRecords                                                    # return a list of lists object 


def testFnDepedencyV(listOfObjects):
    """
    A function that populates a dictionary of courses with keys and values 
    and also tests if there is a functional dependency violation
    """
    sCoursesd = {}
    for rowItem in listOfObjects:
        if rowItem[4] == "None":
            pass
        elif rowItem[4] not in sCoursesd:
            sCoursesd[rowItem[4]] = rowItem[-2].strip()
        elif rowItem[4] in sCoursesd.keys():
            if sCoursesd[rowItem[4]] != rowItem[-2].strip():
                print("There is a functional dependency violation at row: \n %s"%(rowItem))

def deriveDepartmentDict(listOfObjects):
    """
    A function that populates a dictionary of Departments and GradYears and 
    finds the average of Graduation year for each department
    """
    dept = {}
    cntCDM = 1
    cntCSC = 1
    res = 0
    for rowItem in listOfObjects:                                       # iterate through a list of objects
        if rowItem[5].strip() == "None":
            pass
        elif rowItem[5] not in dept.keys() and rowItem[5] != '':
            if rowItem[3] != '':
                # print(rowItem[5], rowItem[3].strip())
                dept[rowItem[5].strip()] = rowItem[3].strip()
        elif rowItem[5] in dept.keys() and rowItem[5] == 'CDM':
            cntCDM = cntCDM + 1
            dept[rowItem[5]] = int(dept[rowItem[5]]) + int(rowItem[3])
        elif rowItem[5] in dept.keys() and rowItem[5] == 'Computer Science':
            cntCSC = cntCSC + 1
            dept[rowItem[5]] = int(dept[rowItem[5]]) + int(rowItem[3]) 

    print("The average graduation year for CDM is %s"%(dept['CDM']/cntCDM))
    print ("The average graduation year for Computer Science is %s" %(round(dept['Computer Science']/cntCSC, 1)))

listOfFileRows = readFileRows(fileName)                                       # Helper function to read the file and returns a list of objects
#testFnDepedencyV(listOfFileRows)                                            # Helper function that adds the corresponding courses with their credits to the dictionary and also tests for any violation in the functional dependency. 
deriveDepartmentDict(listOfFileRows)                                        # Helper function that populates a dictionary of Departments and GradYears and finds the average of Graduation year for each department
