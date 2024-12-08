import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost", database="ev4", user="root", password=""
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        return None


def cerrar(self) -> None:
    self.conexion.close()


def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL UNIQUE,
        contraseña VARCHAR(100) NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Destinos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        descripcion VARCHAR(250) NOT NULL,
        actividades VARCHAR(250) NOT NULL,
        costo VARCHAR(30) NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Paquetes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        descripcion VARCHAR(50) NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,           
        precio_total VARCHAR(30) NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PaquetesDestino (
        paquete_id INT,
        destino_id INT,
        PRIMARY KEY (paquete_id, destino_id),
        FOREIGN KEY (paquete_id) REFERENCES Paquetes(id),
        FOREIGN KEY (destino_id) REFERENCES Destinos(id)
    )            
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Reservas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        usuario_id INTEGER NOT NULL,
        paquete_id INTEGER NOT NULL,
        fecha_reserva DATE NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES Usuarios(id),
        FOREIGN KEY (paquete_id) REFERENCES Paquetes(id)
    )
    """)

    print("Tablas creadas exitosamente!")

    conexion.commit()
    conexion.close()


crear_tablas()
