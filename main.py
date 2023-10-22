
#departamento informatica o ventas
#sueldo > 500000
#antiguedad >= 0

#imprimir cantidad de trabajadores en informatica
#buscar a cliente por su nombre
#clientes con mas de 5 años en la empresa


from Trabajador import Trabajador
from Cliente import Cliente
from utils import agregar_cliente, agregar_trabajador, buscar_cliente, clientes_masde_5, efecto_escritura, efecto_escritura_2



mi_db = {
    "trabajadores": [
        Trabajador("John Doe", "johndoe@example.com", 30, 500000, "IT"),
        Trabajador("Jane Smith", "janesmith@example.com", 25, 400000, "Sales"),
        Trabajador("Bob Johnson", "bobjohnson@example.com", 35, 600000, "IT")
    ],

    "clientes": [
        Cliente("John", "john@example.com", 30, 5, "555-1234"),
        Cliente("Jane", "jane@example.com", 25, 2, "555-5678"),
        Cliente("Bob", "bob@example.com", 40, 10, "555-9012")
    ]
}



continuar = "si"

while continuar == "si":

    opcion = None
    
    while True:
        try:
            print(f"""{efecto_escritura("="*100, velocidad= 0.001 )} \n {efecto_escritura_2("- ( •̀ ω •́ )✧ - 1 Para agregar un Cliente - 2 Para agregar un Trabajador - 3 Para buscar a un Cliente por su nombre - 4 Para Buscar Clientes con más de 5 años de antiguedad - 5 Para mostrar datos - 6 Para Terminar el proceso")}""")
            opcion = int(input("--------> "))
            break
        except:
            print("Seleccione una opción válida porfis")

    print(f"{'='*100}\n")


    match opcion:
        case 1:
            mi_db["clientes"].append(agregar_cliente())
        case 2:
            mi_db["trabajadores"].append(agregar_trabajador())   
        case 3:
            el_nombre = input("Ingrese el nombre a buscar porfis: ")
            mi_cliente = buscar_cliente(mi_db, el_nombre)
            print(mi_cliente)
        case 4:
            mis_clietes = clientes_masde_5(mi_db)

            for el_dict in mis_clietes:
                print(f"{'^_____'*10}^\n")
                resultado = '\n'.join([f'{k}: {v}' for k, v in el_dict.items()])
                efecto_escritura(resultado, velocidad=0.01)
            print("\n")
        case 5:
            for key, value in mi_db.items():
                print(f'{key}:')
                efecto_escritura(value, True, 0.01)
        case 6:
            quit()
        case _:
            print("Seleccione una opción válida porfis")
    

print(f"{'='*100}")