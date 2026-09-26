class Usuario:
    def __init__(self, id_usuario, nombre, rol="Docente"):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.rol = rol

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(data):
        return Usuario(
            id_usuario=data.get("id_usuario"),
            nombre=data.get("nombre"),
            rol=data.get("rol", "Docente")
        )