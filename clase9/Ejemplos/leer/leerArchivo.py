# Primero defino el nombre del archivo

nombre_archivo = 'archivo.txt'

# Paso 2: Leer todo el contenido de una sola vez
with open(nombre_archivo, 'r') as archivo:
    print('Leyendo el archivo de una vez con read(): ')
    contenido_completo = archivo.read()
    print(contenido_completo)
    print('_' * 40)

# Paso 3 Leer el archivo linea por linea
with open(nombre_archivo, 'r') as archive:
    print('Leyendo el archivo linea por linea():')
    linea = archivo.readline()
    while linea:
        print(linea.strip())
        linea = archivo.readline()
    print('_' * 40)

# # aso 3: Leer el archivo linea por linea
# with open (nombre_archivo, 'r') as archivo:
#     print("Leyendo el archivo linea por linea con readline(): ")
#     linea = archivo.readline()
#     while linea:
#         print(linea.strip())
#         linea = archivo.readline()
#     print("-" * 40)


# Paso 4: Leer todas las lineas ala vez con readlines()
with open(nombre_archivo, 'r') as archivo:
    print('Leer todas las lineas a la vez con readlines():')
    lineas = archivo.readlines()
    for line in lineas:
        print(lineas.strip())
    print('_' * 40)
