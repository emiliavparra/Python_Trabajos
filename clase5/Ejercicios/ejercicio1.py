# Ejercicio 1: Crear y Acceder a un Diccionario Básico

# Crea un diccionario que contenga la siguiente información sobre un libro:
# Titulo, autor, año de publicacion, genero

dicc_libro = {
    'titulo': 'El señor de los anillos: la comunidad del anillo',
    'autor': 'JRR Tolkien',
    'año de publicacion': 1954,
    'genero': 'fantastico'
}

# Accede e imprime cada uno de estos valores usando las claves correspondientes

titulo = dicc_libro.get('titulo')
autor = dicc_libro.get('autor')
año_de_publicacion = dicc_libro.get('año de publicacion')
genero = dicc_libro.get('genero')

print('El titulo del libro es: ', titulo)
print('El autor del libro es: ', autor)
print('El año de publicacion del libro es: ', año_de_publicacion)
print('El genero del libro es: ', genero)
