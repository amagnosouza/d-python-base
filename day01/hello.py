#!/usr/bin/env python3
"""
Hello World Multi langage program in Python.

Depending on the language configured in the environment, the message 
will change.

How to run:
Configure the environment variable LANG to the desired language (en_US.UTF-8 
for English, fr_FR.UTF-8 for French, etc.) and then run this script.

Example:
    export LANG=en_US.UTF-8
    python3 hello.py

Output:
    Hello World!
"""
# Metadata about the script
__version__ = "1.0"
__author__  = "Alexandre Souza"

import os

#current_lang = "en_US" # Default language
current_lang = os.getenv("LANG", "pt_BR")[:5] # Default language
# snake_case is used for variable names in Python.

# A simple "Hello, World!" program in Python. | This is a comment.
msg = "Hello, World!" # This variable holds the message to be printed.

if current_lang == "pt_BR":
    msg = "Olá, Mundo!" # If the language is Portuguese, change the message.
elif current_lang == "fr_FR":
    msg = "Bonjour, le Monde!" # If the language is French, change the message.


print(msg) # This line prints the value of the variable `msg` to the console.