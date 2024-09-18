# • Para usar un módulo en tu código, necesitas importarlo.
# • Esto se hace con la palabra clave import.
# • Una vez importado, puedes acceder a las funciones y clases definidas en ese módulo.

# EJEMPLO 1: Importar el modulo completo (es lo mas comun)
# import palabra clave y luego el nombre del modulo (random en este caso)
import random
# EJEMPLO 2: Importar funciones especificas de un modulo
# ahora puedo usar shuffle(metodo) sin necesidad de referirme primero a random
from random import shuffle
# EJEMPLO 3: Importar un modulo con un alias (para hacerlo mas corto y facil de usar)
# ahora puedo llamar a las funciones de random usando 'rnd' en lugar del nombre entero
import random as rnd
