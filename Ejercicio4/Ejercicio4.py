import csv
import statistics

# Paso1: Leer CSV
nombre_csv = "datos.csv"
datos = []
with open(nombre_csv, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        datos.append(float(row[0]))

print(f"Datos leídos del archivo: {datos}")

# Paso2: Calcular la suma, media, y desviación estándar
suma_datos = sum(datos)
media_datos = statistics.mean(datos)
desviacion_estandar = statistics.stdev(datos)

# Paso3: Mostrar resultados
print(f"Suma: {suma_datos}")
print(f"Media: {media_datos}")
print(f"Desviación Estándar: {desviacion_estandar}")
