from Trabajador import Trabajador
from Cliente import Cliente
import time


#===== FUNCIONES PARA AGREGAR DATOS ======

def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre: ")
        if nombre.isalpha():
            return nombre
        else:
            print("Nombre no válido. Por favor, ingrese solo letras.")

def validar_correo():
    while True:
        correo = input("Ingrese el correo: ")
        if "@" in correo and "." in correo:
            return correo
        else:
            print("Correo no válido. Por favor, ingrese un correo válido.")

def validar_edad():
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad >= 18:
                return edad
            else:
                print("La edad debe ser mayor o igual a 18.")
        except ValueError:
            print("Edad no válida. Por favor, ingrese un número entero.")

def validar_antiguedad():
    while True:
        try:
            antiguedad = int(input("Ingrese la antigüedad (mayor o igual a 0): "))
            if antiguedad >= 0:
                return antiguedad
            else:
                print("La antigüedad no puede ser menor que 0.")
        except ValueError:
            print("Antigüedad no válida. Por favor, ingrese un número entero.")

def validar_telefono():
    while True:
        telefono = input("Ingrese el teléfono (entre 1 y 9 caracteres): ")
        if 1 <= len(telefono) <= 9:
            return telefono
        else:
            print("Número de teléfono no válido. Por favor, ingrese entre 1 y 9 caracteres.")

def validar_sueldo():
    while True:
        try:
            sueldo = int(input("Ingrese el sueldo (mayor o igual a 500000): "))
            if sueldo >= 500000:
                return sueldo
            else:
                print("El sueldo debe ser mayor o igual a 500000.")
        except ValueError:
            print("Sueldo no válido. Por favor, ingrese un número entero.")

def validar_departamento():
    while True:
        departamento = input("Ingrese el departamento (TI o Ventas): ")
        if departamento in ['TI', 'Ventas']:
            return departamento
        else:
            print("Departamento no válido. Por favor, ingrese TI o Ventas.")

def agregar_cliente():
    nombre = validar_nombre()
    correo = validar_correo()
    edad = validar_edad()
    antiguedad = validar_antiguedad()
    telefono = validar_telefono()

    return Cliente(nombre, correo, edad, antiguedad, telefono)

def agregar_cliente_db():
    nombre = validar_nombre()
    correo = validar_correo()
    edad = validar_edad()
    antiguedad = validar_antiguedad()
    telefono = validar_telefono()

    return (nombre, correo, edad, antiguedad, telefono)

def agregar_trabajador():
    nombre = validar_nombre()
    correo = validar_correo()
    edad = validar_edad()
    departamento = validar_departamento()
    sueldo = validar_sueldo()

    return Trabajador(nombre, correo, edad, sueldo, departamento)

def agregar_trabajador_db():
    nombre = validar_nombre()
    correo = validar_correo()
    edad = validar_edad()
    departamento = validar_departamento()
    sueldo = validar_sueldo()

    return (nombre, correo, edad, sueldo, departamento)


#====== FUNCIONES COMPLEMENTARIAS =====

def clientes_masde_5(db: dict):
    mas_de_5 = []
    for i in db["clientes"]:
        if i.get_antiguedad() > 5:
            mas_de_5.append(i.get_todos_los_datos())
    return mas_de_5

#Se puede optimizar cambiando a estructura de mi_db
def buscar_cliente(db:dict , nombre:str):
    nombres_usuarios = []
    for i in db["clientes"]:
        print(i.get_nombre() == nombre)
        if i.get_nombre() == nombre:
            nombres_usuarios.append(i)
    
    if nombres_usuarios == []:
        return f"No se encontron el nombre {nombre}"
        
    return nombres_usuarios

def efecto_escritura(texto:str, salto: bool = False, velocidad: float = 0.1):    
    if salto:    
        for caracter in texto:
            print(caracter, end='\n', flush=True)
            time.sleep(velocidad)  
    else:
        for caracter in texto:
            print(caracter, end='', flush=True)
            time.sleep(velocidad)  
    return ""

def efecto_escritura_2(texto:str):
    for caracter in texto.split('-'):
        print(caracter, end='\n', flush=True)
        time.sleep(0.099) 
    return ""