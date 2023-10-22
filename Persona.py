class Persona():
    def __init__(self, nombre: str, correo: str, edad: int) -> None:
        self.__nombre = nombre
        self.__correo = correo
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_edad(self):
        return self.__edad