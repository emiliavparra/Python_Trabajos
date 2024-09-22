# Metodos de instancias

# Definimos la clase
class Perro:
    def __init__(self, raza, nombre):
        self.raza = raza  # Atributo de instancia
        self.nombre = nombre  # Atributo de instancia

        # Metodo para mostrar info del perrito
    def mostrar_info(self):
        return f'Perro: {self.raza} {self.nombre}'


# Creamos un objeto de la clase perro
mi_perro = Perro('Mestiza', 'Canelita')

# Usar el metodo del objeto
print(mi_perro.mostrar_info())

# En la clase Perro, el metodo mostrar_info es un metodo de instancia que proporciona
# una reprfesentacion de la info del perro al acceder a sus atributos
# Este metodo permite realizar acciones especificas sobre los datos del objeto y se invoca
# a traves de la instancia de perro para obtener detalles sobre ese objeto en particular
