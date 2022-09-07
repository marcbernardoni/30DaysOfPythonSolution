############################################
##  Day 11: 30 Days of python programming  #
############################################

# Exercises: Level 1

# 1 - Declare a function add_two_numbers. It takes two parameters and it returns a sum.

# 2 - Area of a circle is calculated as follows: area = π x r x r.
#     Write a function that calculates area_of_circle.

# 3 - Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#     Check if all the list items are number types. If not do give a reasonable feedback.

# 4 - Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
#     Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

# 5 - Write a function called check-season, it takes a month parameter
#     and returns the season: Autumn, Winter, Spring or Summer.

# 6 - Write a function called calculate_slope which return the slope of a linear equation

# 7 - Quadratic equation is calculated as follows: ax² + bx + c = 0.
#     Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

# 8 - Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

# 9 - Declare a function named reverse_list. It takes an array as a parameter
#      and it returns the reverse of the array (use loops).

# 10 - Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

# 11 - Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

# 12 -  Declare a function named remove_item. It takes a list and an item parameters.
#       It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

# 13 - Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.


def sum_of_numbers(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum


print(sum_of_numbers(5))       # 15
print(sum_of_numbers(10))      # 55
print(sum_of_numbers(100))     # 5050

# 14 - Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

# 15 - Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
