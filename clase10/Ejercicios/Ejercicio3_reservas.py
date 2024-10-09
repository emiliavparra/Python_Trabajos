# Creo la clase habitacion

class Habitacion:
    disponible = True  # Seteo que este siempre disponible (True) por default

    # Establezco los 3 parametros indicados en el ejercicio
    def __init__(self, numero, tipo, precio):
        self.numero = numero  # Guardo el parametro numero
        self.tipo = tipo  # Guardo el parametro tipo
        self.precio = precio  # Guardo el parametro precio


class Hotel:  # Creo la clase hotel
    # Defino el parametro habitaciones para ir agregando habitaciones
    def __init__(self, habitaciones):
        self.habitaciones = habitaciones  # Guardo el parametro habitaciones

    def reservar(self, numero):  # Metodo reservar
        for habitacion in self.habitaciones:  # bucle for para iterar sobre las habitaciones de la lista
            # Si el nro de habitacion ingresado es igual al numero del parametro pasa al blucle siguiente:
            if habitacion.numero == numero:
                if habitacion.disponible == True:  # Uso la propiedad de la clase habitacion
                    habitacion.disponible = False
                    print(f'La habitacion {
                          habitacion.numero} ha sido reservada exitosamente')
                else:
                    print(f'La habitacion {
                          habitacion.numero} no se encuentra disponible')
                # Si el nro de habitacion ingresado NO coincide con el del parametro habitacion self, sale del bucle (no ingresa a la propiedad)
                break

    def cancelar(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                if habitacion.disponible == False:
                    habitacion.disponible = True
                    print(f'La habitacion {
                          habitacion.numero} ha sido cancelada exitosamente')
                else:
                    print(f'La habitacion {
                          habitacion.numero} no puede ser cancelada porque esta disponible')
                break

    def habitacionesDisponibles(self):
        for habitacion in self.habitaciones:
            if habitacion.disponible == True:
                print(f'La habitacion {
                      habitacion.numero} se encuentra disponible')


habitaciones = [
    Habitacion(105, 'Suite', 1500),
    Habitacion(107, 'Twin', 900),
    Habitacion(109, 'Single', 600)
]

hotel1 = Hotel(habitaciones)

hotel1.reservar(107)
hotel1.reservar(109)
hotel1.habitacionesDisponibles()

hotel1.cancelar(107)
hotel1.habitacionesDisponibles()
hotel1.reservar(109)
