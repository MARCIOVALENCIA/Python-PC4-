# Paso 1: Leer el archivo temperaturas.txt
with open("temperaturas.txt", "r") as archivo:
    lineas = archivo.readlines()

# Crear listas para almacenar las fechas y temperaturas
fechas = []
temperaturas = []

# Procesar cada línea del archivo
for linea in lineas:
    fecha, temperatura = linea.strip().split(",")
    fechas.append(fecha)
    temperaturas.append(float(temperatura))

# Paso 2: Calcular la temperatura promedio, máxima y mínima
temperatura_promedio = sum(temperaturas) / len(temperaturas)
temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)

# Paso 3: Escribir los resultados en un nuevo archivo
with open("resumen_temperaturas.txt", "w") as resumen:
    resumen.write(f"Temperatura promedio: {temperatura_promedio:.2f}°C\n")
    resumen.write(f"Temperatura máxima: {temperatura_maxima:.2f}°C\n")
    resumen.write(f"Temperatura mínima: {temperatura_minima:.2f}°C\n")

print("Resumen generado exitosamente en 'resumen_temperaturas.txt'")
