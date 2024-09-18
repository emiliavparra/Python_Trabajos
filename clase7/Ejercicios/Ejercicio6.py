# 6. Ejercicio de List Comprehension y range
# Crea un programa que:
# 1. Use range para generar una lista de números del 1 al 15.
# 2. Utilice list comprehension para crear una nueva lista con el cubo
# de los números pares.

# Uso range para crear la lista del 1 al 15
# Lo que le digo aca es que si esta dentro del range, x sume 1 hasta llegar a 15
lista_numeros = [x + 1 for x in range(15)]
print(lista_numeros)

# aca le doy la condicion de par al final
lista_nueva = [x ** 3 for x in range(15) if x % 2 == 0]
# le pido que si es par el nuevo valor sea al cubo
print(lista_nueva)
