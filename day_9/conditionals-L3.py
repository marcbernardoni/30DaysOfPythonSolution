###########################################
##  Day 9: 30 Days of python programming  #
###########################################
import math

# Exercises: Level 3

# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# a - Check if the person dictionary has skills key,
#     if so print out the middle skill in the skills list.
if person['skills'] != 0:
    print(f"This person has the following skills: {person['skills']}")
    length = len(person['skills'])
    if length % 2 == 0:
        value1 = list(person['skills'])[int(math.floor(length / 2)) - 1]
        value2 = list(person['skills'])[int(math.floor(length / 2))]
        print(f"The middle skills on the skill list are {value1} and {value2}")
    else:
        print(
            f"The middle skill on the skill list is {list(person['skills'])[int(math.floor(length / 2))]}")
else:
    print("This person has no skills")

# b - Check if the person dictionary has skills key,
#     if so check if the person has 'Python' skill and print out the result.
skill = 'Python'

if person['skills'] != 0:
    if skill in person['skills']:
        print(f"This person has the {skill} skill")
    else:
        print(f"This person does not have the {skill} skill")
else:
    print("This person has no skills")

# c - If a person skills has only JavaScript and React,
#     print('He is a front end developer'),
#     if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#     if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
#     else print('unknown title') - for more accurate results more conditions can be nested!
skills = person['skills']
front = ['JavaScript', 'React']
back = ['Node', 'Python', 'MongoDB']
full = ['React', 'Node', 'MongoDB']

if skills != 0:
    if all(item in skills for item in front):
        print('He is a front end developer')
    elif all(item in skills for item in back):
        print('He is a backend developer')
    elif all(item in skills for item in full):
        print('He is a backend developer')
    else:
        print('unknown title')
else:
    print("This person has no skills")

# d - If the person is married and if he lives in Finland,
#     print the information in the following format:
#     "Asabeneh Yetayeh lives in Finland. He is married."
print(person)

if person['is_marred'] == True:
    print(
        f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print('This person isn\'t married')
