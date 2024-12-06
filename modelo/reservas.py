class Reserva:
    def __init__(self, usuario_id, paquete_id, fecha_reserva):
        self.usuario_id = usuario_id
        self.paquete_id = paquete_id
        self.fecha_reserva = fecha_reserva

    def __repr__(self):
        return f"Reserva(Usuario ID: {self.usuario_id}, Paquete ID: {self.paquete_id}, Fecha: {self.fecha_reserva})"