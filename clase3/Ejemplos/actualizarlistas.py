# Lista Inicial
mi_lista = [10, 20, 30, 40, 50]
print('Lista original: ', mi_lista)

# Actualizar un elemento en especifico
mi_lista[2] = 35
print('Lista actualizada con 35: ', mi_lista)

# Actualizar un elemento especifico con indice negativo
mi_lista[-1] = 60
print('Lista actualizada con 60: ', mi_lista)

# Actualizar con slicing
mi_lista[1:4] = [25, 35, 45]
print('Lista con slicing: ', mi_lista)

# Actualizar basado en condicion
for i in range(len(mi_lista)):
    if mi_lista[i] > 30:
        mi_lista[1] += 10
print('Lista despues de condicion: ', mi_lista)
