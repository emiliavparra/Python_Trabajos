# Assert verifica que ciertas condiciones se cumplan durante la ejecucion del programa

# EJEMPLO assert condition, 'Mensaje de error'

# condition: La condicion que se verifica. Si es false, se lanza una excepcion
# 'Mensaje de error': Mensaje opciones que se muestra si la condicion es falsa

# EJEMPLO DE MAS ARRIBA

def divide(a, b):
    assert b != 0, 'Error: la division por cero no esta permitida'
    return a/b


print(divide(10, 2))
print(divide(10, 0))  # Lanza AssertionError
