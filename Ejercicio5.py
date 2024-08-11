# Paso 1: Solicitar cadena de texto
texto = input("Ingrese una cadena de texto: ")

# Paso 2: Contar el número de palabras
numero_palabras = len(texto.split())

# Paso 3: Contar el número de caracteres
numero_caracteres = len(texto)

# Paso 4: Resultados
print(f"Número de palabras: {numero_palabras}")
print(f"Número de caracteres: {numero_caracteres}")
