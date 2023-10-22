import sqlite3


# Función para establecer la conexión a la base de datos
def conectar_bd(nombre_bd):
    conn = sqlite3.connect(nombre_bd)
    return conn

def crear_tabla_trabajadores(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trabajadores (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            correo TEXT,
            edad INTEGER,
            sueldo REAL,
            departamento TEXT
        )
    ''')
    conn.commit()

def crear_tabla_clientes(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            correo TEXT,
            edad INTEGER,
            antiguedad INTEGER,
            telefono TEXT
        )
    ''')
    conn.commit()

# Función para agregar un trabajador
def agregar_trabajador(conn, datos_trabajador):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO trabajadores (nombre, correo, edad, sueldo, departamento ) VALUES (?, ?, ?, ?, ?)', (datos_trabajador))
    conn.commit()
    conn.close()

# Función para agregar un cliente
def agregar_cliente(conn, datos_cliente):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clientes (nombre, correo, edad, antiguedad, telefono) VALUES (?, ?, ?, ?, ?)', (datos_cliente))
    conn.commit()

#traer trabajadores de informática
def trabajadores_informatica(conn):
    cursor = conn.cursor()
    resultados = cursor.execute("SELECT * FROM trabajadores WHERE departamento='Informático'")
    for row in resultados:
        print(row)
    
def buscar_trabajador_por_nombre(conn, nombre):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM trabajadores WHERE nombre = ?', (nombre,))
    resultado = cursor.fetchall()
    return resultado
    
def buscar_cliente_antiguedad_5_mas(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes WHERE antiguedad > 5')
    resultado = cursor.fetchall()
    return resultado

def obtener_datos_trabajadores(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM trabajadores')
    resultados = cursor.fetchall()
    return resultados

def obtener_datos_clientes(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    resultados = cursor.fetchall()
    return resultados

def agregar_varios_clientes(conn, datos_clientes):
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO clientes (nombre, correo, edad, antiguedad, telefono)
        VALUES (?, ?, ?, ?, ?)
    ''', datos_clientes)
    conn.commit()

def agregar_varios_trabajadores(conn, datos_trabajadores):
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO trabajadores (nombre, correo, edad, sueldo, departamento)
        VALUES (?, ?, ?, ?, ?)
    ''', datos_trabajadores)
    conn.commit()
