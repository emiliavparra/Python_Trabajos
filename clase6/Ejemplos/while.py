# Programa para adivinar un nro secreto

# Definimos el numero secreto

numero_secreto = 7

# Inicializar la variable para alamacenar el nro a adivinar
numero_adivinado = None

# Mensaje inicial
print('Bienvenido al juego. Adivina un numero secreto entre 1 y 10')

# Bucle while que continua hasta que el usuario adivine el nro secreto
while numero_adivinado != numero_secreto:
    # solicitar al usuario que ingrese un numero:
    numero_adivinado = int(input('Ingrese un numero del 1 al 10: '))

    # Comprobar si el nro adivinado es correcto
    if numero_adivinado == numero_secreto:
        print('Has ganado! Fin del juego')
    else:
        print('Intenta de nuevo')

# Otra version

while numero_adivinado != numero_secreto:
    numero_adivinado = int(input('Ingrese un numero: '))
    if numero_adivinado > 7:
        print('Demasiado alto. Intenta de nuevo')
    elif numero_adivinado < 7:
        print('Demasiado bajo. Intenta de nuevo')
    else:
        print('Numero correcto. Has ganado! ')
