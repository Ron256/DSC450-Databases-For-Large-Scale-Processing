
def generateInsertString(tableName, listPar):
    """Function that returns a SQL Statement given the table name and the value list as parameters"""
        
    valuesL = listPar    # assign the value list parameter to the valuesL object
    stringValue = ""     # declare a string object
    delim = ", "         # declare and assign a character delim 
    for i in valuesL:    # iterate through the elements of the list

        if i.strip("").replace("-","").isdigit():      # replace any hypens with an empty space before checking whether the element is a digit. 
            stringValue += str(i) + delim              # build a string 
        else:
            stringValue += '"' + str(i) + '"' + delim
    
    derivedStr = "(" + stringValue[0:(len(stringValue.strip(" ")) - 1)] + ");"   # clean up the derived string by removing the last comma and surround the string within brackets

    return "INSERT INTO %s VALUES %s" %(tableName, derivedStr)                      # return the derived SQL Insert statement


   
#print(generateInsertString('Students', ['1', 'Jane', 'A+']))
# print(generateInsertString("Phones", ['42', '312-555-1212']))
print(generateInsertString("Contacts", ['34', 'Ronaldlee', 'Ejalu', '734-757-5933']))

