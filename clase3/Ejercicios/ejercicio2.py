# Crea un programa que tome una lista de números y calcule la suma de una sublista especificada por el usuario.

# Defino la lista
lista_numeros = [1, 2, 3, 3, 4, 5, 3, 3, 2, 8]

# Le pido al usuario que ingrese el índice de inicio y el índice de fin para la sublista
sublista_inicio = int(input('Por favor ingrese indice de inicio:'))
sublista_final = int(input('Por favor ingrese indice de final:'))

# Uso slicing para obtener la sublista

print('La lista del usuario es:',
      lista_numeros[sublista_inicio:sublista_final])

sublista_usuario = lista_numeros[sublista_inicio:sublista_final]
suma = sum(sublista_usuario)
print('La suma de la sublista es: ', suma)
