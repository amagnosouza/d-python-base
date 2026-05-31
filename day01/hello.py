#!/usr/bin/env python3
"""
Hello World multilanguage program in Python.

Depending on the language configured in the environment, the output
message will change accordingly.

How to run:
Set the environment variable `LANG` to the desired language
(for example `en_US.UTF-8` for English, `fr_FR.UTF-8` for French)
and run this script.

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

current_lang = os.getenv("LANG", "pt_BR")[:5]  # Default language (first 5 chars)

# A simple "Hello, World!" program. `msg` holds the message to print.
msg = "Hello, World!"

if current_lang == "pt_BR":
    msg = "Olá, Mundo!"
elif current_lang == "fr_FR":
    msg = "Bonjour, le Monde!"
elif current_lang == "es_ES":
    msg = "¡Hola, Mundo!"
elif current_lang == "de_DE":
    msg = "Hallo, Welt!"

print(msg)