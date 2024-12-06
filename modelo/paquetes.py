class Paquete:
    def __init__(self, nombre, descripcion, destinos, fecha_inicio, fecha_fin, precio_total):
        self.nombre = nombre
        self.descripcion = descripcion
        self.destinos = destinos  # Lista de IDs de destinos
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_total = precio_total

    def __repr__(self):
        return f"Paquete({self.nombre}, {self.descripcion}, {self.destinos}, {self.fecha_inicio}, {self.fecha_fin}, {self.precio_total})"