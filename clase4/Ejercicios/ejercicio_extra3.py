# Verificacion de numeros pares e impares con operador ternario

# Escribe un programa que verifique si un num es par o impar usando el operador ternario. Imprime 'par'
# si el nro es divisible por 2 e 'impar' si no lo es

numero_a_verificar = int(input('Ingrese un numero: '))

if numero_a_verificar % 2 == 0:
    print(f'El numero {numero_a_verificar} es par')
else:
    print(f'El numero {numero_a_verificar} es impar')
