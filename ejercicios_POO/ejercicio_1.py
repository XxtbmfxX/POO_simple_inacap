class Estudiante():
    def __init__(self, nombre, grado, edad) -> None:
        self.nombre = nombre
        self.grado = grado
        self.edad = edad

    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")

        
class Trabajador():
    def __init__(self, especialidad) -> None:
        self.especialidad = especialidad


class EstudianteTrabajador(Estudiante, Trabajador):
    def __init__(self, nombre, grado, edad, especialidad) -> None:
        Estudiante.__init__(self, nombre, grado, edad)
        Trabajador.__init__(self, especialidad)
    

mi_persona = EstudianteTrabajador("pepe", 4, 34, "computer science")

print(mi_persona)

mi_persona.estudiar()