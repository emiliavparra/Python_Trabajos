# Definicion de una funcion que usa parametros posicionales, con nombre y predeterminados
def presentar_persona(nombre, edad, ciudad='Desconocida', profesion='Desconocida'):
    # Presenta informacion sobre una persona
    # Parametros:
    # Nombre: (str) nombre de la persona
    # Edad: (int) edad de la persona
    # Ciudad: (str) ciudad donde vive (opcional)
    # Profesion: (str) de que trabaja (opcional)

    print(f'El nombre es: {nombre}')
    print(f'La edad es: {edad}')
    print(f'Vive en la ciudad: {ciudad}')
    print(f'Su profesion es: {profesion}')
    print()  # Linea en blanco para separar la salida de diferentes llamados a la funcion


# Ejemplos de llamada a la funcion
# Usando parametros posicionales
print('Ejemplo con argumentos posicionales: ')
# Ciudad y profesion van a usar valor predeterminado
presentar_persona('Ana', 30)

# Usando posicional y con nombre
print('Ejemplo con argumentos posicionales y con nombres:')
presentar_persona('Luis', 25, ciudad='Madrid', profesion='Ingeniero')
# nombre y edad son posicionales, ciudad y profesion son con nombre

# Usando todos los argumentos con nombre
print('Ejemplo usando todos los argumentos con nombre:')
presentar_persona(nombre='Marta', edad=28,
                  ciudad='Barcelona', profesion='Diseñadora')
# Todos los argumentos son con nombre

# Usando argumentos posicionales y uno con nombre
print('Ejemplo con argumentos posicionales y uno con nombre:')
presentar_persona('Carlos', 35, profesion='Profesor')
# nombre y edad son posicionales, profesion es con nombre, ciudad es predeterminado
