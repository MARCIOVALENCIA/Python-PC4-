import requests

# Solicitar al usuario la cantidad de Bitcoins que posee
try:
    n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    
    # Consultar la API de CoinDesk para obtener el precio actual de Bitcoin
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()  # Verifica si hay errores en la solicitud
    
    # Parsear la respuesta JSON
    data = response.json()
    precio_bitcoin = data["bpi"]["USD"]["rate_float"]
    
    # Calcular el costo de 'n' Bitcoins en USD
    costo_total = n * precio_bitcoin
    
    # Mostrar el resultado con el formato adecuado
    print(f"El costo actual de {n} Bitcoins en USD es: ${costo_total:,.4f}")

except requests.RequestException as e:
    print("Error al consultar el precio de Bitcoin:", e)
except ValueError:
    print("Por favor, ingrese un valor numérico válido para la cantidad de Bitcoins.")
