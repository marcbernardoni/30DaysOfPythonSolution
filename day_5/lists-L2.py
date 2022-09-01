###########################################
##  Day 5: 30 Days of python programming  #
###########################################
import math

# Exercises: Level 2

# 1 - The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a -Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[len(ages) - 1]

print(
    f'minimum age is {ages[0]}, maximum age is {ages[len(ages) - 1]} from the list {ages}')

# b -Add the min age and the max age again to the list
print(ages)

ages.insert(0, min_age)
ages.append(max_age)

print(ages)

# c -Find the median age (one middle item or two middle items divided by two)
# even list
# ages = [19, 22, 19, 23, 20, 25, 26, 24, 25, 26]
# odd list
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25]

# ages.sort()
# print(ages)

if len(ages) % 2 == 0:
    median_age = (ages[int(len(ages) / 2) - 1] + ages[int(len(ages) / 2)]) / 2
else:
    median_age = ages[math.floor(len(ages) / 2)]

print(median_age)

# d -Find the average age (sum of all items divided by their number )
average = 0

for i in ages:
    average += i
average /= len(ages)

print(average)

# e -Find the range of the ages (max minus min)
print(f'The range of the list {ages} is {ages[len(ages) - 1] - ages[0]}')


# f -Compare the value of (min - average) and (max - average), use abs() method
print(abs(ages[len(ages) - 1] - average) == abs(ages[0] - average))

# 2 - Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA',
             'Finland', 'Sweden', 'Norway', 'Denmark']

middle_countries = []

if len(countries) % 2 == 0:
    middle_countries.append(countries[int(len(countries) / 2) - 1])
    middle_countries.append(countries[int(len(countries) / 2)])
else:
    middle_countries = countries[math.floor(len(countries) / 2)]

print(middle_countries)

# 3 - Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = []
second_half = []

if len(countries) % 2 == 0:
    first_half = countries[0:int(len(countries) / 2)]
    second_half = countries[-int(len(countries) / 2):]
else:
    first_half = countries[0:math.floor(len(countries) / 2) + 1]
    second_half = countries[-math.floor(len(countries) / 2):]

print(first_half)
print(second_half)


# 4  - Unpack the first three countries and the rest as scandic countries.
first_country, second_country, third_country, fourth_scandic = first_half
first_scandic, second_scandic, third_scandic = second_half

print(f'{first_country}, {second_country}, {third_country}')
print(f'{first_scandic}, {second_scandic}, {third_scandic}')
