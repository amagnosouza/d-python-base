#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to Ask Forgiveness than Permission

try:
    name = open("name.txt", "r").readlines()
except FileNotFoundError as e: # Capture the exception and assign it to a variable
    print(f"Error: {e}") # Print the error message
    sys.exit(1) # Exit the program with a non-zero status code
else:
    print("Sucesso") # Print a success message if no exception occurred
finally:
    print("Fim do programa") # print execution message regardless of whether an exception occurred or not