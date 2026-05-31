**Dados compostos — Tuplas e Listas**

Tuplas
-----

Tuplas são sequências imutáveis, usadas quando os valores não devem mudar.

Exemplos:
```python
feira = ("laranja", "morango", "banana")
coord = (140, 200, 9)
```

Desempacotamento:
```python
laranja, morango, banana = feira
x, y, z = coord
```

Ignorar valores durante o desempacotamento:
```python
x, *_ = coord        # pega só o primeiro
x, *_, y = coord     # pega primeiro e último
```

Acessando elementos e tamanho:
```python
len(coord)    # 3
coord[0]      # 140
coord[1:]     # (200, 9)
```

Listas
-----

Listas são mutáveis e oferecem métodos para adicionar, remover e contar elementos.

Criação:
```python
lista_vazia = []
cores = ["red", "green", "blue"]
# ou
cores = list()
```

Adicionar elementos:
```python
cores.append("purple")       # ao final
cores.insert(0, "red")       # numa posição específica (0 = início)
cores.extend(["yellow"])     # estende in-place
cores += ["pink"]            # operador += também estende
```

Remover e obter elementos:
```python
cores.remove("green")  # remove a primeira ocorrência
ultimo = cores.pop()     # remove e retorna o último
```

Outras operações úteis:
```python
len(cores)               # tamanho
cores[0]                 # acessar por índice
red, green, blue = cores # desempacotamento (se o tamanho permitir)
nova = cores + ["black"]# concatena criando nova lista
cores.count("green")    # conta ocorrências
```

Dica rápida
-----

- Use tuplas quando os valores não devem mudar.
- Use listas para coleções mutáveis e com muitas inserções/remoções.

Exemplo prático completo:
```python
feira = ("laranja", "morango", "banana")
frutas = list(feira)          # transformar tupla em lista
frutas.append("uva")
print(frutas)                 # ['laranja', 'morango', 'banana', 'uva']
```