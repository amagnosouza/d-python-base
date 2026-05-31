#!/usr/bin/env python3
"""
Exibe relátorio de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequenta por cada uma das atividades oferecidas pela escola.
"""
# Metadata about the script
__version__ = "1.1"
__author__  = "Alexandre Souza"

# Dados
sala1 = ["Maria", "João", "Ana", "Pedro", "Lucas", "Sofia"]
sala2 = ["Carla", "Rafael", "Beatriz", "Gustavo", "Fernanda", "Bruno"]

aula_ingles = ["Maria", "Carla", "Rafael", "Ana", "Gustavo"]
aula_musica = ["João", "Beatriz", "Pedro", "Fernanda", "Sofia"]
aula_artes = ["Lucas", "Bruno", "Ana", "Gustavo", "Sofia"]

# Listas de atividades e suas respectivas aulas
atividades = [
    ("Ingles",aula_ingles),
    ("Musica",aula_musica),
    ("Artes",aula_artes)
]

# Listar alunos em cada atividade por sala usando conjuntos para otimizar a busca
for nome_atividade, atividade in atividades:
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)
    print(f"Atividade {nome_atividade} - Sala 1:", atividade_sala1)
    print(f"Atividade {nome_atividade} - Sala 2:", atividade_sala2)
    print("-"*30)  # Separador para melhor visualização