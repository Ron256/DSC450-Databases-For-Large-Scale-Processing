import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import pandas
from pandas.core import frame
randn = np.random.randn

obj = pd.Series([4, 7, -5, 3])
# print(obj)

# print(obj.values)
# print(obj.index)

obj2 = pd.Series([4,7,-5,3], index= ['d', 'b', 'a', 'c'])

# changing the value of d
obj2['d'] = 6
# print(obj2[['c', 'a', 'd']])
# print(obj2[obj2 > 0])

# print(obj2 * 2)

sdata = {'Ohio':35000, 'Texas':71000, 'Oregon': 16000, 'Utah': 5000}

states = ['California', 'Ohio', 'Oregon', 'Texas']
statesSeries = pd.Series(sdata, index = states)
# print(statesSeries)
# print(pd.notnull(statesSeries))

# print(statesSeries.isnull())
statesSeries.name = 'population'
statesSeries.index.name = 'state'
# print(statesSeries)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
# print(obj)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003], 
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# frame = pd.DataFrame(data)

# print(frame.head())

# specifying a sequence of columns
frames = pd.DataFrame(data, columns=['year', 'state', 'pop'])
# print(frames)
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five', 'six'])

# print(frame2.columns)
# print(frame2['state'])
# print(frame2.year)
# print(frame2.loc['three'])
frame2['debt'] = 16.5
# print(frame2)
frame2['debt'] = np.arange(6.)
# print(frame2)

val = pd.Series([-1.2, -1.5, -1.7], index= ['two', 'four', 'five'])
# print(val)
frame2['debt'] = val
# print(frame2)
frame2['eastern'] = frame2.state == 'Ohio'
del frame2['eastern']
# print(frame2.columns)

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
        'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
# print(frame3)
# # transposing the data frame
# print(frame3.T)
frame4 = pd.DataFrame(pop, index=[2001, 2002, 2003])
# print(frame4)
pdata = {'Ohio':frame3['Ohio'][:-1], 'Nevada':frame3['Nevada'][:2]}
frame3.index.name = 'year'
frame3.columns.name = 'state'
# print(frame3.values)
# print(pd.DataFrame(pdata))
  
# print(frame2.values)
obj = pd.Series(range(3), index=['a', 'b', 'c'])
# print(obj.index)
index = obj.index
# print(obj.index)
# print(index[1:])
labels = pd.Index(np.arange(3))
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
# print(obj2.index is labels)
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                        index=['a', 'c', 'd'],
                        columns=['Ohio', 'Texas', 'California'])
states = ['Texas', 'Utah', 'California']

frame = frame.reindex(columns=states)
# print(frame)

 
#frame2 = frame.reindex(['a','b', 'c', 'd'])
# print(frame.loc[['a','b', 'c', 'd'], states])
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])

# print(obj)
new_obj = obj.drop(['c', 'd'])
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                       index=['Ohio', 'Colorado', 'Utah', 'New York'],
                       columns=['one', 'two', 'three', 'four'])


# print(data.drop('two', axis=1))
# print(data.drop(['two', 'four'], axis='columns'))

obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
# print(obj['b'])
# print(obj[2:4])
# print(obj[['b','a','d']])
# print(obj[[1, 3]])
# print(obj[obj < 2])
obj['b':'c'] = 5
# print(obj)
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                        index=['Ohio', 'Colorado', 'Utah', 'New York'],
                        columns=['one', 'two', 'three', 'four'])
print(data)
print("********************************")
# print(data['two'])
# print(data[['three', 'one']])

# two rows
# print(data[:2])

# print('************************************')

# print(data.loc['Colorado',['two', 'three']])

# using iloc
print('************************************')
# print(data.iloc[[1,2],[3,0,1]])
# print(data.loc[:'Utah', 'two'])
# print(data.iloc[:, :3][data.three > 5])
ser = pd.Series(np.arange(3.))
ser2 = pd.Series(np.arange(3.), index=['a','b','c'])
# print(ser2[-1])

df = pandas.DataFrame({'city':['Chicago', 'Chicago', 'Boston', 'Portland', 'Portland', 'Portland'], 'state':['IL', 'IL', 'MA', 'ME', 'OR', 'ME'], 'data1' : randn(6), 'data2': randn(6) })
print(df)


# aggregation 
data1agg = df['data1'].groupby(df['city'])
# data1agg contains the group and the value corresponding to the group
# print(data1agg)

#The equivalent of saying select city, max of the data column from the data group by city
# print(data1agg.max())

# you can apply any other function to the group
# print(data1agg.mean())

# If I wanted to see the contents of this object, data1agg, combined with city and the contents that I selected
# print the group and the value that corresponds to it.

for gname, gvalue in data1agg:
    # print the group and the value corresponding to the group
    print('GroupName: ', gname)
    print('GroupValue:', gvalue)
    print('-'*30)

# composite grouping
gby1 = df.groupby(['state', 'city']).min()
print('minimum')
print(gby1)

# gby2 = df['data2'].groupby([df['state'], df['city']])
# for gname, gvalue in gby2:
#     # print the group and the value corresponding to the group
#     print('GroupName: ', gname)
#     print('GroupValue:', gvalue)
#     print('-'*30)

# print('******************************************')
# print(gby2.count())
# print('************')
# simple data transformation

spellout = {'IL': 'Illinois', 'MA': 'Massachussets', 'OR':'Oregan', 'ME': 'Maine'}
# use the map function to transform the data into spellout states

df['state'] = df['state'].map(lambda x: spellout[x])
print(df)


 
