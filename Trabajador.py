from Persona import Persona

class Trabajador(Persona):
    def __init__(self, nombre: str, correo: str, edad: int, sueldo: int, departamento: str) -> None:
        super().__init__(nombre, correo, edad)
        self.__sueldo = sueldo
        self.__edad = edad
        self.__departamento = departamento
        print("---------------")    
        print("Trabajador creado")
        print("---------------")

    def get_departamento(self):
        return self.__departamento

    def get_sueldo(self):
        return self.__sueldo

    def __str__(self):
        return f"Trabajador: {self.get_nombre()}"
