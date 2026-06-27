#!/usr/bin/env python3 

import os
import logging # docs.python.org/3/library/logging.html#logging-levels

log_level = os.environ.get("LOG_LEVEL", "WARNING").upper() # DEBUG, INFO, WARNING, ERROR, CRITICAL

# instanciando o logger
log = logging.Logger("logs.py", logging.DEBUG)

# levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
ch = logging.StreamHandler() # destino: console
ch.setLevel(log_level) # definindo o nível de log do destino

# formatacao: logging.<level>(<mensagem>)
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s l: %(lineno)d f: %(filename)s - %(message)s") # formato da mensagem
ch.setFormatter(fmt) # adicionando o formato ao destino

# destino: console, arquivo, etc
log.addHandler(ch) # adicionando o destino ao logger
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