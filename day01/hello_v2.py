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
    python3 hello_v1.py

Output (example):
    Hello, World!
"""
# Metadata about the script
__version__ = "0.1.3"
__author__  = "Alexandre Souza"

import os
import sys

arguments = {
    "lang": None,
    "count": 1
}

for arg in sys.argv[1:]:
    # TODO fix ValueError: not enough values to unpack (expected 2, got 1) if arg does not contain "="
    try:
        key,value = arg.split("=")
    except ValueError as e:
        print(f"Error: {e}")
        print(f"Invalid argument: {arg}")
        print(f"Usage: {sys.argv[0]} --lang=<language_code> --count=<number_of_times>")
        sys.exit(1)

    key = key.lstrip("--").strip()  # Remove leading dashes
    value = value.strip()
    if key not in arguments:
        print(f"Invalid argument: {key}")
        sys.exit()
    #print(key, value) # Debug print
    arguments[key] = value

current_lang = arguments["lang"]
if current_lang is None:
    current_lang = os.getenv("LANG", "pt_BR")[:5]  # Default language (first 5 chars)

# Messages mapping for supported languages
messages = {
    "pt_BR": "Olá, Mundo!",
    "fr_FR": "Bonjour, le Monde!",
    "es_ES": "¡Hola, Mundo!",
    "de_DE": "Hallo, Welt!",
    "en_US": "Hello, World!",
}

# Select message based on current language, defaulting to English
print(
    messages[current_lang] * int(arguments["count"])
)