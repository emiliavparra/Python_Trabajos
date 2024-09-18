# 1. Ejercicio de List Comprehension con range y for
# Crea un programa que:
# 1. Genere una lista de números del 1 al 10 usando range.
# 2. Cree una nueva lista que contenga el cuadrado de cada número
# solo si el número es impar.

lista_numeros = [x+1 for x in range(10)]
print(f'La lista de numeros usando range es: {lista_numeros}')

nueva_lista = [x**2 for x in range(10) if x % 2 != 0]
print(f'La nueva lista que da el cuadrado de los impares (1,3,5,7,9) es: {
      nueva_lista}')
