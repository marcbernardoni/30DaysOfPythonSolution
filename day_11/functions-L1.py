############################################
##  Day 11: 30 Days of python programming  #
############################################
import math

# Exercises: Level 1

# 1 - Declare a function add_two_numbers.
#     It takes two parameters and it returns a sum.


def add_two_numbers(a, b):
    return a + b


print('The function "add_two_numbers" takes two parameters and it returns a sum')
print('The sum of the numbers 5 and 7 is ', add_two_numbers(5, 7))
print('The sum of the numbers 2 and 2 is ', add_two_numbers(2, 2))
print(f'The sum of the numbers 3 and 5 is {(add_two_numbers(3, 5))}')

# 2 - Area of a circle is calculated as follows: area = π x r x r.
#     Write a function that calculates area_of_circle.


def area_of_circle(r):
    return round(math.pi * r ** 2, 2)


print('\nThe function "area_of_circle" takes one parameter and it returns the area of a circle')
print(f'The area of a circle of radius 1 is {area_of_circle(1)}')
print(f'The area of a circle of radius 3 is {area_of_circle(3)}')
print(f'The area of a circle of radius 5 is {area_of_circle(5)}')

# 3 - Write a function called add_all_nums which takes arbitrary number
#     of arguments and sums all the arguments.
#     Check if all the list items are number types.
#     If not do give a reasonable feedback.


def add_all_nums(liste):
    sum = 0
    for i in range(len(liste)):
        if type(liste[i]) == 'int':
            sum += liste[i]
        else:
            sum = 'one of the element isn\'t a number'
    return sum


l1 = [1, 2, 3]
l2 = [10, 20, 5]
l3 = [5, 'apple', 30]

print('\n')
print(f'The sum of all the elements of the list {l1} is {add_all_nums(l1)}')
print(f'The sum of all the elements of the list {l2} is {add_all_nums(l2)}')
print(f'The sum of all the elements of the list {l3} is {add_all_nums(l3)}')

# 4 - Temperature in °C can be converted to °F
#     using this formula: °F = (°C x 9/5) + 32.
#     Write a function which converts °C to °F, convert_celsius_to-fahrenheit.


def convert_celcius_to_fahrenheit(t_cel):
    return (t_cel * 9 / 5) + 32


t1 = 0
t2 = 38
t3 = 100

print('\n')
print(f'The temperature {t1}°C is {convert_celcius_to_fahrenheit(t1)}°F')
print(f'The temperature {t2}°C is {convert_celcius_to_fahrenheit(t2)}°F')
print(f'The temperature {t3}°C is {convert_celcius_to_fahrenheit(t3)}°F')


# 5 - Write a function called check-season, it takes a month parameter
#     and returns the season: Autumn, Winter, Spring or Summer.
seasons = {
    'Autumn': ['September', 'October', 'Novembre'],
    'Winter': ['December', 'January', 'February'],
    'Spring': ['March', 'April', 'May'],
    'Summer': ['June', 'July', 'August']
}


def check_season(month):
    '''This function determines in which season the month is located

    Parameters
    ----------
    month : str
        The month in question

    Returns
    -------
    string
        the corresponding season
    '''
    for key in seasons:
        if month in seasons[key]:
            return key


months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'Novemnber', 'December']

print('\n')
for month in months:
    print(f'The month {month} is in {check_season(month)}')

# 6 - Write a function called calculate_slope which return
#     the slope of a linear equation


def calculate_slope(a, b):
    """Calcul the slope of a linear equation

    Args:
        a (int): coefficient a
        b (int): coefficient b

    Returns:
        int: slope of the linear equation
    """
    x1, y2 = 0, 0
    y1, x2 = int, int

    y1 = b
    x2 = - b / a

    return round((y2 - y1) / (x2 - x1), 2)


print('\n')
print(
    f'The slope of the linear equation (y = 3x + 6) is {calculate_slope(3, 6)}')
print(
    f'The slope of the linear equation (y = 2x + 6) is {calculate_slope(2, 6)}')
print(
    f'The slope of the linear equation (y = 4x + 3) is {calculate_slope(4, 3)}')

# 7 - Quadratic equation is calculated as follows: ax² + bx + c = 0.
#     Write a function which calculates solution set of a quadratic equation,
#     solve_quadratic_eqn.


