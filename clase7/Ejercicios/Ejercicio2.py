# 2. Ejercicio Integrador

# Desarrolla un programa que haga lo siguiente:
# 1. Usar un bucle for con range para iterar sobre los números del 1 al 20.
# 2. Usar continue para saltar los números divisibles por 3.
# 3. Usar break para detener la iteración si se encuentra un número mayor que 15.
# 4. Crear un set con los números restantes y verificar si algún número es par.

lista_numeros = []

for x in range(20):
    if x % 3 == 0:
        continue
    if x > 15:
        break
    else:
        lista_numeros.append(x)

print(lista_numeros)
nueva_lista = set(lista_numeros)
print(nueva_lista)

for y in nueva_lista:
    if y % 2 == 0:
        print(f'El numero {y} es par')
    else:
        print(f'El numero {y} es impar')
