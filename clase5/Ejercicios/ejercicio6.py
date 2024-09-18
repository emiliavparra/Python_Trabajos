# Ejercicio 6: Anidación Compleja de Diccionarios y Listas

# Crea un diccionario que contenga información sobre una escuela. La escuela tiene:
# Nombre, Año de fundación
# Lista de clases, donde cada clase es un diccionario con:
# Nombre de la clase, Lista de estudiantes, donde cada estudiante es un diccionario con:
# Nombre
# Edad

mi_escuela = {
    'nombre': 'Instituto ADA',
    'año de fundacion': 2010,
    'lista de clases': {
        'nombre de la clase 1': 'Introduccion a Python',
        'lista_estudiantes_Python': {
            'nombre_1': 'Emilia Parra',
            'edad_1': 33,
            'nombre_2': 'Juana Perez',
            'edad_2': 28}},
        'nombre de la clase 2': 'Backend',
        'lista_estudiantes_Backend': {
            'nombre_1': 'Agustina Gonzalez',
            'edad_1': 31,
            'nombre_2': 'Romina Copani',
            'edad_2': 27
    }

}

# print(mi_escuela)

# Imprime el nombre del primer estudiante de la primera clase
primer_estudiante = mi_escuela['lista de clases']['lista_estudiantes_Python']['nombre_1']
print(f'El primer estudiante de la primer clase es: {primer_estudiante}')
# nombre_primer_estudiante = primer_estudiante[]

# segundo_producto = lista_tienda[1]
# print(segundo_producto)
# nombre_segundo_producto = segundo_producto['nombre']
# precio_segundo_producto = segundo_producto['precio']
# print(f'El nombre del segundo producto es {
#       nombre_segundo_producto} y el precio es {precio_segundo_producto}')
