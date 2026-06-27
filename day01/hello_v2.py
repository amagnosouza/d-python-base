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
import logging

log_level = os.environ.get("LOG_LEVEL", "WARNING").upper() # DEBUG, INFO, WARNING, ERROR, CRITICAL

# instanciando o logger
log = logging.Logger("logs.py", logging.DEBUG)

# levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
ch = logging.StreamHandler() # destino: console
ch.setLevel(log_level) # definindo o nível de log do destino

# formatacao: logging.<level>(<mensagem>)
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s l: %(lineno)d f: %(filename)s - %(message)s") # formato da mensagem
ch.setFormatter(fmt) # adicionando o formato ao destino
log.addHandler(ch) # adicionando o destino ao logger

arguments = {
    "lang": None,
    "count": 1
}

for arg in sys.argv[1:]:
    # TODO: Logging
    try:
        key,value = arg.split("=")
    except ValueError as e:
        log.error(
            "Invalid argument format: %s", arg
        )
        log.error(
            "Usage: {sys.argv[0]} --lang=<language_code> --count=<number_of_times>"
        )
        sys.exit(1)

    # LBYL (Look Before You Leap) approach to validate the argument
    key = key.lstrip("-").strip()  # Remove leading dashes
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

# EAFP (Easier to Ask for Forgiveness than Permission) approach to handle missing language
try:
    message = messages[current_lang]
except KeyError as e:
    print(f"Error: {e}")
    print(f"Invalid language: {current_lang}")
    print(f"Supported languages: {', '.join(messages.keys())}")
    sys.exit(1)

# Select message based on current language, defaulting to English
print(
    messages[current_lang] * int(arguments["count"])
)