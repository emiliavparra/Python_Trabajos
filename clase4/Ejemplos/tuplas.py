# Crear una tupla con varios valores
tupla_mixta = (1, 'Hola', 3.5)

# Mostrar completa la tupla
print('Tupla completa: ', tupla_mixta)

# Acceder a los elementos de la tupla x su indice (posicion)
print('Primer elemento de la tupla: ', tupla_mixta[0])
print('Segundo elemento de la tupla: ', tupla_mixta[1])
print('Tercer elemento de la tupla: ', tupla_mixta[2])

# Explicacion tuplas inmutables
print('\nlas tuplas no se pueden modificar. Intentemos cambiarla')
# Ejemplo de intento de cambiarla que causa error
# tupla_mixta[0] = 10

# Explicacion clara de la inmutabilidad
print('Si intentamos hacer tupla_mixta[0] = 10, da error')

# Mostramos como si podemos 'modificar' una tupla, creando una nueva
tupla_mixta = (10, 'Hola', 3.5)
print('Nueva tupla con el primer elemento cambiado: ', tupla_mixta)
print('Tupla original sin cambios: ', tupla_mixta)
