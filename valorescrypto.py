import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '50ee7b14-dd76-4a0f-a77a-c3a7441afd8d'
}
params = {
  'symbol': 'BTC,ETH'
}

response = requests.get(url, headers=headers, params=params)

data = response.json()['data']

btc_price = data['BTC']['quote']['USD']['price']
eth_price = data['ETH']['quote']['USD']['price']

print(f"El precio de BTC es {btc_price} USD")
print(f"El precio de ETH es {eth_price} USD")

