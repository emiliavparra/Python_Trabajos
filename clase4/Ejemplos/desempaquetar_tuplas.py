# Ejemplo 1: Desempaquetado basico de tuplas
# Crear una tupla con varios tipos de datos
mi_tupla = (1, 'Python', 3.14)
# Desempaquetar tupla
numero, lenguaje, pi = mi_tupla
# Mostrar el valor de cada variable despues del desempaquetamiento
print('Numero: ', numero)
print('Lenguaje: ', lenguaje)
print('Pi: ', pi)

# Ejemplo 2: Nro de variables no coincice con el nro de
# Crear una tupla con tres elementos
mi_tupla = (1, 'python', 3.14)
# Intentar desempaquetar en dos variables:
# Causa error
# Too many values to unpack (two were given)

#  Ejemplo 3:
# Desempaquetar con el operador *
# Crear una tupla con varios elmentos
mi_tupla = (1, 'python', 3.14, 'Tuplas', 'Desempaquetado')
# Desempaquetar con el operador *
primer_elemento, *resto = mi_tupla
# Mostrar los resultados
print('Primer elemento: ', primer_elemento)
print('Resto', resto)
