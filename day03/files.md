# Notas de Aula: Interagindo com o Sistema de Arquivos

Guia prático comparativo entre comandos do terminal Linux e implementações em Python utilizando as bibliotecas `os`, a função `open()` clássica e `pathlib`.

---

## 1. Operações básicas de sistema de arquivos

### Criar uma pasta

- Linux:

```bash
mkdir pasta1
```

- Python (`os`):

```python
import os
os.mkdir("pasta2")
```

### Acessar uma pasta

- Linux:

```bash
cd pasta1
```

- Python (`os`):

```python
import os
os.chdir("pasta2")
```

### Exibir o diretório de trabalho atual

- Linux:

```bash
pwd
# Exemplo de saída: /path/pasta1
```

- Python (`os`):

```python
import os
os.path.abspath(os.curdir)
# Exemplo de saída: /path/pasta2
```

### Criar um arquivo em branco

- Linux:

```bash
touch arquivo.txt
```

- Python:

```python
open("arquivo.txt", "w")
```

### Listar arquivos e diretórios

- Linux:

```bash
ls
# Exemplo de saída: arquivo.txt
```

- Python (`os`):

```python
import os
os.listdir('.')
# Exemplo de saída: ['arquivo.txt']
```

### Escrever em um arquivo

- Linux:

```bash
echo "Hello" >> arquivo.txt
```

> Nota: no Linux, `>` substitui o conteúdo (modo `w`) e `>>` faz append (modo `a`).

- Python (modo append):

```python
with open("arquivo.txt", "a") as arquivo:
    arquivo.write("Hello\n")
```

### Ler o conteúdo de um arquivo

- Linux:

```bash
cat arquivo.txt
# Saída: Hello
```

- Python:

```python
with open("arquivo.txt", "r") as f:
    print(f.read())
# Saída: 'Hello\n'
```

---

## 2. Boas práticas e dicas úteis em Python

### Gerenciador de contexto (`with`)

O gerenciador de contexto garante o fechamento do arquivo automaticamente, evitando a necessidade de chamar `.close()` explicitamente.

```python
with open("arquivo.txt", "a") as arquivo:
    arquivo.write("Hello")
# Fora do bloco, o arquivo já está fechado.
```

### Criar diretórios em cadeia

`os.mkdir` falha se os diretórios pai não existirem. Use `os.makedirs` com `exist_ok=True` para criar toda a árvore.

```python
import os
os.makedirs("um/outro/maisoutro", exist_ok=True)

print(os.listdir("um"))        # -> ['outro']
print(os.listdir("um/outro"))  # -> ['maisoutro']
```

### Leitura eficiente de arquivos grandes

Evite usar `.read()` ou `.readlines()` em arquivos muito grandes (ex.: 20 GB). Leia linha a linha:

```python
with open("arquivo_grande.txt", "r") as f:
    for linha in f:
        print(linha, end='')
```

### Escrever múltiplas linhas agrupadas

```python
texto = [
    "Este é um texto",
    "cada item desta lista",
    "é uma linha no arquivo",
]

with open("arquivo.txt", "a") as arquivo:
    arquivo.writelines("\n".join(texto) + "\n")
```

### Ler múltiplas linhas para uma lista (arquivos pequenos)

```python
linhas = open("arquivo.txt").readlines()
# Ex.: ['Este é um texto\n', 'cada item desta lista\n', 'é uma linha no arquivo\n']
```

## 3. Manipulação de caminhos com `os.path`

```python
import os

# Juntando caminhos de forma segura
os.path.join("pasta2", "pasta3", "arquivo.txt")
# -> 'pasta2/pasta3/arquivo.txt'

# Caminho absoluto
os.path.abspath(os.path.join("pasta2", "pasta3", "arquivo.txt"))
# Ex.: '/home/user/pasta2/pasta3/arquivo.txt'

# Diretório atual absoluto
os.path.abspath(os.curdir)
# Ex.: '/tmp/pasta2/foo/'
```

## 4. Modernizando com `pathlib` (Python 3+)

`pathlib` fornece uma API orientada a objetos e legível para operações de arquivo e caminho.

```python
from pathlib import Path

# Criar pasta (equivalente a makedirs)
Path("pasta3").mkdir(parents=True, exist_ok=True)

# Criar arquivo (touch)
Path("pasta3/arquivo.txt").touch()

# Escrever texto (gera e fecha o arquivo automaticamente)
Path("pasta3/arquivo.txt").write_text("Bruno")

# Ler o conteúdo
conteudo = Path("pasta3/arquivo.txt").read_text()
print(conteudo)  # 'Bruno'
```

### Sobrecarga do operador `/`

Permite concatenar caminhos de forma intuitiva:

```python
from pathlib import Path
caminho = Path("pasta1") / "pasta2" / Path("pasta3")
print(caminho)  # -> pasta1/pasta2/pasta3
```

### Conclusão

A escolha entre `os`/`os.path` e `pathlib` depende da preferência. Ambos fazem o trabalho; `pathlib` tende a ser mais legível.

## 5. Exercícios propostos

- Histórico da calculadora: salvar o histórico de cálculos de `infixcalc.py` em um arquivo passado pelo parâmetro `--logfile`.
- Automação de e-mails: alterar `interpolacao.py` para ler e-mails dinamicamente a partir de um arquivo `emails.txt` no momento do envio.
- Bloco de notas CLI (`note.py`): criar uma ferramenta de linha de comando:

  - `python3 note.py write`: perguntar os campos título, tag e texto; salvar como nova linha em `notas.txt` em formato TSV (tab-separated values).
  - `python3 note.py read`: exibir todas as notas; aceitar `--tag=geral` para filtrar por tag.

---

Fim das notas.