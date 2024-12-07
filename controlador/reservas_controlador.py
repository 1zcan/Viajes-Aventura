from modelo.bd import conectar

def agregar_reserva(usuario_id, paquete_id, fecha_reserva):
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('''
    INSERT INTO Reservas (usuario_id, paquete_id, fecha_reserva) 
    VALUES (%d, %d, %s)
    ''', (usuario_id, paquete_id, fecha_reserva))
    
    conexion.commit()
    conexion.close()


def mostrar_reservas(usuario_id):
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('''
    SELECT * FROM Reservas WHERE usuario_id = %d
    ''', (usuario_id,))
    
    reservas = cursor.fetchall()
    
    conexion.close()
    return reservas


def eliminar_reserva(reserva_id):
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('''
    DELETE FROM Reservas WHERE id = %d
    ''', (reserva_id,))
    
    conexion.commit()
    conexion.close()