# Ejercicio 2: Modificar y Eliminar Elementos de un Diccionario

# Usando el diccionario del ejercicio anterior, actualiza el año de publicación a 1968.

dicc_libro = {
    'titulo': 'El señor de los anillos: la comunidad del anillo',
    'autor': 'JRR Tolkien',
    'año de publicacion': 1954,
    'genero': 'fantastico'
}
# Imprimi el diccionario original
print('El diccionario sin cambios es: ', dicc_libro)
# Hago el cambio e imprimo el diccionario modificado
dicc_libro['año de publicacion'] = 1968
print('El diccionario actualizado es: ', dicc_libro)

# Elimina el género del diccionario
del dicc_libro['genero']
print('El diccionario con genero eliminado: ', dicc_libro)

# Imprime el diccionario después de cada operación.
