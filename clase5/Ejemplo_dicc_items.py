# Creamos un diccionario
persona = {
    'nombre': 'Alejandra',
    'edad': 30,
    'ciudad': 'Merida'

}

# Usamos el metodo
pares_clave_valor = persona.items()

print('Las pares clave/valor son: ', pares_clave_valor)

pares_clave_mejor = list(pares_clave_valor)
print('Mas lindo: ', pares_clave_mejor)
