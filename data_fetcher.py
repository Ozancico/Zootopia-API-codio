# data_fetcher.py

import requests
from dotenv import load_dotenv
import os

# Lade Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Hol den API-Schlüssel aus der Umgebungsvariablen
API_KEY = os.getenv("API_KEY")
API_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': { ... },
        'locations': [ ... ],
        'characteristics': { ... }
    }
    """
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"⚠️ Error fetching data: {response.status_code}")
        return []

