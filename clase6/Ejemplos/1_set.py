# Gestion de asistentes a un evento

# Objetivo: Crear un proframa que administre una lista de
# asistentes a un evento sin permitir duplicados y que realice
# operaciones entre dos listas

# Crear conjunto de invitados
invitacion_viernes = {'Ana', 'Carlos', 'Pedro', 'Luis', 'Clara'}
invitacion_sabado = {'Carlos', 'Luis', 'Sofia', 'Maria', 'Pedro'}

# Mostrar invitados viernes
print(invitacion_viernes)
# Mostrasr invitados sabados
print(invitacion_sabado)

# Mostrar la union (quien asistio al menos un dia)
todos_asistentes = invitacion_sabado | invitacion_viernes

print(f'Asistentes de ambos dias:  {todos_asistentes}')

# Mostrar la interseccion (solo viernes)
solo_viernes = invitacion_viernes & invitacion_sabado
print(f'Asistentes solo el viernes: ', solo_viernes)

# MOstrar la diferencia
invitados_viernes = invitacion_viernes - invitacion_sabado
print(f'Los que vinieron solo el viernes son: ', invitados_viernes)

# Agregar un nuevo invitado
invitacion_sabado.add('Miguel')
print(f'Con el invitado agregado la lista nueva es: ', invitacion_sabado)

# Eliminar un invitado que cancelo
invitacion_sabado.remove('Miguel')
print(f'Restando a quien cancelo: ', invitacion_sabado)

# Comprobar si asistio alguien
print(f'Ana asistio el sabado? : {'Ana' in invitacion_sabado}')
