# Alcance global y local en Python

# Variable global
x = 20


def funcion_local():
    x = 10  # x aca es una variable local
    print(f'El valor de x dentro de la funcion local es {x}')


def funcion_global():
    # para modificar una variable global se usa la palabra reservada global
    global x
    x = 30
    print(f'Valor de x dentro de la funcion global es {x}')


# Llamada a las funciones
funcion_local()  # Muestra el valor de X dentro de la funcion local
# print (x)
# Esto va a causar error porque x esta definido en el alcance local

funcion_global()
print(f'El valor de x fuera de la funcion es {x}')
# Muestra el valor de x despues de modificarlo en la funcion global
