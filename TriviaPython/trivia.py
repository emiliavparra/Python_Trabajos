# Hola, Bere y Emi! Aquí pondré algunos puntos de la tarea, siéntanse libres de cambiar cualquier cosa o decirme si algo
# no se entiende o no está correcto. Iré explicando de la forma más detallada posible para que se entienda lo que voy
# haciendo. ¡Sí podemos!

# Este comando pertenece al Paso 4 de la Consigna: importar el módulo random.
import random

# Paso 2: Crear el archivo y escribir un comentario inicial de lo que tratará el Programa.

# Proyecto Número 1: Crea tu Primer Juego de Trivia en Python.
# Curso: Python Intensivo.
# Profesora: Bauque Bernardita.
# Alumnas: Emi Parra, Berenice Castro y María Martha Ulloa.

# Paso 3: Estructura Básica del Juego

# Define el flujo principal del programa: Tu programa comenzará pidiendo al usuario su nombre y edad.
print("¡Hola!. Antes de comenzar por favor ingresa la siguiente información personal:")
input("Nombre: ")
# Aquí guardaré la información en la variable "Edad" para después verificar si es mayor de 18 años.
edad = int(input("Edad: "))

# Verifica si el jugador cumple con la edad mínima para jugar (18 años). Si no cumple, el juego deberá terminar.
edad_minima = 18  # Variable de la edad mínima para jugar

# Lo que haré a continuación es establecer un programa que verifique la edad.
if edad >= edad_minima:
    # Le damos la Bienvenida al usuario si su edad es mayor o igual a 18.
    print("\n¡Bienvenida al juego de Trivia en Python!")
else:
    # Si la edad del usuario es menor a 18 este comando terminan la ejecución del programa.
    exit()

# Configura la bienvenida del juego:
print("Esperamos que aprendas y también te diviertas al responder estas preguntas de Programación.")
print("El juego funcionará de la siguiente manera: te presentaremos una serie de preguntas que retarán tus conocimientos de Programación en Python.")
print("Las preguntas serán de opción múltiple y tu ingresarás el inciso que creas que sea correcto.")
print("Lee detenidamente cada pregunta y tómate tu tiempo para responder.")
print("Al final, podrás verificar cuántas preguntas acertaste.")
print("Te deseamos el mejor de los éxitos.¡Comencemos!")
print("\nLee cada pregunta y responde SOLAMENTE con el NÚMERO del inciso que creas correcto:")

# Paso 5: Crear las preguntas del juego

# Usa una lista para almacenar las preguntas, y asocia cada pregunta con su respuesta correcta.
# Aquí ustedes me dirán chicas. Se me hace más sencillo incluir en la pregunta las opciones de respuesta.
# El jugador deberá ingresar mediante input() el número del inciso correcto.
# El hecho de que la entrada sea un número pienso que nos puede ayudar a simplificar el conteo de respuestas correctas.
# De igual manera modifiquen las preguntas como consideren correcto.

# Organiza las preguntas y respuestas en una estructura de datos:
# Usa tuplas para guardar cada pregunta junto con su respuesta correcta. Coloca estas tuplas dentro de una lista.
preguntas_respuestas = [
    ("¿Qué es Python? 1) Un lenguaje de programación. 2) Un tipo de serpiente. 3) Un tipo de comando.", 1),
    ("¿Qué es una variable en Python? 1) Un dato anidado. 2) Un espacio que almacena un valor. 3) Un diccionario.", 2),
    ("¿Cuál es un dato básico en Python? 1) n\. 2) #. 3) int.", 3),
    ("¿Cómo se define una lista en Python? 1) (). 2) []. 3) "".", 2),
    ("¿Cómo se define una lista inmutable en Python? 1) (). 2) []. 3) *.", 1),
    ("En Python las Tuplas son Mutables. 1) Verdadero. 2) Falso.", 2),
    ("¿Para qué se utiliza print() en Python? 1) Para conectar tu impresora. 2) Para hacer una lista. 3) Muestra información en la consola.", 3),
    ("¿Cuál es el operador de asignación en Python? 1) =. 2) +. 3) *.", 1)
]

# Mezclar las preguntas para que aparezcan en un orden diferente cada vez que jueguen:
# Usamos esa función para mezclar aleatoriamente los elementos de la lista. Es este caso, el orden de las preguntas.
random.shuffle(preguntas_respuestas)
# print(preguntas_respuestas) # Nos muestra las preguntas y respuestas cada vez en un orden diferente.

# Paso 6: Mostrar las preguntas al jugador.
# ATENCIÓN: En este paso falta "Controlar los intentos fallidos del jugador".

# Contador de respuestas correctas
aciertos = 0
# Contador de errores consecutivos (3 maximo consecutivos o se acaba el juego. Si contesta bien vuelve a 3)
errores_consecutivos = 3

# Usa un bucle for para mostrar cada pregunta al jugador:
for pregunta, respuesta_correcta in preguntas_respuestas:
    if errores_consecutivos == 0:
        print('Te quedaste sin intentos. Vuelve a empezar')
        break  # Si errores consecutivos llega a 0, se deja de ejecutar
    print(pregunta)  # Muestra las preguntas con sus tres posibles respuestas.
    # El jugador debe ingresar el número del inciso que crea que es correcto.
    tu_respuesta = int(input("Tu respuesta es: "))

    # Paso 7: Validar respuestas: Compara la respuesta del jugador con la respuesta correcta.
    if tu_respuesta == respuesta_correcta:
        print("¡Correcto!\n")
        aciertos += 1  # Aumenta en 1 el contador de aciertos.
        errores_consecutivos = 3  # si responde correctamente el contador de errores vuelve a 3
        continue  # si respondes bien continua con la que sigue
    else:
        # Si la respuesta es incorrecta te muestra el resultado correcto.
        # Y le resta un intento de los 3 consecutivos que tiene el usuario
        errores_consecutivos -= 1
        print(f"Incorrecto. El inciso correcto es el: {
              respuesta_correcta}. Te queda {errores_consecutivos} intentos\n")

# Paso 8: Crear Funciones.
