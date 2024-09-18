# Calcular el precio final con descuento

# Escribe un programa que calcule el precio final de un producto luego de aplicar un desc del 15% si el precio
# inicial es mayor a 200. Usa un condicional if tradicional para aplicar el desc y muestra el precio final

precio_inicial = int(input('Ingrese el precio sin descuento: '))

if precio_inicial > 200:
    descuento = 0.15
    precio_final = precio_inicial * (1 - descuento)
    print(f'El precio sin descuento: {
          precio_inicial} con descuento del 15% es igual a {precio_final}')
else:
    precio_final = precio_inicial
    print('No aplica descuento')
