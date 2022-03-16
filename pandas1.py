from readline import get_history_item
import pandas as pd

grades = pd.Series([87,100,94])

print(grades)

a = pd.Series(98.6, range (3))

#print() # breakpoint # debugger

b = grades[0]
c = grades.count()
d = grades.mean()

print(grades.describe()) # all stats in one shot

# Custom Indexing

grades = pd.Series([87,100,94], index=['Wally', 'Eva', 'Sam'])

#print(grades)

# Directly Create a Series from a Dictionary

grades_dict = {'Wally':87, 'Eva':100, 'Sam': 94} # the keys become the indexes # the values become the columns
grades_ds = pd.Series(grades_dict)

print(grades_ds)

eva = grades['Eva']
wally = grades.Wally

e = grades.values

hardware = pd.Series(['Hammer','Saw','Wrench'])
f = hardware.str.contains('a')
g = hardware.str.upper()

#convert a series object to a Python list
hardware_list = hardware.to_list()

ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,9])

g = ds1 == ds2
h = ds1 > ds2
i = ds1 < ds2
#print(g)
#print(h)
#print(i)

list_of_series = pd.Series([['Red','Green','White'], ['Red','Black'], ['Yellow']])
list_of_series = list_of_series.apply(pd.Series).stack().reset_index(drop=True) # making just one series and resetting all the indexes

# sort a series
s = pd.Series(['100','200','python','300.12','400'])
sorted_series = s.sort_values() # can do sort index or sort values, we may want to sort based on values because index is one or zero

#s = pd.Series(['100',200,'python',300.12,'400']) # error because integers and float, it can't sort elements that have different data types
#sorted_series = s.sort_values() 

#adding to a Series
s = s.append(pd.Series(['500','php'])).reset_index(drop=True) # have to reassign it to s

# write a Pandas program to calculate the frequency counts of each unique value of a given series.
import random
list1 = [random.randrange(1,10) for i in range(0,100)]
s = pd.Series(list1)
result = s.value_counts()

print()




