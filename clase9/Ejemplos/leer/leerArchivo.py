# # Primero defino el nombre del archivo

# nombre_archivo = 'archivo.txt'

# # Paso 2: Leer todo el contenido de una sola vez
# with open(nombre_archivo, 'r') as archivo:
#     print('Leyendo el archivo de una vez con read(): ')
#     # Utiliza el metodo read para leer todo de una vez
#     contenido_completo = archivo.read()
#     print(contenido_completo)
#     # linea de separacion (40 guiones) para distinguir las siguientes lecturas
#     print('-' * 40)

# # Paso 3 Leer el archivo linea por linea
# with open(nombre_archivo, 'r') as archivo:
#     # usa el metodo readline() para leer la primera linea del archivo
#     print('Leyendo el archivo linea por linea():')
#     linea = archivo.readline()
#     # Mientras la variable 'linea' contenga contenido (no estè vacia), sigue leyendo
#     while linea:
#         print(linea.strip())
#         # Lee la siguiente linea del archivo. Si no hay mas lineas, readlione() devolvera una cadena vacia terminando el bucle
#         linea = archivo.readline()
#     print('_' * 40)

# # Paso 4: Leer todas las lineas ala vez con readlines()
# with open(nombre_archivo, 'r') as archivo:
#     print('Leer todas las lineas a la vez con readlines():')
#     # Usa el metodo readlines() para leer todas las lineas del archivo a la vez
#     # El resultado es una lista de cadenas, donde cada cadena es una linea del archivo
#     lineas = archivo.readlines()
#     # Se recorre la lista de cadenas, donde cada cadena es una linea del archivo
#     for linea in lineas:
#         # Imprime cada linea despues de eliminar los saltos de linea con strip()
#         print(linea.strip())
#     # Imprime una linea de separacion (40 guiones) para finalizar
#     print('_' * 40)
