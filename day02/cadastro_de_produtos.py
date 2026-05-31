#!/usr/bin/env python3
"""Escola
"""
__version__ = "1.0"
__author__  = "Alexandre Souza"

produto = {
    "nome": "Caneta",
    "preco": 2.50,
    "cores": ["azul", "preta", "vermelha"],
    "estoque": 100,
    "categoria": "Material Escolar",
    "codigo": "C12345",
    "descricao": "Caneta esferográfica azul, ideal para escrita diária.",
    "fabricante": "Faber-Castell",
    "peso": 0.02,
    "dimensoes": {
        "comprimento": 14.0,
        "largura": 1.0,
        "altura": 1.0
    }
}

cliente = {
    "nome": "Alexandre Souza"
}
compra = {
    "cliente": cliente["nome"],
    "produto": produto["nome"],
    "quantidade": 10,
    "preco_unitario": produto["preco"],
}
# Calcula o total da compra
compra["total"] = compra["quantidade"] * compra["preco_unitario"]
# Exibe o resumo da compra
print(f"O cliente {compra['cliente']} comprou {compra['quantidade']} unidades de {compra['produto']} por R${compra['preco_unitario']:.2f} cada." f"O total da compra é R${compra['total']:.2f}.")