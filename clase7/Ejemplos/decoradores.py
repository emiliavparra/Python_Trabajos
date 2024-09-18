# Decorador basico
def mi_decorador(func):  # Definimos un decorador llamado mi_decorador
    # Definicion de la funcion interna 'wrapper' q acepta cualquier nro de arg
    def wrapper(*args, **kwargs):
        # Codigo que se ejecuta antes de la funcion original('saludar')
        print('Antes de ejecutar la funcion: ')
        # Llamado a la funcion original('saludar') y se almacena el resultado
        resultado = func(*args, **kwargs)
        # Codigo que se ejecuta despues de la funcion original
        print('Despues de ejecutar la funcion')
        return resultado  # Se retorna el resultado de la funcion original
    return wrapper  # Se retorna la funcion wrapper reemplazando la funcion original

# Usamos el decorador en una funcion


@mi_decorador
def saludar(nombre):
    print(f'Hola {nombre}!')


# Llamamos a la funcion decorada
print('Decorador de una funcion:')
saludar('Ana')

# Decorar con parametros


def repetir_veces(veces):  # Def de un decorador generador que acepta un parametro 'veces'
    def decorador(func):  # Def de un decorador dentro del decorador generador
        def wrapper(*args, **kwargs):  # Definicion de la func interna 'wrapper' q acepta argumentos
            for _ in range(veces):  # Ejecuta la funcion original 'veces' veces
                func(*args, **kwargs)  # Llamado a la funcion original
        return wrapper  # Retorna la funcion wrapper que reemplaza a la funcion original
    return decorador  # Retorna el decorador para ser usado con el nro de veces especificado


# Aplica el decorador repetir_veces con el argumento 3 a la funcion 'decir hola'
@repetir_veces(3)
def decir_hola():  # Definicion de la funcion 'decir_hola'
    print('Hola!')  # Codigo de la funcion 'decir_hola'


decir_hola()  # Llama a la funcion 'decir hola'
