###########################################
##  Day 9: 30 Days of python programming  #
###########################################

# Exercises: Level 1

# 1 - Get user input using input(“Enter your age: ”).
#     If user is 18 or older, give feedback: You are old enough to drive.
#     If below 18 give feedback to wait for the missing amount of years.
age = int(input("Enter your age: "))

if (age >= 18):
    print("You are old enough to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# 2 - Compare the values of my_age and your_age using if … else.
#     Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
#     You can use a nested condition to print 'year' for 1 year difference in age,
#     'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 54
your_age = int(input("Enter your age: "))

if my_age == your_age:
    print("We are the same age")
elif my_age > your_age:
    print(f"I am {my_age - your_age} yers older than you")
else:
    print(f"You are {your_age - my_age} yers older than me")

# 3 - Get two numbers from the user using input prompt.
#     If a is greater than b return a is greater than b,
#     if a is less b return a is smaller than b, else a is equal to b.
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a == b:
    print(f"{a} is equal to {b}")
elif a > b:
    print(f"{a} is geater than {b}")
else:
    print(f"{a} is lesser than {b}")
