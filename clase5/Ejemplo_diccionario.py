# Ejemplo de diccionario
# LA CLASE NO SE MODIFICA. El valor si

diccionario_vacio = {}
print('Ejemplo de un diccionario vacio: ', diccionario_vacio)

# Eejemplo basico de un dicc
persona = {
    'nombre': 'Maria',
    'edad': 30,
    'casada': False,
    'hijos': ['Ana', 'Luis'],  # el valor es asi porque es una lista
    'direccion': {            # el valor es otro dicc
        'calle': 'La gran via',
        'ciudad': 'Madrid'
    }
}
print('Ejemplo de diccionario: ', persona)

# Ej de dicc con valores de distinto tipo
diccionario_mixto = {
    'nombre': 'Alejandra',
    1: [2, 3, 4],  # clave es un entero y valor es un string
    (2, 3): 'tupla como clave'  # clave es una tupla
}
print('Ejemplo dicc mixto: ', diccionario_mixto)
