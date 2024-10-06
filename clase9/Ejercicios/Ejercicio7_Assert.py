
try:
    # Le pido al usuario que ingrese un numero
    number = int(input('Por favor ingrese un numero: '))
    assert number >= 18
    print(f'El numero ingresado es {number}')  # Si es un numero lo imprime

except AssertionError:  # La excepcion la uso en error de valor, es decir, si ingresa algo que no es un numero
    # En este caso debe imprimir este mensaje
    print('Error. Debes ser mayor de 18 años.')
