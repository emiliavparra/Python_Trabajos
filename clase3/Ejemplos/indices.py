# Definimos una lista
mi_lista = ['a', 'b', 'c', 'd', 'e']

# Acceso usando indices positivos
primer_elemento = mi_lista[0]
print(f'El primer elemento es: {primer_elemento}')

segundo_elemento = mi_lista[1]
print(f'El segundo elemento es: {segundo_elemento}')

# Acceso usando indices negativos
ultimo_elemento = mi_lista[-1]
print(f'El ultimo elemento es: {ultimo_elemento}')
penultimo_elemento = mi_lista[-2]
print(f'El penultimo elemento es: {penultimo_elemento}')

# Acceso a la sublista (slicing)
print('Sublista (Indice 1 a 3): ', mi_lista[1:4])
print('Sublista (inicio a 3)', mi_lista[:3])
print('Sublista (indice 2 al final)', mi_lista[2:])

# Acceso con paso de slicing
print('Sublista con paso 2: ', mi_lista[::2])
print('Sublista con paso 2 en rango (1 a 4):', mi_lista[1:4:2])

# Iteracion a traves de una lista
print('Iteracion a traves de la lista:')
for elemento in mi_lista:
    print(elemento)

# INDICE Y LONGITUD NO ES LO MISMO
# INDICE VA DESDE 0 Y LONGITUD ES TODO
