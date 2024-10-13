import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# Verificar las fechas disponibles en la tabla sunat_info
cursor.execute("SELECT fecha FROM sunat_info")
fechas = cursor.fetchall()

# Mostrar las fechas disponibles
for fecha in fechas:
    print(fecha[0])

conn.close()
