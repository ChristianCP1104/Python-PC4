import requests
import zipfile

# Descargar la imagen desde el URL
url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
nombre_imagen = "imagen_descargada.jpg"

try:
    # Descargar
    response = requests.get(url)
    response.raise_for_status()

    # Guardar
    with open(nombre_imagen, 'wb') as file:
        file.write(response.content)
    print(f"Imagen descargada y guardada como {nombre_imagen}")

except requests.RequestException as e:
    print(f"Error al descargar la imagen: {e}")

# Paso 2: Almacenar en archivo ZIP
nombre_zip = "imagen_comprimida.zip"

with zipfile.ZipFile(nombre_zip, 'w') as zipf:
    zipf.write(nombre_imagen)
    print(f"Imagen comprimida en el archivo {nombre_zip}")

# Paso 3: Descomprimir el archivo ZIP y extraer la imagen
with zipfile.ZipFile(nombre_zip, 'r') as zipf:
    zipf.extractall()
    print(f"Imagen extraída del archivo {nombre_zip}")
