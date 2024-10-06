# Primero defino el nombre del archivo a leer

open_file = 'mi_archivo.txt'

# Ahora lo abro con el metodo 'read' para leer todo de una
# with open('mi_archivo.txt', 'r') as file:
#     print('Esta forma lee todo el archivo a la vez: ')
#     # Uso el metodo para que lea todo de uan vez
#     open_complete_file = file.read()
#     # Imprimo el resultado
#     print(open_complete_file)

# Ahora hago el programa
with open('mi_archivo.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
