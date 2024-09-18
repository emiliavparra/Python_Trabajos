# Ejercicio 2: Categoría de Edad con Operadores Lógicos

# Hago esta linea para que el usuario ingrese su edad
# Lo transformo de string a numero con int
categoria_edad = int(input('Ingresa tu edad:'))

if categoria_edad >= 0 and categoria_edad <= 12:
    print(f'Tu edad es {categoria_edad}. Tu categoria es NIÑO')

if categoria_edad >= 13 and categoria_edad <= 19:
    print(f'Tu edad es {categoria_edad}. Tu categoria es ADOLESCENTE')

if categoria_edad >= 20 and categoria_edad <= 64:
    print(f'Tu edad es {categoria_edad}. Tu categoria es ADULTO')

if categoria_edad >= 65:
    print(f'Tu edad es {categoria_edad}. Tu categoria es ADULTO MAYOR')
