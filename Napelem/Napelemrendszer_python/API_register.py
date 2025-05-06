import requests
from dotenv import load_dotenv
import os
def register_to_laravel_api(username, password):
    load_dotenv()
    url = os.getenv("API_LOGIN_KEY")

    data = {
        "name": username,
        "password": password
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        # API
        response = requests.post(url, json=data)

        # ha jo
        if response.status_code == 200:
            response = requests.post(url, json=data, headers=headers)
            return response.json()
        else:
            error_message = response.json().get("message", "nem sikerult")
            return None, error_message
    except requests.exceptions.RequestException as e:
        return None, f"Ez az errorr: {e}"   