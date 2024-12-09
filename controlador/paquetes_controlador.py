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
    
    cursor.execute('''
    SELECT p.nombre, GROUP_CONCAT(d.nombre SEPARATOR ', ') as destinos
    FROM Paquetes p
    JOIN PaquetesDestino pd ON p.id = pd.paquete_id
    JOIN Destinos d ON pd.destino_id = d.id
    GROUP BY p.nombre
    ''')
    
    paquetes = cursor.fetchall()
    
    for paquete in paquetes:
        print(f"Paquete: {paquete[0]}, Destinos: {paquete[1]}")
    
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
    
    print("Paquete eliminado exitosamente!")
    conexion.commit()
    conexion.close()


def modificar_paquete(paquete_id, nuevo_nombre, nueva_descripcion, nuevos_destinos, nueva_fecha_inicio, nueva_fecha_fin, nuevo_precio_total):
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Actualizar los detalles del paquete
    cursor.execute('''
    UPDATE Paquetes
    SET nombre = %s, descripcion = %s, fecha_inicio = %s, fecha_fin = %s, precio_total = %s
    WHERE id = %s
    ''', (nuevo_nombre, nueva_descripcion, nueva_fecha_inicio, nueva_fecha_fin, nuevo_precio_total, paquete_id))
    
    # Eliminar los destinos actuales del paquete
    cursor.execute('''
    DELETE FROM PaquetesDestino WHERE paquete_id = %s
    ''', (paquete_id,))
    
    # Insertar los nuevos destinos del paquete
    values_to_insert = [(paquete_id, destino_id) for destino_id in nuevos_destinos]
    query = "INSERT INTO PaquetesDestino (paquete_id, destino_id) VALUES (%s, %s)"
    cursor.executemany(query, values_to_insert)
    
    print("Paquete modificado exitosamente!")
    conexion.commit()
    conexion.close()


def mostrar_paquetes_disponibles():
    print("Ingrese la fecha de inicio deseada (yyyy-mm-dd):")
    fecha_inicio = input()
    print("Ingrese la fecha de fin deseada (yyyy-mm-dd):")
    fecha_fin = input()
    
    paquetes_disponibles = verificar_disponibilidad(fecha_inicio, fecha_fin)
    
    if paquetes_disponibles:
        print("Paquetes disponibles:")
        for paquete in paquetes_disponibles:
            print(paquete)
    else:
        print("No hay paquetes disponibles para las fechas seleccionadas.")