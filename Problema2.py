import pyfiglet
import random

# Crear una instancia de Figlet
figlet = pyfiglet.Figlet()

# Obtener la lista de fuentes disponibles
fuentes_disponibles = figlet.getFonts()

# Solicitar al usuario el nombre de la fuente
fuente_seleccionada = input("Ingrese el nombre de la fuente (presione Enter para elegir una aleatoria): ").strip()

# Si no se ingresa una fuente, se elige una aleatoria
if not fuente_seleccionada:
    fuente_seleccionada = random.choice(fuentes_disponibles)

# Configurar la fuente en la instancia de Figlet
figlet.setFont(font=fuente_seleccionada)

# Solicitar al usuario el texto a imprimir
texto_imprimir = input("Ingrese el texto que desea imprimir: ")

# Imprimir el texto usando la fuente seleccionada
print(figlet.renderText(texto_imprimir))
