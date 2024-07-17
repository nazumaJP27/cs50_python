import sys
import requests
import json

try:
    n_coin = float(sys.argv[1])
    print(n_coin)
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit

o = response.json()
price = o["bpi"]["USD"]["rate"]
price = float(price.replace(",", ""))
coin_price = price * n_coin
print(f"${coin_price:,.4f}")
