
def computeTheAverage(strParameter):
    """Function that returns the average of a string containing comma separated number"""

    average = 0
    sum = 0  

    # Using a list comprehension to access the string values, 
    # which are converted into an integer before being added to the list. 
    listOfStringValues = [int(i) for i in strParameter.strip().split(', ')]
  
    for num in listOfStringValues:                              # iterate through a list of numbers as you compute the sum.
        sum += int(num)

    average = sum / len(listOfStringValues)                     # compute the average
    return average                                              # return the average

def main():
    # strParameter = "5, 6, 12, 55, 1"
    # test1 = computeTheAverage(strParameter)           # helper function which takes a string containing comma separated numbers and returns the average of those numbers
    # print("The average of a string containing comma separated numbers (%s)  is %s" %(strParameter, test1))


    strPar2 = "100, 3, 6, 0, 56, 3, 9, 19"
    test2 = computeTheAverage(strPar2)                  # helper function which takes a string containing comma separated numbers and returns the average of those numbers
    print("The average of a string containing comma separated numbers (%s)  is %s" %(strPar2, test2))

main()