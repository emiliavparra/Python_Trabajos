# 3. Ejercicio con range, enumerate, y break/continue

# Escribe un programa que:
# 1. Itere sobre una lista de cadenas usando enumerate para mostrar el índice y el valor.
# 2. Utilice continue para saltar cadenas vacías.
# 3. Utilice break para detener la iteración si se encuentra una cadena con más de 5 caracteres

# Primero creo la lista de cadenas que vamos a usar
lista_cadenas = ['azul', 'rosa', 'lila', 'violeta', '', 'gris']

# Escribo el bloque con enumerate para mostrar el indice y el valor
# En el mismo hago el ciclo if para usar el continue y el break que solo se pueden usar en un loop

for indice, cadena in enumerate(lista_cadenas):
    if cadena == '':
        continue
    elif len(cadena) > 5:
        break

    print(f'El indice es {indice} y el valor {cadena}')
    # aca me imprime hasta el lila porque violeta ya es mas largo de 5 caracteres y entra el break
