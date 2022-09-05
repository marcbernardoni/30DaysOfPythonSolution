###########################################
##  Day 9: 30 Days of python programming  #
###########################################

# Exercises: Level 2

# 1 - Write a code which gives grade to students according to theirs scores:
score = int(input("Please provide the student's score: "))

if score <= 100 and score >= 80:
    print("The student's degree is A")
elif score < 80 and score >= 70:
    print("The student's degree is B")
elif score < 70 and score >= 60:
    print("The student's degree is C")
elif score < 60 and score >= 50:
    print("The student's degree is D")
elif score < 50 and score >= 0:
    print("The student's degree is F")
else:
    print("The student's score must be between 0 and 100")

# 2 - Check if the season is Autumn, Winter, Spring or Summer.
#     If the user input is: September, October or November, the season is Autumn.
#     December, January or February, the season is Winter.
#     March, April or May, the season is Spring
#     June, July or August, the season is Summer
month = input("Enter your favorite month: ")

if month in ['September', 'October', 'November']:
    print(f"The month of {month} is in Autumn")
elif month in ['December', 'January', 'February']:
    print(f"The month of {month} is in Winter")
elif month in ['March', 'April', 'May']:
    print(f"The month of {month} is in Spring")
elif month in ['June', 'July', 'May']:
    print(f"The month of {month} is in Summer")
else:
    print("Please enter a month that exists")

# 3 - The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
fruit = input("Please submit a fruit: ")

if fruit in fruits:
    print(f"the {fruit} already exist in the list {fruits}.")
else:
    print(f"This fruit: {fruit} is not yet in our list of fruit")
    fruits.append(fruit)
    fruits.sort()
    print(f"I add this fruit in our list wich becomes {fruits}.")
