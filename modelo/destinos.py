class Destino:
    def __init__(self, nombre, descripcion, actividades, costo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.actividades = actividades
        self.costo = costo

    def __repr__(self):
        return f"Destino({self.nombre}, {self.descripcion}, {self.actividades}, {self.costo})"