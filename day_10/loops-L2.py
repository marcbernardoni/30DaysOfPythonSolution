############################################
##  Day 10: 30 Days of python programming  #
############################################

# Exercises: Level 2

# 1 - Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_all = 0

for i in range(101):
    sum_all += i

print(f"The sum of the first 100 numbers is equal to {sum_all}")

# 2 - Use for loop to iterate from 0 to 100 
#     and print the sum of all evens and the sum of all odds.
sum_even, sum_odd = 0, 0

for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"The sum of the first 100 even numbers is equal to {sum_even} while the sum of the first 100 odd numbers is equal to {sum_odd}")