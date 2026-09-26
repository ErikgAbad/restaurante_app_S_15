from datetime import datetime

class Venta:
    def __init__(self, id_venta, usuario, producto, fecha=None):
        self.id_venta = id_venta
        self.usuario = usuario
        self.producto = producto
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "usuario": self.usuario,
            "producto": self.producto,
            "fecha": self.fecha
        }

    @staticmethod
    def from_dict(data):
        return Venta(
            id_venta=data.get("id_venta"),
            usuario=data.get("usuario"),
            producto=data.get("producto"),
            fecha=data.get("fecha")
        )