# Creamos un diccionario

persona = {
    'nombre': 'Alejandra',
    'edad': 30,
    'ciudad': 'Merida'
}

# Usamos el metodo POP xa eliminar la clave 'edad'
# y obtener su valor

valor_eliminado = persona.pop('edad')

# Mostrar
print('El valor eliminado es: ', valor_eliminado)
print('El diccionario resultante es: ', persona)

# Usar POP con una clave que no existe
# y un valor x defecto

valor_inexistente = persona.pop('pais', 'no especificado')
print('Valor cuando la clave no existe: ', valor_inexistente)
