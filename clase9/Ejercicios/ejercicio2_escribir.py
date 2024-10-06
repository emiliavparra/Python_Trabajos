# En este caso el archivo no existe. Creara uno nuevo pero si ya existiera tiraria error

with open('new_file_x.txt', 'x') as file:  # Este es el metodo para crear un archivo nuevo
    file.write('Estoy creando este archivo ahora usando el modo \'x\'.\n')

# Imprimo y se crea el archivo a la vez que imprime el resultado
print('Este archivo new_file_x.txt ha sido creado con exito')

# Ahora lo re escribo

to_add = 'Esto va a reescribir el archivo y quedara con esto nada mas'
with open('rewrite_file_x.txt', 'w') as file:
    file.write(to_add)
print('Archivo new_file_x.txt sobre escrito con texto')
