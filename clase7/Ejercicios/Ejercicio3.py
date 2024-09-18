# 3. Ejercicio de Sets y Operaciones Básicas
# Escribe un programa que:
# 1. Cree dos sets de números.
# 2. Realice operaciones de unión, intersección y diferencia entre estos
# sets.
# 3. Imprima los resultados de cada operación.

# Pense en escribir set predeterminados pero me animè a pedirlo por programa
# Creo la funcion para hacer los set
def crear_sets(*args):
    set_creado = []
    for numero in args:
        set_creado.append(numero)
    return set_creado


# Hago el primer y segundo set usando la misma funcion
primer_set = crear_sets(1, 2, 3, 4, 5, 6)
segundo_set = crear_sets(7, 8, 9, 10, 11, 12)
print('El primer set creado es:')
print(primer_set)
print()
print('El segundo set creado es:')
print(segundo_set)

# Los convierto a set efectivamente (un paso extra pero queria probar de hacerlo)
primer_set_convertido = set(primer_set)
segundo_set_convertido = set(segundo_set)
# Pruebo imprimir para ver que estàn ok
print(f'El primer set es {primer_set_convertido}')
print(f'El segundo set es: {segundo_set_convertido}')

# Operacion de Union
primer_set_convertido.update(segundo_set_convertido)
# Imprimo el resultado
print(f'Set despues de unir el primer y segundo set: {primer_set_convertido}')

# Operacion de interseccion
primer_set_convertido.intersection_update(segundo_set_convertido)
# Imprimo el resultado
print(f'La interseccion entre el primer y el segundo set es: {
      primer_set_convertido}')

# Operacion de diferencia
segundo_set_convertido.difference_update(primer_set_convertido)
# Imprimo el resultado
print(f'Set despues de la diferencia entre sets: {segundo_set_convertido}')
