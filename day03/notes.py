#!/usr/bin/env python3
"""Bloco de Notas
$ notes.py new "Minha Nota"
"Tag: tech"
"Notas geral sobre carreria de tecnologia"

$ notes.py read --tag=tech
...
...

"""
__version__ = "0.1.0"
import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Uso: notes.py <comando> [opções]")
    sys.exit(1)

cnds = ("read", "new")
if arguments[0] not in cnds:
    print(f"Comando inválido: {arguments[0]}")
    sys.exit(1)

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"{title}: {title}")
            print(f"{text}: {text}")
            print(f"-"*40)
            print()

if arguments[0] == "new":
    title = arguments[1]
    text = [
        f"{title}",
        input("Tag: ").strip(),
        input("Text: \n").strip(),
    ]
    with open(filepath, "a") as f:
        f.write("\t".join(text) + "\n")