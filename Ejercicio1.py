import requests

# Solicita la cantidad de bitcoins
n = float(input("Ingrese la cantidad de bitcoins que posee: "))

# URL de la API de CoinDesk
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = requests.get(url)
    # Verificar
    response.raise_for_status()
    
    # Extraer en formato JSON
    bitcoin_data = response.json()
    
    # Obtener el precio actual de Bitcoin (USD)
    bitcoin_price_usd = bitcoin_data['bpi']['USD']['rate_float']
    
    # Calcular el valor total (USD)
    valor_total_usd = n * bitcoin_price_usd
    
    # Mostrar el valor total con el formato adecuado
    print(f"El valor de {n} Bitcoins es: ${valor_total_usd:,.4f} USD")

except requests.RequestException as e:
    print("Error al consultar la API:", e)
