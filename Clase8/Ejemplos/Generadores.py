# EJEMPLO 1 - Basico de un generador
# generador que produce numeros del 1 al 5:
# Definicion del generador:

def contador():
    # Itera sobre los numeros del 1 al 5
    for i in range(1, 6):  # Itera sobre los numeros del 1 al 5, no incluye al 6
        yield i  # Produce el valor de 'i' y pausa la ejecucion


# Crear una instancia del generador
gen = contador()  # 'gen' es un objeto generador

# Iterar sobre los valores producidos por el generador
for numero in gen:  # Itera sobre los valores producidos por el generador Gen
    print(numero)  # Imprime cada nro producido por el generador

# EJEMPLO 2 con generadores y yield
# Un generador puede contener multiples yield y puede ser reanudado desde el ultimo yield si se llama a next()

# Definicion del generador para la secuencia de fibonacci:


def fibonacci():
    a, b = 0, 1  # Inicializa los primeros dos nros de la secuencia
    while True:  # Ciclo infinito para generar los nros de Fibonacci
        yield a  # Produce el valor de a y pausa la ejecucion
        a, b = b, a + b  # Actualiza a y b para la siguiente iteraciòn


# Crear una instancia para el generador
gen = fibonacci()  # gen es un objeto generador que produce nro de Fibonacci
# Obtener los primeros 10 numeros de Fibonacci
for _ in range(10):
    print(next(gen))  # Obtiene el siguiente nro de la secuencia y lo imprime
