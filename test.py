import requests

def read_env(path=".env"):
    """Retourne les variables du .env dans un dict (sans toucher à os.environ)"""
    env_vars = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):  # ignorer vide et commentaires
                continue
            key, value = line.split("=", 1)
            env_vars[key.strip()] = value.strip().strip('"').strip("'")
    return env_vars

# URL de ta base Firebase Realtime Database (finir par .json)
BASE_URL = "https://mariage-efaba-default-rtdb.europe-west1.firebasedatabase.app/test.json?auth="+ read_env()["KEY"]

# Exemple de données JSON à stocker
person = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# 🔹 Créer une liste de 100 personnes identiques
data = [person for _ in range(4)]
#print(requests.get(BASE_URL).content)


response = requests.put(BASE_URL, json=data)
print("PUT:", response.status_code, response.json())


update_data = {"0": {
    "nom": "Marc",
    "age": 26,
    "ville": "Paris"
}}
response = requests.patch(BASE_URL, json=update_data)
print("PATCH:", response.status_code, response.json())


response = requests.get(BASE_URL)
print("GET:", response.status_code, response.json())