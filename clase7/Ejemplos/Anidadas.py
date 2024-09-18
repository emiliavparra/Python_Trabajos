# Ejemplo 1: Funcion basica anidada

# Funcion externa que recibe un parametro x y define una funcion interna
def funcion_externa(x):
    # Parametros x: Valor entero para el calculo
    # Return: resultado de la funcion interna llamada con 'x'
    def funcion_interna(y):  # Funcion interna que recibe un parametro 'y' y lo suma a 10
        # Parametros y: Valor entero que se suma a 10
        # Return:Valor entero resultante de la suma
        return y + 10

    return funcion_interna(x)  # Llamada a la funcion interna con el valor X


# Llamado a la fucnion externa
resultado = funcion_externa(5)
print(f'Resultado de la funcion externa(5): {resultado}')  # Imprime 15

# Ejemplo 2: Cierre (Closure)


def crear_multiplicador(factor):
    # Crea una funcion que multiplica su entrada por un 'factor' especifico
    # Parametro factor:valor por el que se multiplicaran los argumentos de la funcion interna
    # Return:Funcion que multiplica su entrada por el 'factor'
    def multiplicar(x):
        # Funcion interna que multiplica 'x' por 'factor'
        # Paremetro x: Valor entero a multiplicar
        # Return:Resultado de la multiplicacion
        return x * factor
    return multiplicar


# Crear dos funciones multiplicadoras con diferentes factores
duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

# Usar las funciones multiplicadoras
print(f'Duplicar 10: {duplicar(10)}')
print(f'Triplicar 10: {triplicar(10)}')
