#!/usr/bin/env python3
"""Escola
"""
__version__ = "1.0"
__author__  = "Alexandre Souza"

produto_nome = "Caneta"
produto_preco = 2.50
produto_estoque = 100
produto_categoria = "Material Escolar"
produto_codigo = "C12345"
produto_descricao = "Caneta esferográfica azul, ideal para escrita diária."
produto_fabricante = "Faber-Castell"
produto_peso = 0.02  # Peso em kg
produto_dimensoes = (14.0, 1.0, 1.0)  # Dimensões em cm (comprimento, largura, altura)

compra = ("Alexandre", produto_nome, 10, produto_preco)

print(compra)
print(f"O cliente {compra[0]} comprou {compra[2]} unidades de {compra[1]} por R${compra[3]:.2f} cada.")