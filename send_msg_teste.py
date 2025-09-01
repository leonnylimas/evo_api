BASE_URL = 'http://192.168.1.20:8080'
INSTANCE_NAME = 'zabbixcentral_bkp'
EVOLUTION_AUTHENTICATION_API_KEY = 'password'

headers = {
    'apikey': EVOLUTION_AUTHENTICATION_API_KEY,
    'Content-Type': 'application/json'
}
payload = {
    'number': '12036322013XXXXXX@g.us',
    # 'number': 'SEU NÚMERO DE TELEFONE' para enviar mensagem para contato
    'text': 'Olá zabbix!',
    # 'delay': 10000, # simular "digitando"
}
response = requests.post(
    url=f'{BASE_URL}/message/sendText/{INSTANCE_NAME}',
    json=payload,
    headers=headers,
)
print(response.json())
