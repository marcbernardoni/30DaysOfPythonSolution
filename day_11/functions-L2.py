############################################
##  Day 11: 30 Days of python programming  #
############################################
import math

# Exercises: Level 2

# 1 - Declare a function named evens_and_odds .
#     It takes a positive integer as parameter
#     and it counts number of evens and odds in the number.
from operator import is_
from sre_constants import RANGE
from statistics import StatisticsError, mean, median, mode, variance


def even_and_odds(num):
    """
    Count  the number of even and ood numbers in the number

    Args:
        num (int): number oparameter

    Returns:
        list: number of the even and the odd numbers
    """
    odd = 0
    even = 0

    for i in range(num + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


print('\n')
print(f'The number of evens in range 100 are : {even_and_odds(100)[0]}')
print(f'The number of oddss in range 100 are : {even_and_odds(100)[1]}')

# 2 - Call your function factorial,
#     it takes a whole number as a parameter and it return a factorial of the number


def factorial(n):
    factor = 1
    for i in range(1, n + 1):
        factor *= i
    return factor


print('\n')
print(f'The factorial of 2 is {factorial(2)}')
print(f'The factorial of 3 is {factorial(3)}')
print(f'The factorial of 4 is {factorial(4)}')
print(f'The factorial of 10 is {factorial(10)}')


# 3 - Call your function is_empty,
#     it takes a parameter and it checks if it is empty or not
def is_empty(test=''):
    print(test)
    if test == '':
        print('The paramenter is empty')
    else:
        print('The paramenter is not empty')


print('\n')
is_empty()
is_empty(list)
is_empty(set)
is_empty(dict)


# 4 - Write different functions which take lists.
#     They should calculate_mean, calculate_median, calculate_mode, calculate_range,
#     calculate_variance, calculate_std (standard deviation).
def calculate(liste):
    stats = {
        'mean': '',
        'median': '',
        'mode': '',
        'range': '',
        'variance': '',
        'standart deviation': ''
    }

    stats['median'] = median(liste)
    stats['mean'] = round(mean(liste), 2)
    stats['mode'] = mode(liste)
    stats['range'] = round(max(liste) - min(liste), 2)
    stats['variance'] = round(variance(liste), 2)
    stats['standart deviation'] = round(math.sqrt(variance(liste)), 2)

    return stats


l1 = [24.1, 25.0, 25.2, 25.6, 25.7, 26.1, 27.8]

print(calculate(l1))
