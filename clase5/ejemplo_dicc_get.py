#  Crear un diccionario
persona = {
    'nombre': 'Veronica',
    'edad': 25,
    'ciudad': 'Buenos Aires'
}

# Usar el metodo get para acceder
nombre = persona.get('nombre')
edad = persona.get('edad')
ciudad = persona.get('ciudad')

# imprimir
print('Nombre: ', nombre)
print('Edad: ', edad)
print('Ciudad: ', ciudad)

# Usar get con un valor predeterminado si la clave no existe
pais_con_valor_prederminado = persona.get('pais', 'No especificado')
print('Pais (con valor predeterminado): ', pais_con_valor_prederminado)
