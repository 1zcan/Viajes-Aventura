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

    conexion.commit()
    conexion.close()


def mostrar_destinos():
    conexion = conectar()
    cursor = conexion.cursor()
    query = ("SELECT * FROM destinos")
    cursor.execute(query)
    destino = cursor.fetchall()
    print("Destinos: ")
    print(destino)
    conexion.close()


def modificar_destino(
    nombre,
    nuevo_nombre=None,
    nueva_descripcion=None,
    nuevas_actividades=None,
    nuevo_costo=None,
):
    for destino in destinos:
        if destino.nombre == nombre:
            if nuevo_nombre:
                destino.nombre = nuevo_nombre
            if nueva_descripcion:
                destino.descripcion = nueva_descripcion
            if nuevas_actividades:
                destino.actividades = nuevas_actividades
            if nuevo_costo:
                destino.costo = nuevo_costo
            return destino
    return None


def eliminar_destino(nombre):
    global destinos
    destinos = [destino for destino in destinos if destino.nombre != nombre]
