# 2. Ejercicio de while y for

# Desarrolla un programa que haga lo siguiente:
# 1. Usar un bucle while para pedir al usuario que ingrese números hasta que se ingrese el número 0.
# 2. Usar un bucle for para calcular la suma de los números ingresados, excluyendo el 0.

# Primero le doy la bienvenida al usuario al programa
print('Bienvenido! ')

# Creo una lista vacion donde se van a ir sumando los numeros ingresados:
lista_numeros = []

# Hago el bloque while para que se sume o se corte si se ingresa 0
while True:
    numero_pedido = int(
        input('Ingrese un numero (presione 0 para terminar): '))
    if numero_pedido == 0:
        break
    else:
        lista_numeros.append(numero_pedido)

# hago el bloque for para calcular la suma
# creo la variable de la suma empezando en 0
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros += numero

print(f'Haz apretado 0. La suma de todos los numeros ingresados es {
      suma_numeros}')
