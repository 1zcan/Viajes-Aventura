class Usuario:
    def __init__(self, nombre, email, contraseña):
        
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña

    def __repr__(self):
        return f"Usuario({self.nombre}, {self.email})"
