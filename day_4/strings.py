###########################################
##  Day 4: 30 Days of python programming  #
###########################################

# 1 - Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
from cmath import sin


single_string = 'Thirty '
single_string += 'Days '
single_string += 'Of '
single_string += 'Python'
print(single_string)

# 2  - Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
single_string = 'Coding '
single_string += 'For '
single_string += 'All'
print(single_string)

# 3 - Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding for All'

# 4 - Print the variable company using print().
print(company)

# 5 - Print the length of the company string using len() method and print().
print(len(company))

# 6 - Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7 - Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8 - Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())

# 9 - Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# 10 - Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))

# 11 - Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# 12 - Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace('All', 'Everyone'))

# 13 - Split the string 'Coding For All' using space as the separator (split()).
print(company.split(' '))

# 14 - "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
our_string = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(our_string.split(', '))

# 15 - What is the character at index 0 in the string Coding For All.
print(company[0])

# 16 - What is the last index of the string Coding For All.
print(len(company) - 1)

# 17 - What character is at index 10 in "Coding For All" string.
print(company[10])

# 18 - Create an acronym or an abbreviation for the name 'Python For Everyone'.
company = 'Python For Everyone'
acronym = ''
for item in company.split(' '):
    acronym += item[0]

print(acronym)

# 19 - Create an acronym or an abbreviation for the name 'Coding For All'.
company = 'Coding For All'
acronym = ''
for item in company.split(' '):
    acronym += item[0]

print(acronym)

# 20 - Use index to determine the position of the first occurrence of C in Coding For All.
print(company.rfind('C'))

# 21 - Use index to determine the position of the first occurrence of F in Coding For All.
print(company.rfind('F'))

# 22 - Use rfind to determine the position of the last occurrence of l in Coding For All People.
company = 'Coding For All People'
print(company.rfind('l'))

# 23 - Use index or find to find the position of the first occurrence of the word 'because' in
#      the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 24 - Use rindex to find the position of the last occurrence of the word because in
#      the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind('because'))

# 25 - Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.find('because'):(
    sentence.rfind('because')) + len('because')])

# 26 - Find the position of the first occurrence of the word 'because' in
# the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 27 - Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.find('because'):(
    sentence.rfind('because')) + len('because')])

# 28 - Does 'Coding For All' start with a substring Coding?
company = 'Coding For All'
print(company[0:len('Coding')] == 'Coding')

# 29 - Does 'Coding For All' end with a substring coding?
company = 'Coding For All'
print(company[-(len('coding')):] == 'coding')

# 30 - '   Coding For All      '  , remove the left and right trailing spaces in the given string.
company = '   Coding For All      '
print(company.strip())

# 31 - Which one of the following variables return True when we use the method isidentifier():
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32 - The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
our_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(', '.join(our_list))

# 33 - Use the new line escape sequence to separate the following sentences.
str1 = 'I am enjoying this challenge.'
str2 = 'I just wonder what is next.'
print(str1 + '\n' + str2)

# 34 - Use a tab escape sequence to write the following lines.
tab1 = 'Name\tAge\tCountry\tCity'
tab2 = 'Asabeneh\t250\tFinland\tHelsinki'
print(tab1.expandtabs(9))
print(tab2.expandtabs(9))

# 35 - Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {:.0f} meters square.'.format(radius, area))

# 36 - Make the following using string formatting methods:
a = 8
b = 6

print(f'{a} + {b} = {a + b:5}')
print(f'{a} + {b} = {a - b:5}')
print(f'{a} + {b} = {a * b}')
print(f'{a} + {b} = {a / b:.2f}')
print(f'{a} + {b} = {a % b}')
print(f'{a} + {b} = {a // b}')
print(f'{a} + {b} = {a ** b:e}')
