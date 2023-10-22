import DB

my_db = "sqlite_db.db"

conn = DB.conectar_bd(my_db)

datos_clientes = [
    ('Ana', 'ana@example.com', 30, 2, '555-5555'),
    ('Carlos', 'carlos@example.com', 25, 1, '555-5556'),
    # Agrega más tuplas según sea necesario
]

DB.agregar_varios_clientes(conn, datos_clientes)

datos_trabajadores = [
    ('Juan', 'juan@example.com', 28, 3000, 'Desarrollo'),
    ('Laura', 'laura@example.com', 35, 3500, 'Ventas'),
    # Agrega más tuplas según sea necesario
]

DB.agregar_varios_trabajadores(conn, datos_trabajadores)