import pandas as pd
import numpy as np
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

# print(sdata) 

obj3 = pd.Series(sdata)
# print(type(obj3))

# print(obj3)
states = ['California','Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)

# print(obj4)
# print(pd.isnull(obj4))    # determine missing data
# print(pd.notnull(obj4))       # determine non missing data

# print(obj4.isnull())
# print(obj3 + obj4)

obj = pd.Series([4, 7, -5, 3])
# print(obj)
obj.index = ['Bob', 'Steve', 'Jeff','Ryan']
# print(obj)

#define two lists
list1 = ["blue", "black", "tangerine", "brown"]
list2 = [23, 44, 51, 14]

#keys-value lists
# print ("Keys: " + str(list1))
# print ("Values: " + str(list2))

dict1 = dict(zip(list1, list2))

# print(dict1)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
        }

frame = pd.DataFrame(data, columns=['year','state', 'pop','debt'], index=['one', 'two', 'three', 'four', 'five', 'six'])
# print(frame)
# print(frame['state'])
# print(frame.loc['three'])
# frame['debt'] = np.arange(6.)
# print(frame)

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame['debt'] = val
# print(frame)
frame['eastern'] = frame.state == 'Ohio'
del frame['eastern']
# print(frame)
# print(frame.columns)

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
        'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = pd.DataFrame(pop, index=[2000,2001, 2002])
# print(frame3) 

# print(frame3.T)
# pdata = {'Ohio':frame3['Ohio'][:-1], 'Nevada':frame3['Nevada'][:2]}
# print(pd.DataFrame(pdata))
frame3.index.name = 'year'
frame3.columns.name = 'state'
# print(frame3.values) 
obj = pd.Series(range(3), index=['a','b','c'])
# print(obj)
index = obj.index
# print(index[1:])
labels = pd.Index(np.arange(3))
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
# print(obj2)
# print('Ohio' in frame3.columns)
# print('2003' in frame3.index)
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
# print(dup_labels)

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index = ['d', 'b', 'a', 'c'])
obj = obj.reindex(['a','b','c','d','e'])
# print(obj)

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0,2,4])
obj3 = obj3.reindex(range(6), method = 'ffill')
# print(obj3)
frame = pd.DataFrame(np.arange(9).reshape((3,3)), index=['a','c','d'], columns=['Ohio', 'Texas', 'California'])
# print(frame)
frame = frame.reindex(['a', 'b', 'c', 'd'])
# print(frame2)
states = ['Texas', 'Utah', 'California']
frame = frame.reindex(columns=states)
frame = frame.loc[['a', 'b', 'c', 'd'], states]
# print(frame)
obj = pd.Series(np.arange(5.), index = ['a','b','c', 'd', 'e'])
new_obj = obj.drop(['d','c'])
# print(new_obj)


# print(data)
# data = data.drop(['Colorado','Ohio'])
# data = data.drop(['two', 'four'], axis='columns')
# print(data)

obj = pd.Series(np.arange(4.), index=['a','b','c','d'])
# print(obj)
# print(obj['b':'c'])
obj['b':'c'] = 5
# print(obj)
data = pd.DataFrame(np.arange(16).reshape((4, 4)), 
index=['Ohio', 'Colorado', 'Utah', 'New York'],
          columns=['one', 'two', 'three', 'four'])

# print(data[['three', 'one']])
data[data < 5] = 0
# print(data.loc['Colorado', ['two','three']])
print(data)
print('***'*30)
print(data.loc[:'Utah', 'two'])
 







