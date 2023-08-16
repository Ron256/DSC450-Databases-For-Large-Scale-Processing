# Author: Ronaldlee Ejalu
# DSC 450
# Assignment module 8

import os
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import pandas
from pandas.core import frame
randn = np.random.randn

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/Week8')
columnHeaders = ['FirstName', 'MiddleInitial', 'LastName', 'EmployeeId', 'DOB', 'StreetName', 'City', 'State', 'Gender', 'Salary', 'ManagerId', 'OfficeHrCode']
employeesData = pd.read_csv('Employee.txt', names=columnHeaders)

# print(type(employeesData))                            # This is a data frame
# print(employeesData)

# all male employees
filterM = employeesData['Gender']=='M'                       # expression to define male employees
print('All male employees:')
print(employeesData[filterM])                                # use the expression to do the subselection to print all the male employees


# lowest salary for female employees
# first filter out the female employees
filterF = employeesData['Gender'] == 'F'
# print('All female employees')
employeesDataF = employeesData[filterF]                     # use the expression filter for subselection and get only the female employees
# print(employeesDataF)
print(' ')
print('The lowest salary for the female employees is %s' %(employeesDataF['Salary'].min()))
print(' ')
employeeagg = employeesData['Salary'].groupby([employeesData['MiddleInitial']])
print('The Salary groups grouped by middle initial')
for gname, gvalue in employeeagg:
    # print the group and the value corresponding to the group
    print('GroupName: ', gname)
    print('GroupValue:', gvalue)
    print('-'*30)










