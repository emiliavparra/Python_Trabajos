# Los 3 ejemplos de escritura (TXT)

# 1. Modo 'w': Sobre escribe el archivo
with open('modo_w_txt', 'w') as file:
    file.write('Este archivo fue sobreescrito por el modo W')
    file.write('Todo el contenido previo fue eliminado.')
print('Archivo modo_w.txt creado con exito')

# Modo a: Agrega contenido al archivo exsistente
with open('modo_w_txt', 'a') as file:
    file.write('A este archivo se le agrego el final')
    file.write('Todo el contenido previo no fue eliminado.')
print('Archivo modo_a.txt modificado con exito')
