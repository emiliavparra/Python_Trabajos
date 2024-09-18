# Ejercicio 3: Anidación Básica de Diccionarios

# Crea un diccionario que represente una persona con las siguientes claves:
# Nombre, edad, direccion  (donde la dirección es otro diccionario con claves: Calle, Ciudad, Código postal)

persona = {
    'nombre': 'Emilia',
    'edad': 33,
    'direccion': {
        'calle': 'Palestina',
        'ciudad': 'CABA',
        'codigo postal': 1182
    }
}

# Imprime la ciudad de la dirección
direccion = persona.get('direccion')
ciudad_direccion = direccion.get('ciudad')

print('La ciudad donde vive es: ', ciudad_direccion)
