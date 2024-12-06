from modelo.destinos import Destino

destinos = []

def agregar_destino(nombre, descripcion, actividades, costo):
    destino = Destino(nombre, descripcion, actividades, costo)
    destinos.append(destino)

def mostrar_destinos():
    return destinos

def modificar_destino(nombre, nuevo_nombre=None, nueva_descripcion=None, nuevas_actividades=None, nuevo_costo=None):
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