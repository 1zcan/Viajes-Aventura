from modelo.bd import conectar

def agregar_paquete(nombre, descripcion, destinos, fecha_inicio, fecha_fin, precio_total):
    conexion = conectar()
    cursor = conexion.cursor()
    
    destinos_str = ",".join(map(str, destinos))
    
    cursor.execute('''
    INSERT INTO Paquetes (nombre, descripcion, destinos, fecha_inicio, fecha_fin, precio_total) 
    VALUES (%s, %s, %s, %s, %s, %s)
    ''', (nombre, descripcion, destinos_str, fecha_inicio, fecha_fin, precio_total))
    
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