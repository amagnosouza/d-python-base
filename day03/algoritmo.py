# Algoritmos
# Sequencia de instruições que resolvem um problema ou realizam uma tarefa

# Problema: Ir a padaria e comprar pão:
# Premissa: Padaria abre fds: até 12h, semana até 19h feriado(exceto Natal) não abre.and

# 1. A Padaria está aberta?
#     1. Se é feriado e NÃO é natal: não
#     2. Semãp, Se é sábado OU domingo E antes do meio dia: sim
#     3. Senão, se é dia de semana E antes das 19h: sim
#     4. Senão: não
# 2. Se a padaria está aberta E:
#     1. Se está chovendo: Pegar guarda-chuvas
#     2. Se está chovendo E calor: Pegar guarda-chuva e garrafa de água
#     3. Se está chovendo E frio OU nevando: pegar guarda chuva, blusa e botas
#     4. Ir até a padaria:
#         1. Se tem pao integral E baguete: Pedir 6 de cada
#         2. Senão, se tem apenas pao integral OU baguete: Pedir 12
#         3. Senão: Pedir 6 de qualquer pão
# 3. Senão
#     1. Ficar em casa e comer bolacha
#
# Statements:
#
# - Se = if
# - Senão, se = elif
# - Senão = else
# - E = and
# - OU = or
# - Não = not
#
# Expressão booleana: True ou False
#
# Ações:
# - funções, métodos, procedimentos, sub-rotinas, subprogramas, etc

# Pseudocódigo:
import ir, pegar, pedir, tem, comer, ficar

# Premissas
today = "domingo"
time = 11
holiday = False
christmas = False
raining = True
hot = True
cold = False
snowing = False
week = ["segunda", "terça", "quarta", "quinta", "sexta"]
bakery_hours = {
    "week": 19,
    "weekend": 12,
    "holiday": 0
}

# Algoritmo
if today in holiday and not christmas:
    bakery_open = False
elif today not in week and time < bakery_hours["weekend"] or today in week and time < bakery_hours["week"]:
    bakery_open = True
else:
    bakery_open = False

if bakery_open:
    if raining and (cold or snowing):
        pegar("guarda-chuva")
        pegar("blusa")
        pegar("botas")
    elif raining and hot:
        pegar("guarda-chuva")
        pegar("garrafa de água")
    elif raining:
        pegar("guarda-chuva")

    ir("padaria")
    if tem("pão integral") and tem("baguete"):
        pedir(6, "pão integral")
        pedir(6, "baguete")
    elif tem("pão integral") or tem("baguete"):
        pedir(12, "pão")
    else:
        pedir(6, "qualquer pão")
else:
    ficar("casa")
    comer("bolacha")