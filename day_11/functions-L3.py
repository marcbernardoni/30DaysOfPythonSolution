############################################
##  Day 11: 30 Days of python programming  #
############################################

# Exercises: Level 3

# 1 - Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    r = int(n ** 0.5)
    f = 5

    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


print(f'Is 5003 prime ? {is_prime(5003)}')


# 2 - Write a functions which checks if all items are unique in the list.
def is_unique(liste):
    if len(liste) > len(set(liste)):
        print('There is doublons')
    else:
        print('All elements are unique')


l1 = [1, 1, 1, 2, 3, 4, 5, 6, 2]
l2 = [1, 2, 3, 4, 5, 6]

print('\n')
is_unique(l1)
is_unique(l2)

# 3 - Write a function which checks if all the items of the list
#     are of the same data type.


def is_same_type(liste):
    res = True
    for el in liste:
        if not isinstance(el, type(liste[0])):
            res = False
            break
    return res


l1 = [1, 2.5, 'a']
l2 = [1, 2, 3]
l3 = ['a', 1, 'b']

print('\n')
print(f'Is all element in {l1} the same type: {is_same_type(l1)}')
print(f'Is all element in {l2} the same type: {is_same_type(l2)}')
print(f'Is all element in {l3} the same type: {is_same_type(l3)}')

# 4 - Write a function which check if provided variable
#     is a valid python variable

# 5 - Go to the data folder and access the countries-data.py file.
# a - Create a function called the most_spoken_languages in the world.
#     It should return 10 or 20 most spoken languages in the world in descending order
# b - Create a function called the most_populated_countries.
#     It should return 10 or 20 most populated countries in descending order.
