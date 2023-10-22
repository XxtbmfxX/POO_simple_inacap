from Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre: str, correo: str, edad: int, antiguedad: int, telefono: str) -> None:
        super().__init__(nombre, correo, edad)
        self.__antiguedad = antiguedad
        self.__telefono = telefono
        print("---------------")
        print("cliente creado")
        print("---------------")

    def get_antiguedad(self):
        return self.__antiguedad
    
    def get_todos_los_datos(self):
        return {
            "nombre": self.get_nombre(),
            "correo": self.get_correo(),
            "edad": self.get_edad(),
            "telefono": self.__telefono
        }

    def __str__(self):
        return f"Cliente: {self.get_nombre()}"
    
