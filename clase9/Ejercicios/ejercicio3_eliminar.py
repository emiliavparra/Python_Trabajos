
# Primero importo el modulo 'os' para poder interactuar con el s.o
import os
# Defino el nombre del archivo que voy a eliminar
file_name = 'new_file_x.txt'

# Tengo que comprobar si existe y borrarlo si es asi. Uso la funcion os.path.exists y despues (si existe) os.remove
if os.path.exists(file_name):
    os.remove(file_name)
    print(f'El archivo {file_name} fue eliminado')
else:
    print(f'El archivo {file_name} no existe')
