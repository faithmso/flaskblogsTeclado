import time
from openexchange import OpenExchangeClient

APP_ID = {"app_id": "f9b67e221cee486cb5b7bb5c5dbcf91d"}

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
gdp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end-start)
print(f"USD{usd_amount} is GBP{gdp_amount:.2f}")