import requests
import zipfile
import os

# Paso 1: Descargar la imagen desde la URL
url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fD8BMHxwaG90by1wYWdlfHx8GVufDB8fHx8fA%3D%3D"
imagen_nombre = "imagen_descargada.jpg"
respuesta = requests.get(url)

# Guardar la imagen descargada
with open(imagen_nombre, "wb") as file:
    file.write(respuesta.content)

print("Imagen descargada y guardada como:", imagen_nombre)

# Paso 2: Crear un archivo ZIP y almacenar la imagen
zip_nombre = "imagen_zip.zip"
with zipfile.ZipFile(zip_nombre, 'w') as zip_file:
    zip_file.write(imagen_nombre)
    
print(f"Imagen comprimida y guardada en {zip_nombre}")

# Paso 3: Descomprimir el archivo ZIP
with zipfile.ZipFile(zip_nombre, 'r') as zip_file:
    zip_file.extractall("descomprimido")
    
print(f"Archivo {zip_nombre} descomprimido en la carpeta 'descomprimido'")
