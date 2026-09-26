import os
from servicios.archivo_servicio import ArchivoServicio
from modelos.venta import Venta

class RestauranteServicio:
    def __init__(self):
        self.archivo_servicio = ArchivoServicio()
        self.productos = []
        self.usuarios = []
        self.ventas = []
        self.cargar_todos_los_datos()

    def cargar_todos_los_datos(self):
        self.productos = self.archivo_servicio.cargar_json("productos.json")
        self.usuarios = self.archivo_servicio.cargar_json("usuarios.json")
        
        # Cargar ventas y convertirlas a objetos si es necesario
        datos_ventas = self.archivo_servicio.cargar_json("ventas.json")
        self.ventas = []
        for v in datos_ventas:
            if isinstance(v, dict):
                # Convertir diccionario a objeto Venta si el modelo existe
                try:
                    obj_venta = Venta(v.get("id_venta") or v.get("id"), v.get("cliente"), v.get("producto"))
                    self.ventas.append(obj_venta)
                except Exception:
                    self.ventas.append(v)
            else:
                self.ventas.append(v)

    def obtener_productos(self):
        return self.productos

    def obtener_usuarios(self):
        return self.usuarios

    def obtener_ventas(self):
        return self.ventas

    def registrar_venta(self, cliente_mesero, producto_platillo):
        # Generar ID incremental
        nuevo_id = 1
        if self.ventas:
            ids = []
            for v in self.ventas:
                if hasattr(v, 'id_venta'):
                    ids.append(v.id_venta)
                elif hasattr(v, 'id'):
                    ids.append(v.id)
                elif isinstance(v, dict):
                    ids.append(v.get("id_venta") or v.get("id", 0))
            if ids:
                nuevo_id = max(ids) + 1

        # Crear objeto Venta compatible con ui/main_view.py
        try:
            nueva_venta = Venta(nuevo_id, cliente_mesero, producto_platillo)
        except Exception:
            # Respaldo por si el constructor de Venta difiere
            class ObjetoVenta:
                def __init__(self, id_venta, cliente, producto):
                    self.id_venta = id_venta
                    self.cliente = cliente
                    self.producto = producto
            nueva_venta = ObjetoVenta(nuevo_id, cliente_mesero, producto_platillo)

        self.ventas.append(nueva_venta)

        # Preparar lista en formato diccionario para guardar en JSON
        ventas_json = []
        for v in self.ventas:
            if hasattr(v, '__dict__'):
                ventas_json.append({
                    "id_venta": getattr(v, 'id_venta', getattr(v, 'id', 1)),
                    "cliente": getattr(v, 'cliente', ''),
                    "producto": getattr(v, 'producto', '')
                })
            elif isinstance(v, dict):
                ventas_json.append(v)

        self.archivo_servicio.guardar_json("ventas.json", ventas_json)
        return nueva_venta