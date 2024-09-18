edades = {
    'Ana': 33,
    'Emilia': 34,
    'Juana': 25
}

# Iterar sobre la clave del diccionario
for clave in edades.keys():
    print(clave)

# Iterar sobre los valores del diccionario
for valor in edades.values():
    print(valor)

# Iterar sobre claves y valores a la vez
for clave, valor in edades.items():
    print(f'La clave es {clave} y el valor es {valor}')
