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
__version__ = "0.1.1"
__author__  = "Alexandre Souza"

import os

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
msg = messages.get(current_lang, "Hello, World!")

print(msg)