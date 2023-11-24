#
# Lab 5, Task 2
#
# A program that uses a loop to perform two cumulative computations: 
# adding a set of integers, and counting how many integers there are.
#

num_vals = int(input('Enter the number of values: '))

total = 0

for i in range(num_vals):
    val = int(input('Enter a value: '))
    total = total + val
    
print('the total of the values is', total)
print('the number of values is', num_vals)
