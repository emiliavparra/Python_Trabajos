# Crear conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
conjunto_c = {7, 8, 9}

# subconjunto
es_subconjunto = conjunto_a.issubset(conjunto_b)
print(f'Es conjunto_a un subconjunto de conjunto_b: {es_subconjunto}')

# Superconjunto
es_superconjunto = conjunto_b.issuperset(conjunto_a)
print(f'Es conjunto_b un superconjunto con conjunto_a?: {es_superconjunto}')

# Disconjunto
son_disconjunto = conjunto_a.isdisjoint(conjunto_c)
print(f'Son conjunto_a y conjunto_c disjuntos?: {son_disconjunto}')

# Simetria
simetria = conjunto_a.symmetric_difference(conjunto_b)
print(f'La diferencia de simetria es:  {simetria}')

# Union update
conjunto_a.update(conjunto_b)
print(f'Conjunto a despues de la union con b: {conjunto_a}')

# Interseccion update
conjunto_a.intersection_update(conjunto_b)
print(f'La interseccion entre a y b es: {conjunto_a}')

# Difference update
conjunto_b.difference_update(conjunto_c)
print(f'conjunto a despues de la diferencia con b: {conjunto_a}')

# Symmetric Difference update
conjunto_a.symmetric_difference_update(conjunto_b)
print(f'conjunto a despues de la diferencia simetrica con conjunto b: {
      conjunto_b}')
