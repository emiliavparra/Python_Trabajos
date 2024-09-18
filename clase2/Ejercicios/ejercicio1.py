# Calificación con Operador Ternario

# Creo un input para que el usuario ingrese la edad
# lo convierto a int para que sea un numero
calificacion_alumno = int(input('Ingrese su califiacion: '))

# comparo con 60 para tener el resultado pedido
if calificacion_alumno >= 60:
    print(f'Su calificacion es {calificacion_alumno}. Estas aprobado')
if calificacion_alumno < 60:
    print(f'Su calificion es {calificacion_alumno}. Estas Reprobado')
