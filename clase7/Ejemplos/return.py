# EJEMPLO 1 Basico de return
def calcular_cuadrado(numero):
    return numero * numero  # retorna el cuadrado del numero


# Llamada a la funcion y almacenamiento del resultado
resultado = calcular_cuadrado(4)

# Imprimimos el resultado:
print('Ejemplo 1 basico de return:')
print(f'El cuadrado de 4 es {resultado}')
print()  # esto para separar el uso de la funcion

# EJEMPLO 2 retorno de multiples valores


def obtener_datos():
    nombre = 'Ana'
    edad = 30
    return nombre, edad  # Retorna dos valores como una tupla


# Asignamos los valores retornados a variables
nombre, edad = obtener_datos()

# Imprimimos los valores
print('Ejemplo 2 retorno de multiples valores:')
print(f'Nombre: {nombre}, Edad: {edad}')
print()

# Ejemplo 3 sin return


def mostrar_mensaje():
    print('Esta funcion no retorna ningun valor')


resultado = mostrar_mensaje()
# Imprimimos el valor retornado
print('Ejemplo 3 sin return')
print(f'Valor retornado: {resultado}')  # output: None
print()

# Ejemplo 4 return con condiciones


def clasificar_numero(numero):
    if numero > 0:
        return 'Positivo'
    elif numero < 0:
        return 'Negativo'
    else:
        return 'Cero'


# Llamamos a la funcion con diferentes argumentos
resultado1 = clasificar_numero(10)
resultado2 = clasificar_numero(-5)
resultado3 = clasificar_numero(0)

# Imprimimos los resultados
print('Ejemplo 4 return con condiciones')
print(f'El numero 10 es {resultado1}')
print(f'El numero -5 es {resultado2}')
print(f'El numero 0 es {resultado3}')
