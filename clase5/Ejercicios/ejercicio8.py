# Ejercicio 8: Modificar un Valor en un Diccionario Anidado
# 1. Crea un diccionario que contenga información sobre una tienda de libros, con las siguientes claves:
# nombre_tienda libros, que es una lista de diccionarios, donde cada diccionario representa un libro
# con claves titulo y precio.
# 2. Cambia el precio del segundo libro en la lista a un nuevo valor (por ejemplo, 15.99).
# 3. Imprime el título y el precio del segundo libro después de la modificación.

# Primero creo el diccionario:
tienda_de_libros = {
    'nombre_tienda': 'La hojita',
    'libros_lista': [
        {
            'titulo_1': 'El Hobbit',
            'precio_titulo_1': 300
        },
        {
            'titulo_2': 'El Silmarilion',
            'precio_titulo_2': 410
        },
        {
            'titulo_3': 'El señor de los anillos',
            'precio_titulo_3': 700
        }
    ]
}

# Ahora cambio el precio del segundo libro

tienda_de_libros['libros_lista'][1]['precio_titulo_2'] = 375

# Imprimo el resultado. Ahora en vez de 410 cuesta 375
print(tienda_de_libros)
