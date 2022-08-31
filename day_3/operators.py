###########################################
##  Day 3: 30 Days of python programming  #
###########################################

# 1 - Declare your age as integer variable
age = 52

# 2 - Declare your height as a float variable
height = 172.0

# 3 - Declare a variable that store a complex number
complex_num = 1 + 1j

# 4 - Write a script that prompts the user to enter base and height of the triangle 
#     and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input('Enter the base: '))
height = int(input('Enter the height: '))

print('The area of the triangle is', int(base * height / 2))

# 5 - Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
#     Calculate the perimeter of the triangle (perimeter = a + b + c).
sideA = int(input('Enter the side a: '))
sideB = int(input('Enter the side b: '))
sideC = int(input('Enter the side c: '))

print('The perimeter of the triangle:', int(sideA + sideB + sideC))

# 6 - Get length and width of a rectangle using prompt. 
#     Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('Enter the length: '))
width = int(input('Enter the width: '))

print('The area of the rectangle is', length * width)
print('The perimeter of the rectangle is', 2 * (length * width))

# 7 - Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and 
#     circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.1410
radius = int(input('Enter the radius: '))

print('The area of the circle is', pi * radius * radius)
print('The perimeter of the circle is', 2 * pi * radius)

# 8 - Calculate the slope, x-intercept and y-intercept of y = 2x -2
print('The slope of line y = 2x -2 is 2')
print('The x-intecepte is the point (1, 0)')
print('The y-intecepte is the point (0, -2)')

# 9 - Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance 
#     between point (2, 2) and point (6,10)
import math

slope = (10 - 2) / (6 - 2)
euclididean_distance = math.sqrt((10 - 2) ** 2 + (6 - 2) ** 2)
print('The slope is', slope)
print('The eucliddean distance between point (2, 2) and (6, 10) is', euclididean_distance)

# 10 - Compare the slopes in tasks 8 and 9.
is_equal = True

if is_equal:
    print('The slopes in tasks 8 and 9 are equal')

# 11 - Calculate the value of y (y = x^2 + 6x + 9). 
#      Try to use different x values and figure out at what x value y is going to be 0.
delta = 6 ** 2 - (4 * 1 * 9)

if delta == 0:
    print('The equation (y = x^2 + 6x + 9) has 1 solution:',  - 6 / 2)

# 15 - Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print('Do "dragon" and "python" have the same number of letters:', len('dragon') == len('python'))

# 16 - Find the length of the text python and 
#      convert the value to float and convert it to string
text_length = len("python")
print('The length of text \'Python\' is', float(text_length))
print('The length of text \'Python\' is ' + str(text_length))

# 17 - Even numbers are divisible by 2 and the remainder is zero. 
#      How do you check if a number is even or not using python?
print('Is 4 even:', 4 % 2 == 0)
print('Is 3 even:', 3 % 2 == 0)

# 18 - Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print('Is floor division of 7 by 3 is equal to int converted value of 2.7:', 7 // 3 == int(2.7))

# 19 - Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# 20 - Check if int('9.8') is equal to 10
# print(int('9.8') == 10)

# 21 - Writ a script that prompts the user to enter hours and rate per hour. 
#      Calculate pay of the person?
hours = input('Enter hours: ')
rate = input('Enter rate per hour: ')

print('Your weekly earning is', int(hours) * int(rate))

# 22 - Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. 
#      Assume a person can live hundred years
years = int(input('Enter number of years you have lived: '))
seconds = 60 * 60 * 24 * 365 * years

print('You have lived for ' + str(seconds) + ' seconds.')

# 23 - Write a Python script that displays the following table
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')


