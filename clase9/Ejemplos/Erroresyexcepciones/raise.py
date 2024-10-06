# RAISE se usa para lanzar una excepcion de manera explicita en el codigo

# EJEMPLO: raise ExceptionType('Mensaje de error')
# ExceptionType: El tipo de excepcion a lanzar (por ejemplo ValueError)
# Mensaje de error: Mensaje opcional que proporciona info adicional sobre la excepcion

# EJEMPLO

def check_age(age):
    if age < 0:
        raise ValueError('La edad no puede ser negativa')
    print(f'Edad: {age}')


check_age(25)
check_age(-5)