def solve_quadric_eqn(a, b, c):
    """ Calculates solution set of a quadratic equation,

    Args:
        a (_type_): coefficient a
        b (_type_): coefficient b
        c (_type_): cofficient

    Returns:
        list: list of solutions
    """
    solution = []
    if a == 0:
        solution.append(-c / b)
    else:
        delta = (b * b) - (4 * a * c)
        if delta > 0:
            s1 = round((-b + math.sqrt(delta)) / (2 * a), 2)
            s2 = round((-b - math.sqrt(delta)) / (2 * a), 2)
            solution.append(s1)
            solution.append(s2)

    return solution


print('\n')
print(
    f'Solutions of the equation 3x^2 - 4x + 2 = 0 is {solve_quadric_eqn(3, -4, 2)}')
print(
    f'Solutions of the equation 2x^2 + x - 10 = 0 is {solve_quadric_eqn(2, 1, -10)}')
print(
    f'Solutions of the equation 4x^2 - 4x + 1 = 0 is {solve_quadric_eqn(-1, 2, 5)}')

# 8 - Declare a function named print_list. It takes a list as a parameter
#     and it prints out each element of the list.


def print_list(liste):
    """print elements in a list

    Args:
        list (_list_): list of elements
    """
    for idx in range(len(liste)):
        print(liste[idx], end=" ")
    print('\n')
    return


l1 = [0, 1, 2, 3, 4, 5]
l2 = ['apple', 'banana', 'mango', 'orange']
l3 = []

print('\n')
print_list(l1)
print_list(l2)
print_list(l3)

# 9 - Declare a function named reverse_list. It takes an array as a parameter
#      and it returns the reverse of the array (use loops).


def reverse_list(liste):
    """reverse list order

    Args:
        liste (_list_): original list

    Returns:
        _list_: reverse list
    """
    solution = []

    for i in range(len(liste) - 1, -1, -1):
        solution.append(liste[i])

    return solution


l1 = [1, 2, 3, 4, 5]
l2 = ['A', 'B', 'C']

print('\n')
print(f"The list {l1} become {reverse_list(l1)}")
print(f"The list {l2} become {reverse_list(l2)}")

# 10 - Declare a function named capitalize_list_items.
#      It takes a list as a parameter and it returns a capitalized list of items


def capitalize_list(liste):
    """Capitalize each element of a list

    Args:
        liste (_list_): original list

    Returns:
        list: 
    """
    solution = []

    for i in range(len(liste)):
        solution.append(liste[i].capitalize())

    return solution


l1 = ['apple', 'banana', 'mango', 'orange']
l2 = ['facebook', 'google', 'microsoft',
      'apple', 'IBM', 'oracle', 'amazon']

print('\'')
print(f'The list {l1} is capitalized ({capitalize_list(l1)})')
print(f'The list {l2} is capitalized ({capitalize_list(l2)})')

# 11 - Declare a function named add_item.
#      It takes a list and an item parameters.
#      It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]


def add_item(liste, item):
    """Add an item to a list

    Args:
        liste (list): original list
        item (): item to add to the list

    Returns:
        list: list with the new item
    """
    liste.append(item)
    return liste


print('\n')
print(add_item(food_staff, 'apple'))
print(add_item(numbers, 20))

# 12 -  Declare a function named remove_item.
#       It takes a list and an item parameters.
#       It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]


def remove_item(liste, item):
    """Remove an item from a list

    Args:
        liste (list): original list
        item (): item to remove from the list

    Returns:
        list:
    """
    if item in liste:
        liste.remove(item)

    return liste


print('\n')
print(remove_item(food_staff, 'Mango'))
print(remove_item(numbers, 20))
print(remove_item(numbers, 7))


# 13 - Declare a function named sum_of_numbers.
#      It takes a number parameter and it adds all the numbers in that range.


def sum_of_numbers(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum


print('\n')
print(sum_of_numbers(5))       # 15
print(sum_of_numbers(10))      # 55
print(sum_of_numbers(100))     # 5050

# 14 - Declare a function named sum_of_odds.
#      It takes a number parameter and
#      it adds all the odd numbers in that range.


def sum_of_odds(num):
    """adds all the odd numbers in number range

    Args:
        num (int): number oparameter

    Returns:
        int: sum of the odd numbers
    """
    sum = 0
    for i in range(num + 1):
        if i % 2 != 0:
            sum += i

    return sum


print('\n')
print(sum_of_odds(100))

# 15 - Declare a function named sum_of_even.
#      It takes a number parameter and
#      it adds all the even numbers in that - range.


def sum_of_even(num):
    """adds all the even numbers in number range

    Args:
        num (int): number oparameter

    Returns:
        int: sum of the even numbers
    """
    sum = 0
    for i in range(num + 1):
        if i % 2 == 0:
            sum += i

    return sum


print('\n')
print(sum_of_odds(100))
