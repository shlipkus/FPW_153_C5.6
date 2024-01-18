import requests
import json
from config import keys
class APIExeption(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIExeption('Валюты должны быть разными')

        try:
            amount = float(amount)
        except ValueError:
            raise APIExeption('Некоректное количество валюты')

        if quote not in keys:
            raise APIExeption(f'Валюта {quote} недоступна ')

        if base not in keys:
            raise APIExeption(f'Валюта {base} недоступна ')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total = json.loads(r.content)[keys[base]]*amount
        return total
