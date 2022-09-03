###########################################
##  Day 7: 30 Days of python programming  #
###########################################

# Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1 - Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
if len(age) >= len(age_st):
    print(f'The list {age} is bigger than the set {age_st}')
else:
    print(f'The set {age_st} is bigger than the list {age}')

# 2 - Explain the difference between the following data types: string, list, tuple and set
###
# list :    - is a datatype
#           - are mutable
#           - can store any type of element
#
# tuple :   - is immutable
#           - can't be change or replaced
#           _ can store any type of element
#
# set :     - is an unordered collection of elements
#           - the order of the elements is not fixed
#           - is mutable, however, only immutable objects can be stored in it

# 3 - I am a teacher and I love to inspire and teach people.
#     How many unique words have been used in the sentence?
#     Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people"
words = list(sentence.split(' '))
print(f'the sentence "{sentence}" is composed of {len(words)} words')
unique_words = set(words)
print(f'But ther are only {len(unique_words)} unique words ({unique_words})')
