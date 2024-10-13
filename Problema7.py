import sqlite3

# Conectar a SQLite
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# Crear la tabla sunat_info si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sunat_info (
        fecha TEXT,
        compra REAL,
        venta REAL
    )
''')

conn.commit()
conn.close()

print("Tabla 'sunat_info' creada correctamente.")


import requests
import sqlite3

# Definir las fechas del 2023 para las que se requiere el tipo de cambio
meses = list(range(1, 13))  # Meses de 1 a 12
anio = 2023
token = 'apis-token-1.aTSI1U7KEuT-6bbbCguH-4Y8TI6KS73N'  # Reemplaza con el token correcto si es necesario

# Conectar a la base de datos
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# Recorrer cada mes y obtener los datos del tipo de cambio para cada día del mes
for mes in meses:
    url = f"https://api.apis.net.pe/v2/sunat/tipo-cambio?month={mes}&year={anio}"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    response = requests.get(url, headers=headers)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        
        # Insertar los datos en la base de datos
        for entry in data:
            fecha = entry.get('fecha')
            compra = entry.get('compra')
            venta = entry.get('venta')
            cursor.execute("INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)", (fecha, compra, venta))
    else:
        print(f"Error al obtener datos para el mes {mes}: {response.status_code}")

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Datos de tipo de cambio cargados correctamente en la base de datos.")
