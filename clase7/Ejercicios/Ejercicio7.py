# 7. Ejercicio Combinado
# Desarrolla un programa que:
# 1. Genere una lista de números aleatorios entre 1 y 20.
# 2. Usa un bucle for con range para iterar sobre la lista.
# 3. Usar continue para saltar números menores de 10.
# 4. Usar break para detener la iteración si se encuentra un número
# divisible por 15.
# 5. Imprimir todos los números que cumplen las condiciones.
# 6. Utilizar list comprehension para filtrar los números que no cumplen
# ninguna condición.

# LO HICE EN FORMATO SIMPLE
# Primero genero la linea aleatoria entre 1 y 20
lista_aleatoria = [1, 2, 3, 4, 5, 2, 1, 4, 8, 11, 19, 15, 13, 2]
# Creo una lista vacia donde se van a guardar los que cumplan las condiciones
lista_que_cumple = []

for x in range(20):  # Le pido que busque en el range de 20
    if x < 10:  # Si el numero es menor a 10 se agrega a la lista que cumple las condiciones
        lista_que_cumple.append(x)
        continue  # continua
    if x % 15 == 0:  # si el nro es divisible por 15 lo agrega a la lista que cumple las condiciones
        lista_que_cumple.append(x)
        break  # se rompe el codigo cuando llega a 15 por eso no sale el 2

print(f'Los numeros que cumplen las condiciones de ser menores a 10 y divisibles por 15 son: {
      lista_que_cumple}')

# LO HICE EN FORMATO FUNCION

# defino una funcion que va a recibir una cantidad variable de argumentos


def lista_a_analizar(*args):
    lista_que_cumple = []  # creo la lista vacia donde se van a guardar
    for x in range(20):
        if x < 10:
            lista_que_cumple.append(x)
            continue
        if x % 15 == 0:
            lista_que_cumple.append(x)
            break
    return lista_que_cumple


# uso mi funcion con una lista aleatoria de numeros
lista_aleatoria = lista_a_analizar(
    1, 2, 3, 4, 5, 2, 1, 4, 8, 11, 19, 15, 13, 2)
print(f'Los numeros que cumplen las condiciones de ser menores a 10 y divisibles por 15 pero en funcion es: {
      lista_aleatoria}')

# uso list comprehension para que imprima los mayores a 10 no divisibles por 15
lista_que_no_cumple = [x for x in range(20) if x % 15 != 0 and x > 10]
print(f'La lista de los que son mayores que 10 y no se divididen por 10 son: {
      lista_que_no_cumple}')
