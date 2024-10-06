
def number_check(number):
    if number > 10:
        raise ValueError('El numero debe estar entre 1 y 10')
    print(f'El numero ingresado es {number}')


my_number = int(input('Ingrese un numero del 1 al 10:'))

number_check(my_number)
