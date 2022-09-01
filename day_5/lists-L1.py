###########################################
##  Day 4: 30 Days of python programming  #
###########################################
from copy import copy
import math
from turtle import back
# Exercises: Level 1

# 1 - Declare an empty list
my_list = []
print(type(my_list))

# 2 - Declare a list with more than 5 items
my_list = ['Microsoft', 'Bill Gates', 1975, 221000, True]

# 3 - Find the length of your list
print(len(my_list))

# 4 - Get the first item, the middle item and the last item of the list
print(my_list[0], my_list[math.floor(len(my_list) / 2)],
      my_list[len(my_list) - 1])

# 5 - Declare a list called mixed_data_types,
#     put your(name, age, height, marital status, address)
mixed_data_types = ['Marc', 54, 172, 'married', 'France']

# 6 - Declare a list variable named it_companies and assign initial values
#     Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']

# 7 - Print the list using print()
print(it_companies)

# 8 - Print the number of companies in the list
print(len(it_companies))

# 9 - Print the first, middle and last company
print(it_companies[0], it_companies[math.floor(len(it_companies) / 2)],
      it_companies[len(it_companies) - 1])

# 10 - Print the list after modifying one of the companies
it_companies.pop()
print(it_companies)

# 11- Add an IT company to it_companies
it_companies.append('Amazon')
print(it_companies)

# 12 - Insert an IT company in the middle of the companies list
it_companies.insert(math.floor(len(it_companies) / 2), 'Sun')
print(it_companies)

# 13 - Change one of the it_companies names to uppercase (IBM excluded!)
upper_companies = []
for i in it_companies:
    if i == 'IBM':
        upper_companies.append(i.lower())
    else:
        upper_companies.append(i.upper())

print(upper_companies)

# 14 - Join the it_companies with a string '#;  '
print(('#; ').join(it_companies))

# 15 - Check if a certain company exists in the it_companies list.
print('Amazon' in it_companies)
print('Thomson' in it_companies)

# 16 - Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17 - Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18 - Slice out the first 3 companies from the list
first_three = it_companies[0:3]
print(it_companies)
print(first_three)

# 19 - Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(it_companies)
print(last_three)

# 20 - Slice out the middle IT company or companies from the list
index = (math.floor(len(it_companies) / 2))
middle = it_companies[index - 1: index + 1]
print(it_companies)
print(middle)

# 21 - Remove the first IT company from the list
print(it_companies)
# it_companies.remove(it_companies[0])
it_companies.pop(0)
print(it_companies)

# 22 - Remove the middle IT company or companies from the list
# odd list
it_companies = ['Sun', 'Oracle', 'Microsoft',
                'IBM', 'Facebook', 'Apple', 'Amazon']
# even list
#it_companies = ['Oracle', 'Microsoft', 'IBM', 'Facebook', 'Apple', 'Amazon']

print(it_companies)
index = (math.floor(len(it_companies) / 2))

if len(it_companies) % 2 == 0:
    del it_companies[index - 1: index + 1]
else:
    it_companies.pop(index)

print(it_companies)

# 23 - Remove the last IT company from the list
print(it_companies)
it_companies.pop()
print(it_companies)

# 24 - Remove all IT companies from the list
print(it_companies)
it_companies.clear()
print(it_companies)

# 25 - Destroy the IT companies list
print(it_companies)
del it_companies
# print(it_companies) throw 'NameError' error

# 26 - Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
print(front_end.extend(back_end))

# 27 - After joining the lists in question 26.
#      Copy the joined list and assign it to a variable full_stack.
#      Then insert Python and SQL after Redux.
full_stack = front_end
full_stack2 = full_stack.copy()

# 1st method
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Redux') + 2, 'SQL')
print(full_stack)

# 2nd method
insert = ['Python', 'SQL']
full_stack2[full_stack2.index(
    'Redux') + 1:full_stack2.index('Redux') + 1] = insert
print(full_stack2)
