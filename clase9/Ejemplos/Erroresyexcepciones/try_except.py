# try:
# Codigo que podria causar una excepcion
# except <ExceptionType> as e:
# Codigo para manejar la excepcion

# Ejemplo de lo de arriba
try:
    number = int(input('Introduce un numero: '))
    result = 10 / number
    print(f'Resultado: {result}')
except ZeroDivisionError:
    print('Error: No se puede dividir por cero')
except ValueError:
    print('Error: Entrada no valida. Introduce un numero entero')
