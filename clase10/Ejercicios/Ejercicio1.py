
class Estudiante:  # Defino la clase estudiante
    # Uso el constructor para crear el objeto y le doy los atributos pedidos
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre  # Guarda el nombre del estudiante
        self.edad = edad     # Guarda la edad del estudiante
        self.notas = notas   # Guarda la nota del estudiante

    def promediar(self):     # Creo el metodo promediar para calcular el promedio
        return sum(self.notas) / len(self.notas)

    # Creo el aprobar para calcular si aprueba o no el estudiante
    def aprobar(self):
        return self.promediar() >= 4


Alumno_1 = Estudiante('Emilia', 33, [10, 9, 4, 3])  # Lo pruebo con un ejemplo

print(f'El promedio del alumno {Alumno_1.nombre} es {
      Alumno_1.promediar()}. El estudiante ha aprobado con {Alumno_1.aprobar()}')
# Lo pruebo asi hasta ver como hacer un mensaje de error
# Como aprobo me tira True


class Curso:
    def __init__(self):
        self.lista_estudiantes = []

    def sumar_estudiante(self, estudiante):
        self.lista_estudiantes.append(estudiante)

    def aprobados(self, nota_aprueba=4):
        print('Los estudiantes aprobados son: ')
        for estudiante in self.lista_estudiantes:
            if estudiante.aprobar():
                print(f'El alumno {estudiante.nombre} ha aprobado con un promedio de {
                      estudiante.promediar():}')
            else:
                print(f'El alumno {estudiante.nombre} no ha aprobado por su promedio de {
                      estudiante.promediar()}')


Alumno_1 = Estudiante('Emilia', 33, [10, 9, 4, 3])  # Lo pruebo con un ejemplo
Alumno_2 = Estudiante('Dario', 31, [3, 10, 4, 7])
Alumno_3 = Estudiante('Juana', 25, [2, 4, 5, 2])

lista_curso = Curso()
lista_curso.sumar_estudiante(Alumno_1)
lista_curso.sumar_estudiante(Alumno_2)
lista_curso.sumar_estudiante(Alumno_3)

lista_curso.aprobados()
