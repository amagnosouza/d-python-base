#!usr/bin/env python3
"""
Tabuada program in Python.
How to run:
    python3 tabuada.py
Output:
    Tabuada do 1:
    1 x 1 = 1
    1 x 2 = 2
    ...
    Tabuada do 2:
    2 x 1 = 2
    2 x 2 = 4
    ...
    Tabuada do 9:
    9 x 1 = 9
    9 x 2 = 18
    ...
"""
# Metadata about the script
__version__ = "1.0"
__author__  = "Alexandre Souza"

# Tabuada program in Python.
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # List of numbers from 1 to 10.
numeros = list(range(1, 11)) # Range of numbers from 1 to 10.

for numero in numeros:
    print("Tabuada do:", numero) # Print the header for the current number.
    for numero2 in numeros:
        print(numero * numero2)
    print("----------")