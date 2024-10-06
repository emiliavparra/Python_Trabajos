# El bloque with se usa para envolver la ejecucion de un bloque de codigo dentro de metodos definidos por un contexto especifico
# Garantiza que los recursos sean limpiados correctamente cuando se sale del bloque, incluso si ocurre una excepcion

# EJEMPLO SINTAXIS:
# with expression as variable:
#       Bloque de codigo

# expression: Expresion que devuelve un objeto que implementa los metodos __enter__ y __exit__
# variable: Variable que recibe el valor devuelto por __enter__

# EJEMPLO:

# with se ultiliza para abrir el archivo en modo escritura. El archivo se cierra automaticamente al final del bloque
with open('archivo.txt', 'w') as file:
    # Incluso si ocurre una excepcion dentro del bloque
    file.write('Hola mundo!')
