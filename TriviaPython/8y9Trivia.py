import random

# 1ra funcion: BIENVENIDA y funcion MADRE? tal vez


def funcion_bienvenida():
    # Mensaje inicial
    print("¡Hola!. Antes de comenzar por favor ingresa la siguiente información personal:")

    nombre = input("Nombre: ")  # Pido al jugador que ingrese el nro
    edad = int(input("Edad: "))  # Pido al jugador que ingrese la edad
    edad_minima = 18  # Defino en esta funcion que la edad minima es 18
    # Utilizo la funcion para validar la edad usando 2 argumentos dados
    if validar_edad(edad, edad_minima):
        # Si es True da el mensaje
        print("\n¡Bienvenida al juego de Trivia en Python!")
        print()
    else:
        # Si es false termina el juego
        print(f'Lo siento. Debes ser mayor de edad para jugar')

# 2da funcion: VALIDAR EDAD


def validar_edad(x, b):  # Le doy dos parametros (uno x la edad que ingresa el jugador, otro por la edad necesaria)
    return x >= b  # Si la edad que ingresa el jugador es igual o mayor a la necesaria, retorna True


# Pruebo que funcionen
prueba = funcion_bienvenida()
edad_a_validar = validar_edad(33, 18)

# 3ra funcion: Texto bienvenida e instrucciones para el juego


def texto_bienvenida_explicaciones():
    return 'Esperamos que aprendas y también te diviertas al responder estas preguntas de Programación\nEl juego funcionará de la siguiente manera: te presentaremos una serie de preguntas que retarán tus conocimientos de Programación en Python\nLas preguntas serán de opción múltiple y tu ingresarás el inciso que creas que sea correcto\nLee detenidamente cada pregunta y tómate tu tiempo para responder\nAl final, podrás verificar cuántas preguntas acertaste\nTe deseamos el mejor de los éxitos.¡Comencemos!\nLee cada pregunta y responde SOLAMENTE con el NÚMERO del inciso que creas correcto:'
# Aca pongo una instruccion seguida de la otra con un salto de linea \n para que se lean una debajo de otra


instrucciones_bienvenida = texto_bienvenida_explicaciones()  # Aca llamo la funcion 3
print(instrucciones_bienvenida)  # Imprimo el resultado
