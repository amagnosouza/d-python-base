**Conjuntos — `set` em Python**

Visão geral
-----

`set` representa um conjunto matemático: itens únicos, mutáveis e com operações de teoria dos conjuntos.

Criação
-----

```python
# A partir de um iterável
iteravel = [1, 2, 3]
set(iteravel)

# Literais
{1, 2, 3, 4}

# Desempacotando um iterável
{*iteravel}
```

Operações básicas
-----

```python
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

# União
conjunto_a | conjunto_b        # {1,2,3,4,5,6,7,8}

# Interseção
conjunto_a & conjunto_b        # {4,5}

# Diferença
conjunto_a - conjunto_b        # {1,2,3}

# Diferença simétrica
conjunto_a ^ conjunto_b        # {1,2,3,6,7,8}
```

Exemplo de uso prático
-----

Pense em redes sociais: `A` = pessoas que você segue, `B` = pessoas que te seguem. `A - B` mostra quem você segue e não te segue de volta; `A & B` mostra seguidores em comum.

Performance
-----

`set` é implementado sobre uma tabela de hash. Operações de busca (`in`) e inserção/remover têm complexidade média O(1), enquanto buscas em listas são O(n).

```python
if "alfredo" in usuarios_set:   # muito rápido
	...

if "alfredo" in usuarios_list:  # pode ser lento para listas grandes
	...
```

Mutabilidade e métodos úteis
-----

```python
a = set([1, 2, 3])
a.add(4)
a.remove(1)
a.discard(10)   # não lança erro se não existir
a.pop()         # remove e retorna um elemento arbitrário
```

Deduplicação
-----

`set` é excelente para eliminar duplicatas:

```python
lista = [1, 2, 2, 3, 3, 3]
set(lista)   # {1, 2, 3}
```

Limitações
-----

- Não preservam ordem de inserção; a ordem de iteração é arbitrária e pode variar entre execuções/versões do Python.
- Não suportam indexação/subscrição — `conjunto[0]` gera `TypeError`.

```python
conjunto = {4, 5, 6}
4 in conjunto        # True
list(conjunto)[0]    # converte para lista para indexar
```

Exemplo prático completo
-----

```python
seguidores = {"joao", "maria", "ana"}
seguidos = {"maria", "carlos"}

nao_seguem_de_volta = seguidos - seguidores
seguidores_em_comum = seguidores & seguidos
```

Quando usar
-----

- Use `set` para testar pertinência rápida (`in`), remover duplicatas e aplicar operações de conjuntos.
- Use listas ou tuplas quando precisar de ordem ou indexação.

Fim

