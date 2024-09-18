# Ejemplo 1 funcion que usa ARGS
def sumar_numeros(*args):
    # Esta funcion acepta un nro variable de argumentos numericos y retorna su suma
    # parametros args: un nro variable de argumentos numericos
    # return: la suma de los argumentos

    total = 0
    for numero in args:
        total += numero
    return total


# Llamado a la funcion con diferentes numeros de argumentos
print('Ejemplo de args:')
print(f'Suma de 1,2,3: {sumar_numeros(1, 2, 3)}')
print(f'Suma de 4,5,6,7,8: {sumar_numeros(4, 5, 6, 7, 8)}')
print()

# Ejemplo 2 que usar KWARGS


def mostrar_detalles(**kwargs):
    # Esta funcion acepta un nro variable de argumentos nombrados (clave:valor) y los imprime
    # Parametros kwargs: un nro variable de argumentos nombrados(clave:valor)
    print('Detalles:')
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')


# Llamado a la funcion con diferentes argumentos nombrados
print('Ejemplo de Kwargs:')
mostrar_detalles(nombre='Ana', edad=30, ciudad='Madrid')
print()

# Ejemplo 3 combinado de ARGS Y KWARGS


def mostrar_info_completa(*args, **kwargs):
    # Esta funcion combina argumentos no nombrados y nombrados y los imprime
    # Parametros args: Argumentos no nombrados
    # Parametros kwargs: Argumentos nombrados (clave:valor)

    print('Argumentos no nombrados:')
    for arg in args:
        print(arg)

    print('\nArgumentos nombrados:')
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')


# Llamado ala funcion combinada
print('Ejemplo combinado de args y kwargs:')
mostrar_info_completa(1, 2, 3, nombre='Ana', edad=30, ciudad='Madrid')
