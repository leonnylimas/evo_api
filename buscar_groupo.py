import requests

url = "http://192.168.1.20:8080/group/fetchAllGroups/zabbixcentral_bkp"

querystring = {"getParticipants":"true"}

headers = {"apikey": "pasword"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
