def contar_lineas_codigo(ruta_archivo):
    # Verificar si la extensión del archivo es .py
    if not ruta_archivo.endswith(".py"):
        print("El archivo no tiene la extensión .py. No se procesará.")
        return
    
    try:
        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()
        
        lineas_codigo = 0

        # Contar líneas de código excluyendo comentarios y líneas en blanco
        for linea in lineas:
            linea = linea.strip()
            if linea and not linea.startswith("#"):  # Excluir comentarios y líneas en blanco
                lineas_codigo += 1

        print(f"El archivo '{ruta_archivo}' tiene {lineas_codigo} líneas de código.")
    
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe. Verifique la ruta.")

# Solicitar al usuario la ruta del archivo
ruta_archivo = input("Ingrese la ruta del archivo .py: ")
contar_lineas_codigo(ruta_archivo)
