import os

# Función para escribir la tabla de multiplicar en un archivo
def escribir_tabla(n):
    with open(f"tabla-{n}.txt", "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en tabla-{n}.txt")

# Función para leer y mostrar la tabla de multiplicar
def leer_tabla(n):
    try:
        with open(f"tabla-{n}.txt", "r") as archivo:
            contenido = archivo.read()
        print(f"Tabla de multiplicar del {n}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")

# Función para leer una línea específica de la tabla
def leer_linea_especifica(n, m):
    try:
        with open(f"tabla-{n}.txt", "r") as archivo:
            lineas = archivo.readlines()
        if 1 <= m <= 10:
            print(f"Línea {m}: {lineas[m - 1]}")
        else:
            print("El número m debe estar entre 1 y 10.")
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")
    except IndexError:
        print(f"La línea {m} no existe en la tabla de multiplicar.")

# Función principal para mostrar el menú y ejecutar las tareas
def menu():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Leer una línea específica de una tabla")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= n <= 10:
                escribir_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "2":
            n = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= n <= 10:
                leer_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "3":
            n = int(input("Ingrese el número entre 1 y 10: "))
            m = int(input("Ingrese el número de línea (m) entre 1 y 10: "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                leer_linea_especifica(n, m)
            else:
                print("Ambos números deben estar entre 1 y 10.")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()
