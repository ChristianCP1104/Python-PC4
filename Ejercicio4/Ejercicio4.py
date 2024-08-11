import csv

def calcular_estadisticas_temperaturas(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r') as archivo:
            lector = csv.reader(archivo)
            temperaturas = [float(fila[1]) for fila in lector if fila[1].replace('.', '', 1).isdigit()]

        if not temperaturas:
            raise ValueError("El archivo no contiene datos válidos de temperatura.")

        promedio = sum(temperaturas) / len(temperaturas)
        maxima = max(temperaturas)
        minima = min(temperaturas)

        with open(archivo_salida, 'w') as archivo:
            archivo.write(f'Temperatura promedio: {promedio:.2f}\n')
            archivo.write(f'Temperatura máxima: {maxima:.2f}\n')
            archivo.write(f'Temperatura mínima: {minima:.2f}\n')

        print(f'Resultados escritos en {archivo_salida}')

    except FileNotFoundError:
        print(f'El archivo {archivo_entrada} no se encuentra.')
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    calcular_estadisticas_temperaturas('temperaturas.txt', 'resumen_temperaturas.txt')
