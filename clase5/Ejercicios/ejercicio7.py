# Contar Ocurrencias de Elementos en un Diccionario Anidado

# Crea un diccionario que contenga información sobre tres clubes deportivos, cada uno con una lista de jugadores:
# Cada jugador es un diccionario con las claves: nombre y edad
# Cuenta cuántos jugadores en total tienen cada uno de los clubes

# Creo el diccionario principal:
clubes_deportivos = {
    'nombre_del_club_1': 'Club Atletico Boca Juniors',
    'cancha_1': 'La bombonera',
    'lista_de_jugadores_1': [
        {
            'nombre': 'Edinson Cavani',
            'edad': 37},
        {'nombre': 'Marcos Rojo',
         'edad': 34
         },
        {
            'nombre': 'Pol Fernandez',
            'edad': 36
        }
    ],
    'nombre_del club_2': 'River Plate',
    'cancha_2': 'El monumental',
    'lista_de_jugadores_2': [
        {
            'nombre': 'Miguel Borja',
            'edad': 32},
        {'nombre': 'Franco Armani',
         'edad': 37
         },
    ],
    'nombre_del_club_3': 'San Lorenzo',
    'cancha_3': 'El gasometro',
    'lista_de_jugadores_3': [
        {
            'nombre': 'Perrito Barrios',
            'edad': 30},
    ]
}

print(clubes_deportivos)

club_1 = clubes_deportivos.get('lista_de_jugadores_1')
cuantos_son_1 = len(club_1)
print(f'El primer club tiene {cuantos_son_1} jugadores  en su lista')

club_2 = clubes_deportivos.get('lista_de_jugadores_2')
cuantos_son_2 = len(club_2)
print(f'El segundo club tiene {cuantos_son_2} jugadores  en su lista')

club_3 = clubes_deportivos.get('lista_de_jugadores_3')
cuantos_son_3 = len(club_3)
print(f'El tercer club tiene {cuantos_son_3} jugadores  en su lista')
