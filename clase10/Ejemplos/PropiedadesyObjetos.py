# Propiedades de un objeto

# Definir la clase persona
class Persona:
    def __init__(self, nombre, edad):
        # Inicializamos las propiedades del objeto
        self.nombre = nombre  # Propiedad nombre
        self.edad = edad  # Propiedad edad


# Creamos un objeto de la clase Persona
persona1 = Persona('Ana', 30)
persona2 = Persona('Luis', 35)

# Acceder a las propiedades del objeto
print(persona2.nombre)
print(persona2.edad)

# La clase Persona define un objeto que tiene propiedades
# como nombre y edad.
# Al instanciar persona1 con valores especificos, se crean
# atributos unicos que representan el estado de ese objeto
# Se puede acceder a estas propiedades itilizando la notacion de piunto,
# lo que permite obtener info sobre la instancia creada
