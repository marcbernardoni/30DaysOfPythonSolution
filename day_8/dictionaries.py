###########################################
##  Day 8: 30 Days of python programming  #
###########################################

# 1 - Create an empty dictionary called dog
dog = {}
print(type(dog))

# 2 - Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'daisy',
    'color': 'brown and fire',
    'breed': 'Royal Bourbon',
    'legs': 4,
    'age': 6
}

for key in dog:
    print(f'the {key} name contains the value {dog[key]}.')

# 3 - Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Marc',
    'last_name': 'Bernardoni',
    'gender': "M",
    'age': 54,
    'marital_status': 'married',
    'skills': [
        'Python',
        'JavaScript',
        'LUA'
    ],
    'country': 'France',
    'city': 'Paris',
    'address': "1, rue de la Pompe"
}

# 4 - Get the length of the student dictionary
print(len(student))

# 5 - Get the value of skills and check the data type, it should be a list
print(type(student['skills']))

# 6 - Modify the skills values by adding one or two skills
print(student['skills'])
student['skills'] += ['HTML', 'CSS']
print(student['skills'])

# 7 - Get the dictionary keys as a list
keys = []
for key in student:
    keys.append(key)

print(keys)

# 8 - Get the dictionary values as a list
values = []
for key in student:
    values.append(student[key])

print(values)

# 9 - Change the dictionary to a list of tuples using items() method
tuples = ()
tuples = student.items()

print(tuples)

# 10 - Delete one of the items in the dictionary
student.pop('city')
print(student)

# 11 - Delete one of the dictionaries
del dog
