import zipfile


archivo_zip = "Ruta donde esta alojado tu .zip"


directorio_destino = "Ruta de destino de los ficheros"


with zipfile.ZipFile(archivo_zip, 'r') as archivo_zip:

    archivo_zip.extractall(directorio_destino)

print(f"Archivos descomprimidos en: {directorio_destino}")
