import requests

BASE_URL = "http://localhost:5000"

# Listar dispositivos
devices = requests.get(f"{BASE_URL}/devices").json()
print(f"🔎 Dispositivos disponíveis: {devices}")

# Ligar lâmpada
response = requests.post(f"{BASE_URL}/lampada", json={"action": "ligar"})
print(response.json())

# Desligar lâmpada
response = requests.post(f"{BASE_URL}/lampada", json={"action": "desligar"})
print(response.json())
