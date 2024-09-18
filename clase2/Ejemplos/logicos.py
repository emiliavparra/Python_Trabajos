# devuelven siempre un valor booleano
# AND, OR Y NOT

# Definimos distintas variables para usar en las comparaciones

a = 10
b = 5
c = 15
d = 8

# Operador AND
# Ambas deben ser verdad para que sea true
resultado_and = (a > b) and (c > d)
print(f'Resultado de (a > b) and (c > d): {resultado_and}')

# Operador OR
# Si al menos UNA de las condiciones se cumple, es true
resultado_or = (a < b) or (c > d)
print(f'Resultado de (a < b) or (c > d): {resultado_or}')

# Operador NOT
# Invierte el valor de la expresion
resultado_not = not (a < b)
print(f'Resultado de not (a < b): {resultado_not}')
# si dihgo que a es menor que b es false porque 10 no es menor que 5
# pero como pongo NOT, es true (el invertido)

# Combinacion de operadores
resultado_combinado = (a > b) and (not (c > d)) or (b < c)
print(f'Resultado combinado: {resultado_combinado}')
# a > b es True porque 10 es mayor que 5
# c < d es False porque 15 no es menor que 8 y not lo vuelve True
# a > b and c < d es True porque true and true es True
# True or True resulta en True
