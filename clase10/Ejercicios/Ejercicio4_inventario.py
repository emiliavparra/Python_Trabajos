class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def aumentarCantidad(self, cantidad):
        self.cantidad += cantidad
        print(f'El producto {self.nombre} ha añadido {
              cantidad} al stock. El total actual es de {self.cantidad}')

    def disminuirCantidad(self, cantidad):
        self.cantidad -= cantidad
        print(f'El producto {self.nombre} ha restado {
              cantidad} al stock. El total actual es de {self.cantidad}')


class Inventario:
    def __init__(self, productos):
        self.productos = productos

    def agregarProducto(self, producto):
        self.productos.append(producto)
        print(f'El {producto.nombre} ha sido agregado exitosamente')

    def mostrarProductos(self):
        print('La lista actual del inventario es:')
        for producto in self.productos:
            print(f' Producto: {producto.nombre}, Precio: {
                  producto.precio}, Cantidad: {producto.cantidad}')


lista_de_productos = [
    Producto('yerba', 100, 3),
    Producto('azucar', 120, 4),
    Producto('sal', 15, 7)
]

mi_stock = Inventario(lista_de_productos)
mi_stock.mostrarProductos()

nuevoProducto = Producto('Galletitas', 20, 4)
nuevoProducto.aumentarCantidad(3)
nuevoProducto.disminuirCantidad(1)
mi_stock.agregarProducto(nuevoProducto)
mi_stock.mostrarProductos()
