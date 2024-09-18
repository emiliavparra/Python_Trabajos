# 1. Ejercicio de Sets y for

# Crea un programa que reciba una lista de números y realice las siguientes operaciones:
# 1. Crear un set a partir de la lista para eliminar duplicados.
# 2. Iterar sobre el set e imprimir cada número.
# 3. Contar cuántos números son mayores que un valor dado y almacenarlos en un nuevo set.

# Primero le doy las listas al programa

lista_numeros = {1, 2, 3, 4, 3, 8, 1, 2, 3, 5, 7, 2}

# Creo el set para eliminar duplicados
lista_set = set(lista_numeros)
print(lista_set)  # Chequeo que se hayan eliminado los duplicados

# Itero sobre el set e imprimo cada numero
for numero in lista_set:
    print(numero)

# Cuento cuantos numeros son mayores que 3 y los guardo en un nuevo set:
mayor_que = 3
nuevo_set = set()

for numero in lista_set:
    if numero > mayor_que:
        nuevo_set.add(numero)
print(f'El set con los numeros mayores a 3 es {nuevo_set}')
