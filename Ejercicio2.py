from pyfiglet import Figlet
import random

# Crear en Figlet
figlet = Figlet()

# Solicitar nombre de la fuente
fuente = input("Ingrese el nombre de la fuente (o presione Enter para una aleatoria): ")

# Si no se ingresa una fuente, se selecciona una aleatoria
if not fuente:
    fuente = random.choice(figlet.getFonts())

# Configurar la fuente ingresada
figlet.setFont(font=fuente)

# Solicitar texto
texto = input("Ingrese el texto que desea convertir en arte ASCII: ")

# Imprimir el texto en estilo ASCII
print(figlet.renderText(texto))
