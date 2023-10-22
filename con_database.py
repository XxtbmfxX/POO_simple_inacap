import DB

from utils import efecto_escritura, efecto_escritura_2
import utils

my_db = "sqlite_db.db"

conn = DB.conectar_bd(my_db)

DB.crear_tabla_trabajadores(conn)

DB.crear_tabla_clientes(conn)



def main():

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
                DB.agregar_cliente(conn, utils.agregar_cliente_db())
            case 2:
                DB.agregar_trabajador(conn, utils.agregar_trabajador_db())
            case 3:
                nombre = input("Ingrese el nombre porfis: ")
                resultados = DB.buscar_trabajador_por_nombre(conn, nombre)
                if resultados:
                    for resultado in resultados:
                        print(resultado)
                else:
                    print('No se encontraron trabajadores con ese nombre.')
            case 4:
                resultado = DB.buscar_cliente_antiguedad_5_mas(conn)
                print(resultado)
            case 5:                        
                # Obtener datos de trabajadores
                datos_trabajadores = DB.obtener_datos_trabajadores(conn)

                # Obtener datos de clientes
                datos_clientes = DB.obtener_datos_clientes(conn)

                # Imprimir los datos
                print("Datos de Trabajadores:")
                efecto_escritura(datos_trabajadores, True)
            
                print("\nDatos de Clientes:")
                efecto_escritura(datos_clientes, True)

            case 6:
                conn.close()
                quit()
            case _:
                print("Seleccione una opción válida porfis")
        

    print(f"{'='*100}")


if __name__ == "__main__":
    main()