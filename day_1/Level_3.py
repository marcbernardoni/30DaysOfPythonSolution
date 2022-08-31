"""
    Write an example for different Python data types such as Number
    (Integer, Float, Complex), String, Boolean, List, Tuple, 
    Set and Dictionary.
"""
from math import sqrt


print(type(10))             # Integer (int)
print(type(3.14))           # Float (float)
print(type(1 + 3j))         # Complex (complex)

print(type('Asabeneth'))    # String (str)
print(type(True))           # Boolean (bool)

print(type([1, 2, 3]))              # List (list)
print(type((9.8, 3.14, 2.7)))       # Tuple (tuple)
print(type({9.8, 3.14, 2.7}))       # Set (set)
print(type({'name': 'Asabeneh'}))   # Dictionary (dict)

    # Find an Euclidian distance between (2, 3) and (10, 8)
distance = sqrt(((10 - 2) ** 2) + ((8 - 3) ** 2))
print(distance)
