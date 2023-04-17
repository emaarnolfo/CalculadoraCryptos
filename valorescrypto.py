import requests
import subprocess


### API REQUEST ###
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

prices_array = []

### PRICES REQUEST ###

# Solicitar los precios en USD de BTC y ETH
btc_price_dolar = data['BTC']['quote']['USD']['price']
eth_price_dolar = data['ETH']['quote']['USD']['price']


# Solicitar precios de BTC y ETH en EUR
params_eur = {
  'symbol': 'BTC,ETH',
  'convert': 'EUR'
}

response_eur = requests.get(url, headers=headers, params=params_eur)

data_eur = response_eur.json()['data']

# Obtener los precios de BTC y ETH en EUR
btc_price_eur = data_eur['BTC']['quote']['EUR']['price']
eth_price_eur = data_eur['ETH']['quote']['EUR']['price']


# Solicitar precios de BTC y ETH en ARS
params_ars = {
  'symbol': 'BTC,ETH',
  'convert': 'ARS'
}

response_ars = requests.get(url, headers=headers, params=params_ars)

data_ars = response_ars.json()['data']

# Obtener los precios de BTC y ETH en ARS
btc_price_ars = data_ars['BTC']['quote']['ARS']['price']
eth_price_ars = data_ars['ETH']['quote']['ARS']['price']


# Precios de las criptomonedas en Dolar
print(f"Obteniendo datos de la API de CoinMarket:")
print(f"El precio de BTC es {round(btc_price_dolar, 2)} USD")
print(f"El precio de ETH es {round(eth_price_dolar, 2)} USD\n")

# Precios de las criptomonedas en Euros
print(f"El precio de BTC es {round(btc_price_eur, 2)} EUR")
print(f"El precio de ETH es {round(eth_price_eur, 2)} EUR\n")

# Precios de las criptomonedas en Pesos Argentinos
print(f"El precio de BTC es {round(btc_price_ars, 2)} pesos")
print(f"El precio de BTC es {round(eth_price_ars, 2)} pesos\n")

# Acomodar en el arreglo BTC y ETH: [[btc], [eth]]
prices_array = [[btc_price_dolar, btc_price_eur, btc_price_ars], 
                [eth_price_dolar, eth_price_eur, eth_price_ars]]

#moneda = str(int(btc_price_dolar))


def crypto_converter(crypto_type):
  
  print("Ingrese el tipo de conversión que desea realizar")
  moneda = input("Las opciones son: 'USD', 'EUR', 'ARS': ")

  if(moneda.upper() == "USD"):
    n = input("Ingrese cuánto quiere convertir a USD: ")
    moneda = str(int(prices_array[crypto_type][0]))
        
  elif(moneda.upper() == "EUR"):
    n = input("Ingrese cuánto quiere convertir a Euro: ")
    moneda = str(int(prices_array[crypto_type][1]))
    
  elif(moneda.upper() == "ARS"):
    n = input("Ingrese cuánto quiere convertir a pesos argentinos: ")
    moneda = str(int(prices_array[crypto_type][2]))
      

  return n, moneda


crypto_type = 0


while True:
  # Leer la entrada del usuario
  print("Ingrese que moneda quiere convertir. (o escriba 'quit' para salir): ")
  crypto = input("Las opciones son BTC, ETH o quit para salir: ").lower()
  
  if crypto == 'quit':
    print("¡Hasta luego!")
    break

  if(crypto == 'btc'):
    crypto_type = 0
  elif(crypto == 'eth'):
    crypto_type = 1
  else:
    print("Opción no válida. Por favor intente nuevamente")
    continue

  
  n, conversion = crypto_converter(crypto_type)

  result = subprocess.run(["./build/main", conversion, n], stdout=subprocess.PIPE)
  print(result.stdout.decode("utf-8"))  