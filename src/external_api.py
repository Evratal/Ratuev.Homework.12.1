"""""""""
Модуль для конвертации иностранной валюты из транзакции  в рубли (при необходимости).
"""""""""""
from pathlib import Path

import requests, os
from dotenv import load_dotenv

dotenv_path = os.path.join(Path(os.path.dirname(__file__)).parents[0], "data", ".env")

load_dotenv(dotenv_path)

def get_currency_rate(amount_val):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount_val}"
    api_key = os.getenv("API_KEY")

    headers = {
        "apikey": f"{api_key}"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return data["result"]

print(get_currency_rate(458))