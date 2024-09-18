# Definir listas

# Lista vacia
lista_vacia = []
print(f'Lista vacia: {lista_vacia}')

# Lista de elementos iniciales
lista_elementos = [1, 2, 3, 4, 5]
print(f'Lista con elementos iniciales: {lista_elementos}')

# Lista de cadenas
lista_cadenas = ['manzana', 'banana', 'cereza']
print(f'Lista de cadenas: {lista_cadenas}')

# Lista Mixta
lista_mixta = [42, 'texto', 3.14, [1, 2, 3]]
print(f'Lista mixta: {lista_mixta}')

# Lista con elementos repetidos
listas_repetidos = [0] * 5
print(f'Listas con elementos repetidos: {listas_repetidos} ')

# Listas a partir de otros iterables
cadena = 'Hola'
lista_de_caracteres = list(cadena)
print('Lista a partir de otro iterable (cadena): ', lista_de_caracteres)
