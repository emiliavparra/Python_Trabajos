# Verificar el estado de un nro con operador ternario

# Escribe un programa que verifique si un nro es positivo, negativo o cero usando el operador ternario en una sola
# linea de codigo para cada estado y muestra el resultado

numero_a_verificar = int(input('Ingrese un numero: '))

if numero_a_verificar > 0:
    print(f'El numero {numero_a_verificar} es positivo')
elif numero_a_verificar == 0:
    print(f'El numero {numero_a_verificar} es igual a 0')
else:
    print(f'El numero {numero_a_verificar} es negativo')
