# Ejemplo 1 funcion Lambda basica
from functools import reduce
def suma(x, y): return x + y


print(f'Suma de 5 + 3: {suma(5, 3)}')

# Ejemplo 2 uso de Lambda con map()
# Map aplica una funcion a todos los elementos de un iterable y devuelve un iterador con los resultados
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x**2, numeros)
print(f'Cuadrados de la lista {numeros}: {list(cuadrados)}')

# Ejemplo 3 uso de Lambda con filter()
# Filtra los elementos de un iterable basado en una condicion, devolviendo solo los que cumplen la condicion
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(f'Los pares de {numeros} son: {list(pares)}')

# Ejemplo 4 uso de Lambda con sorted()
# Ordena los elementos de una lista, tupla o cualquier iterante basado en una funcion de clave
tuplas = [(1, 2), (3, 1), (5, 0)]
ordenadas = sorted(tuplas, key=lambda t: t[1])
print(f'Lista de tuplas ordenadas por el segundo elemento: {ordenadas}')

# Ejemplo 5 uso de Lambda con reduce()
# Aplica una funcion de forma acumulativa a los elementos de un iterable, reduciendolo a un solo valor
numeros = [1, 2, 3, 4]
producto = reduce(lambda x, y: x*y, numeros)
print(f'Producto de todos los elementos en {numeros}: {producto}')

# Ejemplo 6 uso de Lambda con funciones personalizadas


def resta(x, y): return x - y


print(f'Resta de 10 - 7: {resta(10, 7)}')

# Ejemplo 7 uso de Lambda con funciones integradas (sorted con strings)
nombres = ['Ana', 'Carlos', 'Beatriz', 'David']
ordenados = sorted(nombres, key=lambda nombre: len(nombre))
print(f'Nombres ordenados por longitud: {ordenados}')
