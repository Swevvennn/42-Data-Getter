import requests
import os
from rich import print
from dotenv import load_dotenv

def get_access_token():
    try:
        load_dotenv()
        url = "https://api.intra.42.fr/oauth/token"
        data = {
            'grant_type': 'client_credentials',
            'client_id': os.getenv('API_PUBLIC_KEY'),
            'client_secret': os.getenv('API_SECRET_KEY')
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json().get('access_token')
    except requests.exceptions.HTTPError:
        os.system("clear")
        print("Double check if you have well set up the .env file at the root of the git.")
        print("If yes then check your API keys on your account.")
        exit()
