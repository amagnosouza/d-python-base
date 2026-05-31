#!/usr/bin/env python3
"""
Multiplication table program in Python.
How to run:
    python3 tabuada.py
Output example:
Multiplication table for 1:
    1 x 1 = 1
    1 x 2 = 2
    ...
#########################
Multiplication table for 2:
    2 x 1 = 2
    2 x 2 = 4
    ...
#########################
Multiplication table for 9:
    9 x 1 = 9
    9 x 2 = 18
    ...
"""
# Metadata about the script
__version__ = "1.1"
__author__  = "Alexandre Souza"

# Multiplication table program in Python.
numeros = list(range(1, 11))  # Numbers from 1 to 10.

for n1 in numeros:
    print("{:-^30}".format(f"Multiplication table for {n1}"))
    for n2 in numeros:
        result = n1 * n2
        print("{:^20}".format(f"{n1} x {n2} = {result}"))
    print("#" * 20 + "\n")