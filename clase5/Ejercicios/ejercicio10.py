# Ejercicio 10: Buscar y Actualizar la Información en un Diccionario Anidado

# 1. Crea un diccionario que represente una base de datos de empleados de una empresa. El diccionario debe tener:
# o nombre_empresa
# o empleados, que es una lista de diccionarios, donde cada diccionario representa un empleado con:
# ▪ id_empleado
# ▪ nombre
# ▪ departamento
# ▪ salario

# 2. Escribe una función que busque y actualice el salario de un empleado dado su id_empleado. La función debe:
# o Buscar el empleado por su id_empleado.
# o Actualizar el salario del empleado a un nuevo valor proporcionado.
# o Imprimir la información del empleado después de la actualización.

# Primero creo el diccionario

empleados_empresa = {
    'nombre_empresa': 'La jirafa',
    'lista_empleados': [
        {
            'id_empleado': 101,
            'nombre': 'Emilia Parra',
            'departamento': 'administracion',
            'salario': 100
        },
        {
            'id_empleado': 102,
            'nombre': 'Dario Gomez',
            'departamento': 'marketing',
            'salario': 170
        },
        {
            'id_empleado': 107,
            'nombre': 'Juan Lopez',
            'departamento': 'finanzas',
            'salario': 280
        },
    ]
}

# Imprimo para ver si esta ok
# print(empleados_empresa)


# Defino a cual empleado le voy a actualizar segun id (podria haber sido un input)
empleado_a_actualizar_sueldo = 107
# Defino el nuevo salario (podria haber sido un input)
nuevo_salario = 215

# Hago la funcion que primero busque un empleado por id


def cambio_salario(empleados_empresa, id_empleado, nuevo_salario):
    for empleado in empleados_empresa:
        if id_empleado == empleado_a_actualizar_sueldo:
            empleados_empresa['salario'] = nuevo_salario
            return empleado


# Uso la funcion que hice pidiendo que se aplica en ID 107 y cambie el salaio de 280 a 215
cambio_salario(empleados_empresa, 107, 235)
print(empleados_empresa)
