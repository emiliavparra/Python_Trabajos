# Importo el modulo:
import csv

# Lo abro al archivo pero en modo lectura unicamente
with open('datos.csv', 'r') as file:
    # Creo el lector que es el que va a interpretar el archivo csv
    reader = csv.reader(file)

    # Y ahora le pido que itere por cada fila y la imprima
    for line in reader:
        print(line)
