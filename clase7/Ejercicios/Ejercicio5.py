# 5. Ejercicio de for con enumerate y break/continue
# Escribe un programa que:
# 1. Itere sobre una lista de nombres de personas.
# 2. Usar enumerate para mostrar el índice y el nombre.
# 3. Saltar los nombres que empiezan con la letra 'A' usando continue.
# 4. Detener la iteración si se encuentra el nombre 'Carlos' usando break

lista_nombres = ['Ana', 'Sofia', 'Enrique', 'Carlos',
                 'Raul']  # Aca le doy la lista de nombres

# Uso enumerate para obtener indice y nombre
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('A'):  # aca le digo que si empieza con A, salte ese nombre
        continue
    if nombre == 'Carlos':  # Aca la digo que cuando aparezca Carlos, termine el codigo. Por eso no se imprime 'Raul'
        break
    print(f'Indice{indice}: {nombre}')
