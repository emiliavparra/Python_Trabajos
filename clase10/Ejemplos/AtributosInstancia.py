# Atributos de instancias

# Definimos la clase
class Gato:
    def __init__(self, color, nombre):
        self.color = color  # Atributo de instancia
        self.nombre = nombre  # Atributo de instancia


# Crear diferentes objetos (instancias) de la clase Gato
gato1 = Gato('negro', 'Felix')
gato2 = Gato('gris', 'nene')

# Acceder a los atributos de instancia
print(f'El color y nombre del gato 1 es : {gato1.color}')
print(gato1.nombre)
print(gato2.color)
print(gato2.nombre)

# La clase Gato incluye atributos de instancia, color y nombre que se inicializan en el constructor
# Cada objeto creado a partir de esta clase (como gato1 y gato2) tiene sus propios valores para estos atributos
# Lo que permite que diferentes instancias representen gatos disntios con caracteristicas unicas
