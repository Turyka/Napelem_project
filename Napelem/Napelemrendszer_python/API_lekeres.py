import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

try:
    lekeres = requests.get(api_key, timeout=10)

    # ha jó
    if lekeres.status_code == 200:
        data = lekeres.json()
        print("Status:", data['status'])
        print("Data:", data['data'])
        print("\n")
        for user in data['data']:
            print(f'felhasznalonev: "{user["name"]}" jelszo: "{user["password"]}"')
       
    else:
        print(f"Hiba nem sikerult csatlakozni: {lekeres.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")