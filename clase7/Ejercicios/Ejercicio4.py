# 4. Ejercicio de while con Condiciones y Contadores
# Desarrolla un programa que:
# 1. Use un bucle while para generar números de la serie de Fibonacci.
# 2. Continúe generando números hasta que el número actual sea mayor o igual a 100.
# 3. Imprima la serie de Fibonacci generada.


def serie_fibonacci():
    a, b = 0, 1
    lista_serie = []
    while a <= 100:
        lista_serie.append(a)
        a, b = b, a + b

    return lista_serie


print(serie_fibonacci())

fibonacci = serie_fibonacci(1, 1)
print(f'La lista de la serie Fibonacci es: {fibonacci}')
