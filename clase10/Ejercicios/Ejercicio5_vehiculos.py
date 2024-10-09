class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def Mostrar_info(self):
        print(f'La marca del vehiculo es {self.marca}')
        print(f'El modelo del vehiculo es {self.modelo}')


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo)
        self.año = año

    def Mostrar_info(self):
        super().Mostrar_info()
        print(f'El año del vehiculo es {self.año}')


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def Mostrar_info(self):
        super().Mostrar_info()
        print(f'El color del vehiculo es {self.color}')


mi_coche = Coche('Ford', 'Fiesta', 1990)
mi_coche.Mostrar_info()
