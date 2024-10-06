# Primero defino el nombre del archivo

nombre_archivo = 'archivo1.txt'

# Paso 2: Leer todo el contenido de una sola vez
with open(nombre_archivo, 'r') as archivo:
    print('Leyendo el archivo de una vez con read(): ')
    contenido_completo = archivo.read()
    print(contenido_completo)
    print('-' * 40)
