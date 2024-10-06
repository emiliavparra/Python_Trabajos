# Los 3 modos de escritura en archivos

# 1. Modo 'w': Sobre escribe el archivo
with open('modo_w.txt', 'w') as file:
    file.write('Este archivo fue sobreescrito por el modo \'w\'.\n')
    file.write('Todo el contenido previo fue eliminado.\n')
print('Archivo modo_w.txt creado con exito')

# Modo a: Agrega contenido al archivo exsistente
with open('modo_a.txt', 'a') as file:
    file.write('Este texto se agrego al final del archivo usando el modo \'a\'.\n')
    file.write('Todo el contenido previo no fue eliminado.\n')
print('Archivo modo_a.txt creado o modificado con exito')

# Modo'x': Crear un archivo nuevo
# Nota: Si el archivo ya existe, este codigo fallarà y no se creara el archivo
with open('modo_x.txt', 'x') as file:
    file.write('Este archivo fue creado usando el modo \'x\'.\n')
    file.write('Falla si el archivo ya existe. \n')

print('Archivo modo_x.txt creado con exito')
