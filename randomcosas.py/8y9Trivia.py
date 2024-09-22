

# 1ra funcion: BIENVENIDA y funcion MADRE? tal vez


def funcion_madre():
    import random

    def funcion_bienvenida():
        # Mensaje inicial
        print(
            "¡Hola!. Antes de comenzar por favor ingresa la siguiente información personal:")
        nombre = input("Nombre: ")  # Pido al jugador que ingrese el nro
        edad = int(input("Edad: "))  # Pido al jugador que ingrese la edad
        return nombre, edad

        edad_minima = 18  # Defino en esta funcion que la edad minima es 18
        # Utilizo la funcion para validar la edad usando 2 argumentos dados
        if validar_edad(edad, edad_minima):
            # Si es True da el mensaje
            print("\n¡Bienvenida al juego de Trivia en Python!")
        else:
            # Si es false termina el juego
            print(f'Lo siento. Debes ser mayor de edad para jugar')
            # Imprimo las instrucciones de la funcion texto_bienvenida_explicaciones
            print(texto)
    # 2da funcion: VALIDAR EDAD

    # Le doy dos parametros (uno x la edad que ingresa el jugador, otro por la edad necesaria)
    def validar_edad(x, b):
        return x >= b  # Si la edad que ingresa el jugador es igual o mayor a la necesaria, retorna True

    # Pruebo que funcionen
    prueba = funcion_bienvenida()
    edad_a_validar = validar_edad(33, 18)

    # 3ra funcion: Texto bienvenida e instrucciones para el juego

    def texto_bienvenida_explicaciones():
        print('Esperamos que aprendas y también te diviertas al responder estas preguntas de Programación\nEl juego funcionará de la siguiente manera: te presentaremos una serie de preguntas que retarán tus conocimientos de Programación en Python\nLas preguntas serán de opción múltiple y tu ingresarás el inciso que creas que sea correcto\nLee detenidamente cada pregunta y tómate tu tiempo para responder\nAl final, podrás verificar cuántas preguntas acertaste\nTe deseamos el mejor de los éxitos.¡Comencemos!\nLee cada pregunta y responde SOLAMENTE con el NÚMERO del inciso que creas correcto:')
    # Aca pongo una instruccion seguida de la otra con un salto de linea \n para que se lean una debajo de otra

    texto = texto_bienvenida_explicaciones()  # Llamo la funcion

    def preguntas_juego(preguntas):
        return preguntas_respuestas

    preguntas_respuestas = [
        ("¿Qué es Python?\n 1) Un lenguaje de programación. \n 2) Un tipo de serpiente. \n 3) Un tipo de comando.", 1),
        ("¿Qué es una variable en Python?\n 1) Un dato anidado. \n 2) Un espacio que almacena un valor. \n 3) Un diccionario.", 2),
        ("¿Cuál es un dato básico en Python?\n 1)'n\' \n 2) # \n 3) int", 3),
        ("¿Cómo se define una lista en Python?\n 1) () \n 2) [] \n 3) {} ", 2),
        ("¿Cómo se define una lista inmutable en Python?\n 1) () \n 2) [] \n 3) *", 1),
        ("En Python las Tuplas son Mutables.\n 1) Verdadero. \n 2) Falso.", 2),
        ("¿Para qué se utiliza print() en Python?\n 1) Para conectar tu impresora. \n 2) Para hacer una lista. \n 3) Muestra información en la consola.", 3),
        ("¿Cuál es el operador de asignación en Python?\n1) = \n2) + \n3) *", 1)
    ]


funcion_madre()
