#!/usr/bin/env python3 

import logging # docs.python.org/3/library/logging.html#logging-levels

# instanciando o logger
log = logging.Logger("logs.py", logging.DEBUG)

# levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

# formatacao: logging.<level>(<mensagem>)

# destino: console, arquivo, etc

log.debug("Mensagem de debug para desenvolvedores")
log.info("Mensagem de informação para usuários")
log.warning("Mensagem de aviso que algo inesperado aconteceu")
log.error("Mensagem de erro que afetou o funcionamento do programa")
log.critical("Mensagem de erro crítico que afetou o funcionamento do programa e precisa de atenção imediata")

print("---")

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu Ruim! %s", str(e))