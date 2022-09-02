###########################################
##  Day 6: 30 Days of python programming  #
###########################################

# Exercises: Level 2
import math

family_members = ('Marc', 'Christophe', 'Eric', 'Jordan', 'Erin',
                  'Samantha', 'Corine', 'Karine', 'Elisabeth', 'André', 'Geneviève')
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# 1 - Unpack siblings and parents from family_members
print(family_members)
siblings = family_members[0:len(family_members) - 3]
parents = family_members[-2:]

print(f'Siblings are {siblings} \nand parents are {parents}')

# 2 - Create fruits, vegetables and animal products tuples.
#     Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon', 'apple')
vegetables = ('Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce')
animals = ('pork', 'chicken', 'beef', 'duck')

food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

# 3 - Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(f'{food_stuff_lt} is {type(food_stuff_lt)} type')

# 4 - Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = []

if len(food_stuff_tp) % 2 == 0:
    # The Tuple contains an even number of elements
    middle_item = food_stuff_tp[int(len(
        food_stuff_tp) / 2) - 1:int(len(food_stuff_tp) / 2) + 1]
else:
    # The Tuple contains an odd number of elements
    middle_item = food_stuff_tp[math.floor(len(food_stuff_tp) / 2)]

print(middle_item)

# 5 - Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-3:]

print(f'{first_three}, {last_three}')

# 6 - Delete the food_staff_tp tuple completely
del (food_stuff_tp)

# 7 - Check if an item exists in tuple:
# a - Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

# b - Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
