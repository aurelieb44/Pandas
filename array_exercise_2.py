## Numpy Exercise 2
import numpy as np
import pandas as pd

## This array documents the last 5 sales for each of Superstore's four cash registers. 
salesArray = np.array([[150.68,207.99,107.88,58.99,60.59],[20.89,98.99,258.62,19.76,101.59],[70.66,190.10,134.54,200.14,15.59],[10.52,201.59,140.55,13.99,45.98]])

#salesArray.index = ["Cash Register 1", "Cash Register 2", "Cash Register 3", "Cash Register 4"]

## Step 1: Print the total sales for the store.
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")

ts_store = int(salesArray.sum())
print('\nTotal Sale for the store:\n $', ts_store)

print()

## Step 2: What was Superstore's smallest and largest sale? Print them.
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")

low = salesArray.min()
high = salesArray.max()
print('\nSuperstore highest sales:\n', low)
print('\nSuperstore lowest sales :\n', high)

print()

## Step 3: Print an array that will show which sales are greater than or equal to $100.
print("-----------------------------------------------   STEP THREE  -----------------------------------------------")

greater_100 = salesArray[salesArray>=100]
print('\nNew array for sales greater than 100:\n\n', greater_100)

print()

## Step 4: Print the total sales for each register.
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")

print('\nTotal Sales', salesArray.sum(axis=1))

register_num = 1
index = 0
for register in salesArray:
    ts_register = int(salesArray[index].sum())
    print('\nTotal Sale for Register ', register_num, ':\n $', ts_register)
    register_num += 1
    index += 1

print()

## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. Each sale is subject to a 2% credit card fee.
#           Using the salesArray, create a new array that stores the 2% fee for each sale and register. Print the array and then print the total fees.
print("-----------------------------------------------   STEP FIVE  -----------------------------------------------")

feeArray = salesArray*0.02
print('\nNew Array for sales greater than 100:\n\n', feeArray)

tf= int(feeArray.sum())
print('\nTotal Fees for the store:\n $', tf)

print()

## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. Store this in a new array and print it.
print("-----------------------------------------------   STEP SIX  -----------------------------------------------")

profitArray = salesArray - feeArray
print('\nNew Array for Total Profit for the store:\n', profitArray)

t_profit= int(profitArray.sum())
print('\nTotal Profit for the store:\n $', t_profit)

print()

## Step 7: Print the sales only for the second and forth cash register # ROWS
print("-----------------------------------------------   STEP SEVEN  -----------------------------------------------")

ts_2_4_registers = salesArray[[1,3]].sum()
print('\nTotal Sales for Registers 2 and 4:\n ', ts_2_4_registers)


print()

## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister. Add the new register to the original array. Print the updated salesArray.
print("-----------------------------------------------   STEP EIGHT  -----------------------------------------------")
newRegister = np.array([17.89,13.59,107.89,176.88,56.78])
new_salesArray = np.vstack((salesArray,newRegister))
print(new_salesArray)

print()

## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly. The sale should have been $20.14. Update the array to correct this error.
#           Print the array before and after the update to see the change.
print("-----------------------------------------------   STEP NINE  -----------------------------------------------")


print('\nFormer Array:\n', salesArray)
salesArray[2][3] = 20.14
print('\nUpdated Array:\n', salesArray)

print()

