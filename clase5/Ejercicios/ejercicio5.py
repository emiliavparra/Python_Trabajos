# Ejercicio 5: Diccionario dentro de una Lista

# Crea una lista de diccionarios donde cada diccionario representa un producto en una tienda, con claves:
# Nombre, Precio, Cantidad en stock

producto_1 = {
    'nombre': 'Detergente',
    'precio': 15,
    'cantidad en stock': 5
}
producto_2 = {
    'nombre': 'Lavandina',
    'precio': 17,
    'cantidad en stock': 8
}
producto_3 = {
    'nombre': 'Papel higienico',
    'precio': 9,
    'cantidad en stock': 12
}

lista_tienda = [producto_1, producto_2, producto_3]
print(lista_tienda)
# Imprime el nombre y el precio del segundo producto en la lista.

segundo_producto = lista_tienda[1]
print(segundo_producto)
nombre_segundo_producto = segundo_producto['nombre']
precio_segundo_producto = segundo_producto['precio']
print(f'El nombre del segundo producto es {
      nombre_segundo_producto} y el precio es {precio_segundo_producto}')
