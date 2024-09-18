# Ejercicio 4: Manipulación de Tuplas y Comprobación de Índices

# Crea una tupla llamada frutas con los siguientes elementos: ("manzana", "banana", "cereza").
tupla_frutas = ('manzana', 'banana', 'cereza')
# Usa el método index para encontrar la posición de la fruta "banana"
fruta_buscada = tupla_frutas.index('banana')
print('La fruta banana se encuentra en la posicion: ', fruta_buscada)

# Verifica si la fruta "naranja" está en la tupla. Si no está, muestra un mensaje indicando que no está presente.

fruta_pedida = 'naranja'

if fruta_pedida in tupla_frutas:
    print(f'La fruta {fruta_pedida} se encuentra en la tupla')
else:
    print(f'La fruta {fruta_pedida} no se encuentra en la tupla')
