import os

# Paso 1: Solicitar la ruta del archivo .py
ruta_archivo = input("Ingrese la ruta del archivo .py: ")

# Paso 2: Verificar si la ruta es válida y si el archivo termina en .py
if not os.path.isfile(ruta_archivo) or not ruta_archivo.endswith('.py'):
    print("Ruta inválida o el archivo no es un .py")
else:
    # Paso 3: Contar las líneas de código
    lineas_codigo = 0

    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()

            for linea in lineas:
                linea = linea.strip()

                if linea and not linea.startswith('#'):
                    lineas_codigo += 1

        print(f"Número de líneas de código: {lineas_codigo}")

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
