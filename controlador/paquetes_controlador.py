from modelo.bd import conectar

def agregar_paquete(nombre, descripcion, destinos, fecha_inicio, fecha_fin, precio_total):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
    INSERT INTO Paquetes (nombre, descripcion, fecha_inicio, fecha_fin, precio_total) 
    VALUES (%s, %s, %s, %s, %s)
    ''', (nombre, descripcion, fecha_inicio, fecha_fin, precio_total))
    conexion.commit()
    paquete_id = cursor.lastrowid
    values_to_insert = [(paquete_id, destino_id) for destino_id in destinos]
    query = "INSERT INTO PaquetesDestino (paquete_id, destino_id) VALUES (%s, %s)"

    cursor.executemany(query, values_to_insert)
    print("Paquete creado exitosamente!")
    conexion.commit()
    conexion.close()


def mostrar_paquetes():
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('SELECT * FROM Paquetes')
    paquetes = cursor.fetchall()
    
    conexion.close()
    return paquetes


def verificar_disponibilidad(fecha_inicio, fecha_fin):
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('''
    SELECT * FROM Paquetes WHERE fecha_inicio <= %s AND fecha_fin >= %s
    ''', (fecha_fin, fecha_inicio))
    
    paquetes_disponibles = cursor.fetchall()
    
    conexion.close()
    return paquetes_disponibles


def eliminar_paquete(id):
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('''
    DELETE FROM Paquetes WHERE id = %s
    ''', (id,))
    
    conexion.commit()
    conexion.close()


def modificar_paquete(id, nombre, descripcion, destinos, fecha_inicio, fecha_fin, precio_total):
    conexion = conectar()
    cursor = conexion.cursor()
    
    destinos_str = ",".join(map(str, destinos))
    
    cursor.execute('''
    UPDATE Paquetes SET nombre = %s, descripcion = %s, destinos = %s, fecha_inicio = %s, fecha_fin = %s, precio_total = %s
    WHERE id = %s
    ''', (nombre, descripcion, destinos_str, fecha_inicio, fecha_fin, precio_total, id))
    
    conexion.commit()
    conexion.close()