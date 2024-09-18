# Crear un diccionario con info de una persona
persona = {
    'nombre': 'Catalina',
    'edad': 33,
    'ciudad': 'Bogota'
}

# Acceder a los elementos usando []
nombre = persona['nombre']
edad = persona['edad']
ciudad = persona['ciudad']

# Imprimir los valores de c/u
print('Nombre: ', nombre)
print('Edad: ', edad)
print('Ciudad: ', ciudad)

# Intento acceder a una que no existe
# print(persona['mi pais'])
# va a dar KEY ERROR
