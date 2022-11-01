import requests
import  json
from config import keys



class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: float):
        base=base.lower()
        quote=quote.lower()
        if quote == base and (base  in keys or quote  in keys) :
            raise APIException(f'Введите различные валюты: {base}.')


        # quote_ticker, base_ticker = keys[quote], keys[base]
        try:
            base_ticker = keys[base]

        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            quote_ticker = keys[quote]

        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            amount = float(amount)

        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        if  amount < 0:
            raise APIException('Введите положительное число')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base = total_base * amount

        return total_base