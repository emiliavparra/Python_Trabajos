# Creamos un diccionario

persona = {
    'nombre': 'Alejandra',
    'edad': 30,
    'ciudad': 'Merida',
    'profesion': 'veterinaria'
}

# imprimir dicc original
print('Diccionario original: ', persona)
valor_eliminado = persona.popitem()

# Imprimir sin par borrado por popitem
print('Ultimo par borrado:', valor_eliminado)
print('Diccionario actualizado: ', persona)
