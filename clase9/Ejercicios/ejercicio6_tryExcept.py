
# Empiezo el programa con try
try:
    # Le pido al usuario que ingrese un numero
    number = int(input('Por favor ingrese un numero: '))
    print(f'El numero ingresado es {number}')  # Si es un numero lo imprime
except ValueError:  # La excepcion la uso en error de valor, es decir, si ingresa algo que no es un numero
    # En este caso debe imprimir este mensaje
    print('El valor ingresado no es un numero. Por favor ingrese un numero')
