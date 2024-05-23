import requests
from cachetools import cached, TTLCache

class OpenExchangeClient:
    Base_Url = "https://openexchangerates.org/api/latest.json"

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest(self):
        return requests.get(self.Base_Url, self.app_id, verify=False).json()
    
    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest['rates']
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return from_amount * to_rate
        else:
            from_in_usd = from_amount/rates[from_currency]
            return from_in_usd * to_rate