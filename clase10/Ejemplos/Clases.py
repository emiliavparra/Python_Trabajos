# Definir una clase en Python

# Definimos una clase llamada coche
class Coche:
    # Metodo __init__ es el constructor para crear un objeto
    def __init__(self, marca, modelo):
        # self es una referencia al objeto que etsamos usando
        # Inicializamos los atributos de instancia
        self.marca = marca  # Guarda la marca del coche
        self.modelo = modelo  # Guarda el modelo del coche

# La clase coche es una plantilla para crear objetos de tipo auto
# Contiene un metodo constructor __init__ que inicializa los atributos especificos de cada coche que hagamos
# como por ej: marca, modelo usando la referencia self para
# # distinguir entre las propiedades del objeto y los parametros pasados al constructor
