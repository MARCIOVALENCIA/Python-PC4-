import csv
import sqlite3

# Paso 1: Leer el archivo ventas.csv desde la ruta proporcionada
ventas = []
ruta_ventas = '/workspaces/Python-PC4-/ventas.csv'  # Asegúrate de que la ruta es correcta

with open(ruta_ventas, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        fecha, producto, cantidad, precio_dolares = row
        ventas.append({
            'fecha': fecha,
            'producto': producto,
            'cantidad': int(cantidad),
            'precio_dolares': float(precio_dolares)
        })

# Paso 2: Conectar a la base de datos SQLite para obtener el tipo de cambio
def obtener_tipo_cambio(fecha):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    # Consultar el tipo de cambio para la fecha
    cursor.execute("SELECT compra FROM sunat_info WHERE fecha = ?", (fecha,))
    resultado = cursor.fetchone()
    
    conn.close()
    
    if resultado:
        return resultado[0]  # Devuelve el tipo de cambio de compra
    else:
        return None

# Paso 3: Calcular el precio en soles por cada venta y mostrar el resultado
print(f"{'Fecha':<12} {'Producto':<15} {'Cantidad':<10} {'Precio $':<10} {'Precio S/':<10}")
for venta in ventas:
    tipo_cambio = obtener_tipo_cambio(venta['fecha'])
    
    if tipo_cambio:
        precio_soles = venta['precio_dolares'] * tipo_cambio
        print(f"{venta['fecha']:<12} {venta['producto']:<15} {venta['cantidad']:<10} {venta['precio_dolares']:<10} {precio_soles:<10.2f}")
    else:
        print(f"No se encontró tipo de cambio para la fecha {venta['fecha']}")
