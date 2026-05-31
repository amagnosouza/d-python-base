#!/usr/bin/env python3
"""
Exibe relátorio de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequenta por cada uma das atividades oferecidas pela escola.
"""
# Metadata about the script
__version__ = "1.3"
__author__  = "Alexandre Souza"

# Dados
sala1 = ["Maria", "João", "Ana", "Pedro", "Lucas", "Sofia"]
sala2 = ["Carla", "Rafael", "Beatriz", "Gustavo", "Fernanda", "Bruno"]

aula_ingles = ["Maria", "Carla", "Rafael", "Ana", "Gustavo"]
aula_musica = ["João", "Beatriz", "Pedro", "Fernanda", "Sofia"]
aula_artes = ["Lucas", "Bruno", "Ana", "Gustavo", "Sofia"]

salas = {
    "Sala 1": set(sala1),
    "Sala 2": set(sala2),
}

# Listas de atividades e suas respectivas aulas
atividades = {
    "Ingles": set(aula_ingles),
    "Musica": set(aula_musica),
    "Artes": set(aula_artes)
}

# Listar alunos em cada atividade por sala usando conjuntos para otimizar a busca
for nome_atividade, participantes in atividades.items():
    print(f"Atividade {nome_atividade}")
    for nome_sala, alunos in salas.items():
        inscritos = alunos & participantes
        print(f"{nome_sala}: {sorted(inscritos)}")
    print("-" * 30)  # Separador para melhor visualização