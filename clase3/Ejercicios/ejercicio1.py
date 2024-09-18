# Escribe un programa que cuente cuántas veces aparece un número específico en una lista

# Primero creo la lista de numeros
lista_numeros = [1, 2, 3, 3, 4, 5, 3, 3, 2, 8]
# le pido al usuario que ingrese el numero a buscar
contador = lista_numeros.count(int(input('Por favor ingresa un numero:')))
# Imprimo el resultado
print(f'El numero que ingresaste aparece {contador} veces')
