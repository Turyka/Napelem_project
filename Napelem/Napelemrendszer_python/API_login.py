import requests
from dotenv import load_dotenv
import os
def login_to_laravel_api(username, password):
    load_dotenv()
    url = os.getenv("API_LOGIN_KEY")

    data = {
        "name": username,
        "password": password
    }

    try:
        # API
        response = requests.post(url, json=data)

        # ha jo
        if response.status_code == 200:
            # megkapja ha jo
            token = response.json().get("token")
            return token, None  
        else:
            error_message = response.json().get("message", "Nem jo a user vagy a jelszo")
            return None, error_message
    except requests.exceptions.RequestException as e:
        return None, f"Ez az errorr: {e}"