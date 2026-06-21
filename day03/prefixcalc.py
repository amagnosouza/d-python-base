#!/usr/bin/env python3
"""Prefix calculator program in Python
[operation] [number1] [number2]
Operations supported: 
sum -> +
sub -> -
mul -> *
div -> /

Example:
    python3 prefixcalc.py sum 5 3
Output:
    8
    python3 prefixcalc.py mul 4 6
Output:
    24
    python3 prefixcalc.py div 10 2
Output:
    5
Os resultados serão salvos em um arquivo chamado "results.txt" no mesmo diretório do script.
"""
__version__ = "0.1.1"
__author__  = "Alexandre Souza"

import os
import sys

arguments = sys.argv[1:]
if len(arguments) != 3:
    print("Usage: prefixcalc.py [operation] [number1] [number2]")
    sys.exit(1)

operation, num1_str, num2_str = arguments
num1 = int(num1_str)
num2 = int(num2_str)

if operation == "sum":
    result = num1 + num2
elif operation == "sub":
    result = num1 - num2
elif operation == "mul":
    result = num1 * num2
elif operation == "div":
    result = num1 / num2
else:
    print("Invalid operation")
    sys.exit(1)

path = os.curdir
filename = "results.txt"
filepath = os.path.join(path, filename)

with open(filepath, "a") as file_:
    file_.write(f"{operation}, {num1}, {num2} = {result}\n")

sys.exit(0)