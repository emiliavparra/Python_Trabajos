# import csv

# # Definimos los nombres de las columnas para el archivo csv
# fieldnames = ['Nombre', 'Edad', 'Ciudad']

# # Abrir en modo lectura
# # Newline='' se utiliza para evitar lineas en blanco adicionales en algunos s.o
# with open('archivo.csv', 'w', newline='') as file:
#     # Creamos un objeto 'Dictwriter
#     # se pasa el archivo y la lista de nombres de colimnas (fieldnames)
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     # Escribir la fila de encabezados en el archivo csv
#     # Esto crea la primera fila con los nombres de columnas
#     writer.writeheader()

#     # Escribir una fila con los datos de un archivo csv
#     # Cada dicc debe tener claves que coincidan con los nombres de las columnas
#     writer.writerow({'Nombre': 'Ana', 'Edad': '35', 'Ciudad': 'Neuquen'})

#     # Escribir multiples filas de datos en el archivo csv
#     writer.writerows([
#         {'Nombre': 'Luis', 'Edad': '25', 'Ciudad': 'Barcelona'},
#         {'Nombre': 'Marta', 'Edad': '28', 'Ciudad': 'Valencia'
#          }])

# Importo el modulo
import csv

# Defino los nombres de las columnas para mi csv:
fieldnames = ['Nombre', 'Edad']
# Lo abro en modo escritura
with open('archivoadef.csv', 'w', newline='') as file:
    # Creo el objeto dictwriter
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # Escribo la fila de encabezados en el csv para crear la primera fila con los nombres de mis columnas
    writer.writeheader()

    writer.writerows([
        {'Nombre': 'Ana', 'Edad': 23},
        {'Nombre': 'Luis', 'Edad': 25}
    ])
