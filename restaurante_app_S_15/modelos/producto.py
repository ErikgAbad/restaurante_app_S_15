class Producto:
    def __init__(self, id_producto, nombre, autor=""):
        self.id_producto = id_producto
        self.nombre = nombre
        self.autor = autor

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "autor": self.autor
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            id_producto=data.get("id_producto"),
            nombre=data.get("nombre"),
            autor=data.get("autor", "")
        )