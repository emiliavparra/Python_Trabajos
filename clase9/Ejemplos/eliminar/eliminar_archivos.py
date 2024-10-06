# Importar el modulo 'os' para interactuar con el sistema operativo
import os

# Definir el nombre del archivo que queremos eliminar
nombre_archivo = 'archivo.txt'

# Comprobar si el archivo existe en la ruta especificada
# La funcion os.path.exists() devuelve True si el achivo existe, False si no existe
if os.path.exists(nombre_archivo):
    # Si el archivo existe procede a eliminarlo
    # La funcion os.remove() elimina el archivo en la ruta especificada
    os.remove(nombre_archivo)
    # Informar al usuario que el archivo ha sido eliminado
    print(f'Archivo {nombre_archivo} eliminado.')
else:
    # Si el archivo no existe, informar al usuario que no se encontro el archivo
    print(f'El archivo {nombre_archivo} no existe.')
