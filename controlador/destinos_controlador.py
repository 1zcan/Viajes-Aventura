from modelo.destinos import Destino
from modelo.bd import conectar

destinos = []


def agregar_destino(nombre, descripcion, actividades, costo):
    conexion = conectar()
    cursor = conexion.cursor()
    destino = Destino(nombre, descripcion, actividades, costo)
    destinos.append(destino)

    cursor.execute(
        """
    INSERT INTO Destinos (nombre, descripcion, actividades, costo) VALUES (%s,%s,%s,%s)
    """,
        (nombre, descripcion, actividades, costo),
    )
    print("destino agregado ")   
    conexion.commit()
    conexion.close()


def mostrar_destinos():
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM destinos"
    cursor.execute(query)
    destino = cursor.fetchall()
    print("Destinos: ")
    print(destino)
    conexion.close()


def modificar_destino(nombre, nuevo_nombre, nueva_descripcion, nuevas_actividades, nuevo_costo):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        """
    UPDATE Destinos SET nombre = %s, descripcion = %s, actividades = %s, costo = %s WHERE nombre = %s
    """,
        (nuevo_nombre, nueva_descripcion, nuevas_actividades, nuevo_costo, nombre),
    )
    print("Destino modificado correctamente")
    conexion.commit()
    conexion.close()


def eliminar_destino(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "DELETE FROM Destinos WHERE nombre = %s",
        (nombre,),
    )
    print("")
    print("Destino eliminado")
    conexion.commit()
    conexion.close()
