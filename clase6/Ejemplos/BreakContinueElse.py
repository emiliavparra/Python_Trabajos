# Programa que pide un nro hasta que se ingrese un nro negativo

# Inicializamos la variable suma: esto acumula la suma de los nros positivos ingresados
suma = 0

# Inicializamos un ciclo infinito utilizando while true
while True:
    # Solicitamos al usuario que introduzca un nro
    # La entrada se convierte en nro entero
    entrada = int(input('Introduce un numero (negativo para terminar): '))

    # Verificamos si el nro ingresado es negativo
    if entrada < 0:
        # Si el nro es negativo salimos del ciclo usando break
        break

    # Sumamos el nro positivo ingresado en la variable suma
    suma += entrada

    # Verificamos si el nro ingresado es par
    if entrada % 2 == 0:
        # si el nro es par usamos continue para saltar la impresion y seguir iterando
        continue
    # si el nro es impar se ejecuta esta linea
    print(f'Numero impar ingresado: {entrada}')

else:  # ESTE ELSE NO SE EJECUTA PORQUE HAY UN BREAK
    print(f'El ciclo ha terminado porque se ingreso un nro negativo')

# Mensaje final
print(f'La suma de los nros ingresados es: {suma}')
