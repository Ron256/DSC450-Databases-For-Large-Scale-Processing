
# Author's name: Ronaldlee Ejalu
# Course: DSC 450
# Part 1-4
import re
def validateInsert(sqlStatement):
    """A function that validates a SQL Insert statement"""
    validSql = re.search("^INSERT INTO.*;$", sqlStatement)

    if validSql: # check if the string starts with an INSERT INTO statement and ends with a semi colon
        startPos = sqlStatement.index("(")                                                                          # search for the first bracket
        endPosition = sqlStatement.index(")")                                                                       # search for the first closing bracket
        valuesString = sqlStatement[startPos:endPosition + 1]                                                       # extract out the values string.
        startPosInto =  sqlStatement.find("INTO")                                                                   # search for into statement
        endPosVal = sqlStatement.find("VALUES")                                                                     # search for the VALUES statement

        tableName = sqlStatement[startPosInto + 5: endPosVal - 1].strip()                                           # extract out the table name

        print("Inserting %s into %s table" %(valuesString, tableName))
        
    else:
        print("Invalid insert")


validateInsert("INSERT INTO Students VALUES (1, Jane, A+);")
validateInsert('INSERT INTO Students VALUES (1, Jane, A+)')
validateInsert('INSERT Students VALUES (1, Jane, A+);')
validateInsert('INSERT INTO Phones VALUES (42, 312-555-1212);')
