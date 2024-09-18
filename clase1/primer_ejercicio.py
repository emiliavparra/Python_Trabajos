# 1. Declaracion de Variables y Constantes
edad = 25                   # Numero
nombre = 'Ana'              # Cadena de texto (String)
esta_estudiando = True      # Booleano

# Declaracion de Constantes
PI = 3.14                   # Numero
PAIS = 'Argentina'          # Cadena de texto (String)

# 2. Leer Valores por teclado
edad = int(input('Introduce tu edad: '))    # Leer un numero entero
nombre = input('Introduce tu nombre: ')      # Leer una cadena de textos
# leer y convertir a booleano
esta_estudiando = input('Estas estudiando? (si/no): ').lower() == 'sì'

# 3. Tipos de datos
cantidad_de_libros = 10     # Numero (int)
titulo_libro = 'El Principito'  # Cadena de texto (String)
es_interesante = True  # Booleano (bool)
temas = ['Aventura', 'Fantasia', 'Filosofia']  # Lista (Array)
autor = {                                     # Diccionario (Objeto)
    'nombre': 'Antoine de Saint-Exupery',
    'nacionalidad': 'Francesa'
}

# Convertir Tipo de Datos
edad_str = str(edad)  # Convierte numero a cadena de texto
# Convierte entero a numero float
cantidad_de_libros_float = float(cantidad_de_libros)

# 4. Imprimir Resultados en la Consola
print('Nombre:', edad)
print('Edad:', edad)
print('Esta estudiando?', esta_estudiando)
print('Constante PI:', PI)
print('Constante Pais:', PAIS)
print('Cantidad de libros:', cantidad_de_libros)
print('Titulo del libro:', titulo_libro)
print('Es interesante?', es_interesante)
print('Temas del libro:', temas)
print('Autor del libro:', autor)
print('Edad (como cadena dse texto):', edad_str)
print('Cantidad de libros(como float):', cantidad_de_libros_float)
