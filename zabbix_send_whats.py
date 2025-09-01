#!/usr/bin/env python3
import sys
import requests
import json

# ✅ Parâmetros do Zabbix (recebidos ao disparar alerta)
# $1 = número (ou grupo)
# $2 = assunto
# $3 = mensagem
try:
    TO = sys.argv[1]
    SUBJECT = sys.argv[2]
    MESSAGE = sys.argv[3]
except IndexError:
    print("Erro: parâmetros insuficientes. Esperado: TO SUBJECT MESSAGE")
    sys.exit(1)

# ✅ Configuração da Evolution API
BASE_URL = 'http://IP_DO_SERVIDOR:8080'
INSTANCE_NAME = 'zabbixcentral'
API_KEY = 'password'

headers = {
    'apikey': API_KEY,
    'Content-Type': 'application/json'
}

payload = {
    'number': TO,
    'text': f"{SUBJECT}\n{MESSAGE}"
}

# ✅ Envio da mensagem
try:
    response = requests.post(
        url=f"{BASE_URL}/message/sendText/{INSTANCE_NAME}",
        json=payload,
        headers=headers
    )
    response.raise_for_status()
    print("Mensagem enviada com sucesso!")
except Exception as e:
    print(f"Erro ao enviar mensagem: {e}")
    sys.exit(1)
