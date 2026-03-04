import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("golosinas.db")
cursor = conexion.cursor()

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    ciudad TEXT,
    telefono TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL,
    stock INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    fecha TEXT,
    total REAL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
)
""")

conexion.commit()

# ---------------- FUNCIONES CLIENTES ----------------

def crear_cliente():
    nombre = input("Nombre: ")
    ciudad = input("Ciudad: ")
    telefono = input("Teléfono: ")
    cursor.execute("INSERT INTO clientes (nombre, ciudad, telefono) VALUES (?, ?, ?)",
                   (nombre, ciudad, telefono))
    conexion.commit()
    print("Cliente creado correctamente.\n")

def ver_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)
    print()

def actualizar_cliente():
    id_cliente = input("ID del cliente a actualizar: ")
    nuevo_nombre = input("Nuevo nombre: ")
    cursor.execute("UPDATE clientes SET nombre=? WHERE id_cliente=?",
                   (nuevo_nombre, id_cliente))
    conexion.commit()
    print("Cliente actualizado.\n")

def eliminar_cliente():
    id_cliente = input("ID del cliente a eliminar: ")
    cursor.execute("DELETE FROM clientes WHERE id_cliente=?",
                   (id_cliente,))
    conexion.commit()
    print("Cliente eliminado.\n")

# ---------------- MENÚ PRINCIPAL ----------------

def menu():
    while True:
        print("=== GESTIÓN DULCICAT ===")
        print("1. Crear cliente")
        print("2. Ver clientes")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")

        opcion = input("Selecciona opción: ")

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            ver_clientes()
        elif opcion == "3":
            actualizar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            break
        else:
            print("Opción incorrecta\n")

menu()
conexion.close()