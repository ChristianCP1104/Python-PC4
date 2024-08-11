import os

def crear_tabla_multiplicar(n):
    """Genera una tabla de multiplicar y la guarda en un fichero."""
    if 1 <= n <= 10:
        with open(f'tabla-{n}.txt', 'w') as archivo:
            for i in range(1, 11):
                archivo.write(f'{n} x {i} = {n * i}\n')
        print(f'Tabla de multiplicar del {n} guardada en tabla-{n}.txt')
    else:
        print("Número fuera del rango permitido (1-10).")

def mostrar_tabla(n):
    """Lee y muestra la tabla de multiplicar desde el fichero."""
    if 1 <= n <= 10:
        try:
            with open(f'tabla-{n}.txt', 'r') as archivo:
                contenido = archivo.read()
                print(f'Tabla de multiplicar del {n}:\n{contenido}')
        except FileNotFoundError:
            print(f'El fichero tabla-{n}.txt no existe.')
    else:
        print("Número fuera del rango permitido (1-10).")

def mostrar_linea_m(n, m):
    """Lee y muestra una línea específica de la tabla de multiplicar desde el fichero."""
    if 1 <= n <= 10 and 1 <= m <= 10:
        try:
            with open(f'tabla-{n}.txt', 'r') as archivo:
                lineas = archivo.readlines()
                if 1 <= m <= len(lineas):
                    print(f'Línea {m} de la tabla de {n}: {lineas[m - 1].strip()}')
                else:
                    print(f'La línea {m} no existe en el fichero tabla-{n}.txt.')
        except FileNotFoundError:
            print(f'El fichero tabla-{n}.txt no existe.')
    else:
        print("Números fuera del rango permitido (1-10).")

def menu():
    while True:
        print("\nMenú:")
        print("1. Crear tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea específica de la tabla")
        print("4. Salir")

        opcion = input("Elija una opción (1-4): ")
        
        if opcion == '1':
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            crear_tabla_multiplicar(n)
        elif opcion == '2':
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            mostrar_tabla(n)
        elif opcion == '3':
            n = int(input("Ingrese el número de la tabla (entre 1 y 10): "))
            m = int(input("Ingrese el número de la línea (entre 1 y 10): "))
            mostrar_linea_m(n, m)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()
