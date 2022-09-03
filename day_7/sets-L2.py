###########################################
##  Day 7: 30 Days of python programming  #
###########################################

# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1 - Join A and B
C = A.union(B)
print(C)

# 2 - Find A intersection B
print(C)

# 3 - Is A subset of B
D = A.issubset(B)
print(D)

# 4 - Are A and B disjoint sets
E = A.isdisjoint(B)
print(E)

# 5 - Join A with B and B with A
F = A.union(B)
G = B.union(A)
print(F == G)

# 6 - What is the symmetric difference between A and B
A.symmetric_difference_update(B)
print(A)

# 7 - Delete the sets completely
del A
del B
