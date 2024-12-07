from modelo.usuarios import Usuario
from modelo.bd import conectar
import bcrypt



def registrar_usuario(nombre, email, contraseña):
    conexion = conectar()
    cursor = conexion.cursor()
    
    contraseña_hashed = hash_contraseña(contraseña)
    usuario = Usuario(nombre, email, contraseña_hashed)
    
    cursor.execute('''
    INSERT INTO Usuarios (nombre, email, contraseña) VALUES (%s,%s,%s)
    ''', (usuario.nombre, usuario.email, usuario.contraseña))
    
    conexion.commit()
    conexion.close()


def autenticar_usuario(email, contraseña):
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('''
    SELECT * FROM Usuarios WHERE email = %s
    ''', (email,))
    
    usuario = cursor.fetchone()
    conexion.close()

    if usuario and bcrypt.checkpw(contraseña.encode('utf-8'), usuario[3].encode('utf-8')):
        return Usuario(usuario[1], usuario[2], usuario[3])
    
    else:
        return None
    

def hash_contraseña(contraseña):

    hash_contraseña = bcrypt.hashpw(contraseña.encode('utf-8'),bcrypt.gensalt())
    
    return hash_contraseña



