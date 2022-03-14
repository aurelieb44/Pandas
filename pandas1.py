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

print()




