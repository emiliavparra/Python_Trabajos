import csv  # Importamos el modulo

# Abrir el archivo csv en modo lectura
with open('archivo.csv', 'r') as file:
    # Crear un lector csv que unterpreta el archivo como un archivo csv
    reader = csv.reader(file)

    # Iterar sobre cada file del archivo
    for fila in reader:
        print(fila)
