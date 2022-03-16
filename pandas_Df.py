import pandas as pd

grades_dict = {'Wally':[87,96,70],'Eva':[100,87,90],'Sam':[94,77,90],'Katie':[100,81,82],'Bob':[83,65,85]} 
# the value of each key is a list # each value become a row in the dataframe

# a series is one-dimensional array
# a data frame is a two-diensional array
# each column on a data frame is a series

grades = pd.DataFrame(grades_dict)
grades.index = ['Test1','Test2','Test3']
print(grades) 

eva = grades['Eva'] # the object returned is a series, which is one column in a dataframe
same = grades.Sam # can only do this with string indexes

# Using the loc and iloc methods (location)
# iloc method uses integers, indexes
test2 = grades.loc['Test2']
test1 = grades.iloc[0]

# For Consecutive rows - we need a column
test1_thru_test3 = grades.loc['Test1':'Test3'] # semi-column

# For Non-Consecutive rows
test1_and_test3 = grades.loc[['Test1','Test3']] # use a comma and it has to be in a list, therefore double brackets

test1_and_test2 = grades.iloc[0:2] # the iloc method doesn't include the upper index # it'll only do 0 and 1


# View only Eva's and katie's grades for Test1 and Test2
eva_katie_1_2 = grades.loc[['Test1','Test2'],['Eva','Katie']] # first part is row, second part is columns
eva_katie_1_2 = grades.loc[:'Test2',['Eva','Katie']] # other option
#print(eva_katie_1_2)

# View only Sam's thru Bob's grades for Test1 and Test3
sam_bob_1_2_3 = grades.loc[['Test1','Test3'],'Sam':] # don't have to mention Bob because ti's upper limit
print(sam_bob_1_2_3) 

# Boolean Indexing
# Select everyone with an A grade
grades_A = grades[grades >= 90]

#create a dataframe for everyone with a B grade
grades_B = grades[(grades >= 80) & (grades < 90)]

#create a dataframe for everyone with an A or B grade # pipe symbol
grades_A_or_B = grades[(grades >=90) | (grades >= 80)]

pd.set_option('precision',2)

# information by student
print(grades.describe())

# information by test
print(grades.T.describe()) # we transpose it

# get the average of all the students grades on each test
print(grades.T.mean())

# sort rows by their indices (Test name)
r_sorted_grades_i = grades.sort_index(ascending=False)
print(r_sorted_grades_i)

# sort columns by their column names (student names)
# axis = 1 indicates to sort by oclumn indices
# axis = 0 indicates to sort by row indices
c_sorted_grades_i = grades.sort_index(axis=1)
print(c_sorted_grades_i)

# in reverse sort order
cr_sorted_grades_i = grades.sort_index(axis=1, ascending=False)
print(cr_sorted_grades_i)

print()


