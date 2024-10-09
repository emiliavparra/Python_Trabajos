import math


class Forma:  # Creo la clase Forma
    def area(self):
        pass


class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.radio * 2 * math.pi


class TrianguloRectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


mis_formas = [Rectangulo(20, 10),
              Circulo(8),
              TrianguloRectangulo(10, 15)]

for forma in mis_formas:
    print(f'El area de {type(forma).__name__} es : {forma.area():.2f}')
