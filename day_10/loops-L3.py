############################################
##  Day 10: 30 Days of python programming  #
############################################

# Exercises: Level 3

# 1 - Go to the data folder and use the countries.py file. Loop through the countries 
#     and extract all the countries containing the word land.
datas = open("countries.txt")
pattern = "land"
liste = []

for data in datas:
    if pattern in data:
        data = ''.join(filter(str.isalnum, data))
        liste.append(data)

print(liste)

# 2 - This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] 
#     reverse the order using loop.
liste = ['banana', 'orange', 'mango', 'lemon']
new_liste = []

for idx in range(len(liste) - 1, -1, -1):
    new_liste.append(liste[idx])

print(new_liste)

# 3 - Go to the data folder and use the countries_data.py file.

# a - What are the total number of languages in the data
# b - Find the ten most spoken languages from the data
# c - Find the 10 most populated countries in the world
