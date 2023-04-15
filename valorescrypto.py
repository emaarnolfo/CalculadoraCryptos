import requests
import subprocess

#Cargar la biblioteca compartida
#lib_conversion = ctypes.CDLL('./libasm.so')

#Definir la firma de la funcion de conversion
#lib_conversion.conversion_a_pesos.restype = ctypes.c_double
#lib_conversion.conversion_a_pesos.argtypes = [ctypes.c_double]

#lib_conversion.sumaAsm.restype = ctypes.c_double
#lib_conversion.sumaAsm.argtypes = [ctypes.c_double, ctypes.c_double]


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

#Obtener los precios de BTC y ETH de la respuesta de la API
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

#Convertir el valor a pesos
#btc_price_pesos = lib_conversion.conversion_a_pesos(btc_price)
#eth_price_pesos = lib_conversion.conversion_a_pesos(eth_price)

#Precios de las criptomonedas en Dolar
print(f"Obteniendo datos de la API de CoinMarket:")
print(f"El precio de BTC es {round(btc_price_dolar, 2)} USD")
print(f"El precio de ETH es {round(eth_price_dolar, 2)} USD\n")

print(f"El precio de BTC es {round(btc_price_eur, 2)} EUR")
print(f"El precio de ETH es {round(eth_price_eur, 2)} EUR\n")

print(f"El precio de BTC es {round(btc_price_ars, 2)} pesos")
print(f"El precio de BTC es {round(eth_price_ars, 2)} pesos\n")

#tot_price_dolar = lib_conversion.sumaAsm(eth_price, btc_price)

#print(f"El precio de la suma de ambas monedas es {tot_price_dolar} dolares")


moneda = str(int(btc_price_dolar))

while True:
  # Leer la entrada del usuario
  print("Ingrese que moneda quiere convertir. (o escriba 'quit' para salir): ")
  moneda = input("Las opciones son: 'USD', 'EUR', 'ARS': ")

  if moneda.lower() == 'quit':
    print("¡Hasta luego!")
    break

  if(moneda.upper() == "USD"):
    n = input("Ingrese cuantos btc quiere convertir a USD: ")
    moneda = str(int(btc_price_dolar))
        
  if(moneda.upper() == "EUR"):
    n = input("Ingrese cuantos btc quiere convertir a Euro: ")
    moneda = str(int(btc_price_eur))
    
  if(moneda.upper() == "ARS"):
    n = input("Ingrese cuantos btc quiere convertir a pesos argentinos: ")
    moneda = str(int(btc_price_ars))
      

  result = subprocess.run(["./build/main", moneda, n], stdout=subprocess.PIPE)
  print(result.stdout.decode("utf-8"))