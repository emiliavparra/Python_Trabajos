# FUNCIONES COMUNES DE RANDOM
# EJEMPLO 1.random(): # Genera un numero flotante aleatorio entre 0.0 y 1.0

import random

print(random.random())

# EJEMPLO 2.Randint lleva como parametros a y b. Genera un numero entero aleatorio entre ambos
print(random.randint(1, 10))  # un numero del 1 al 10

# EJEMPLO 3.CHOICE(SEQ): Selecciona aleatoriamente un elemento de una secudncia (como una lista)
print(random.random())

colores = ['rojo', 'azul', 'verde']
print(random.choice(colores))  # Devuelve uno de los colores al azar

# EJEMPLO 4 shuffle(list)
print(random.random())

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)  # Mezcla los numeros
print(numeros)
