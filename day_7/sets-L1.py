###########################################
##  Day 7: 30 Days of python programming  #
###########################################

# Exercises: Level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1 - Find the length of the set it_companies
print(len(it_companies))

# 2 - Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3 - Insert multiple IT companies at once to the set it_companies
it_companies.update(['Sun', 'Thomson'])
print(it_companies)

# 4 - Remove one of the companies from the set it_companies
it_companies.remove('Sun')
print(it_companies)

# 5 - What is the difference between remove and discard

# These 2 methods allow you to remove an element from a set,
# however the remove() method will throw an error if the element
# to be deleted does not exist unlike the discard() method
