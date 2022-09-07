############################################
##  Day 10: 30 Days of python programming  #
############################################

# Exercises: Level 1

# 1 - Iterate 0 to 10 using for loop, do the same using while loop.
print(f"Iterate 0 to 10 using for loop")
for i in range(11):
    print(i, end=' ')

print(f"\nIterate 1 to 10 using while loop")
count = 0
while count < 11:
    print(count, end=' ')
    count +=1

# 2 - Iterate 10 to 0 using for loop, do the same using while loop.
print(f"\nIterate 10 to 0 using for loop")
for i in range(10, -1, -1):
    print(i, end=' ')

print(f"\nIterate 10 to 0 using while loop")
count = 10
while count >= 0:
    print(count, end=' ')
    count -= 1

# 3 - Write a loop that makes seven calls to print(), 
#    so we get on the output the following triangle:
for i in range(8):
    print('#' * i)

# 4 -Use nested loops to create the following:
for i in range(9):
    print("# " * 9)

# 5 - Print the following pattern:
for i in range (11):
    print(f"{i} x {i} = {i * i}")

# 6 - Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
liste = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in liste:
    print(i) 

# 7 - Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i, end=' ')

print()
# 8 - Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i, end=' ')
