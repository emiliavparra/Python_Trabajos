# Ejemplo 1: Callback en una operacion basica
# Definimos las funciones de callback
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b

# Funcion que recibe otra funcion como callback


def operar(a, b, funcion_callback):
    resultado = funcion_callback(a, b)
    print(f'El resultado de la operacion es: {resultado}')


# Uso de la funcion operar con diferentes callbacks
print('Ejemplo de callback simple:')
operar(5, 3, sumar)  # Resultado de la operacion es 8
operar(5, 3, restar)  # Resultado de la operacion es 2

# Uso de una lambda como callback
operar(5, 3, lambda a, b: a*b)  # Resultado de la operacion es 15
operar(5, 3, lambda a, b: a/b)  # Resultado de la operacion es 1.6666...
