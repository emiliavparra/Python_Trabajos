# Ejercicio 9: Buscar y Imprimir la Edad de un Estudiante en un Diccionario Anidado

# 1. Crea un diccionario que represente una clase con los siguientes datos:
# nombre_clase
# estudiantes, que es una lista de diccionarios con información de cada estudiante (nombre y edad).

# 2. Escribe una función que busque la edad de un estudiante dado su nombre usando el índice de la
# lista en lugar de bucles (suponiendo que conoces el índice).

# 3. Imprime la edad del estudiante buscado.

# Primero creo el diccionario
mi_diccionario = {
    'nombre_clase_1': 'matematicas',
    'estudiantes_clase_1': [
        {
            'nombre': 'Emilia Parra',
            'edad': 33
        },
        {
            'nombre': 'Juan Lopez',
            'edad': 32
        },
        {
            'nombre': 'Carlos Perez',
            'edad': 34
        }
    ]
}

# Compruebo que estè bien el diccionario creado
print(mi_diccionario)

# Busco la edad del segundo estudiante de la lista
buscar_edad = mi_diccionario['estudiantes_clase_1'][1]['edad']

# Imprimo la edad
print(f'La edad del estudiante pedido es: {buscar_edad}')
