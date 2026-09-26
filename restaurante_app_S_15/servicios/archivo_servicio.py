import os
import json

class ArchivoServicio:
    def __init__(self):
        # Obtiene la ruta de este mismo archivo
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        
        # Sube un nivel para llegar a la carpeta datos/
        self.ruta_datos = os.path.join(os.path.dirname(dir_actual), "datos")

    def cargar_json(self, nombre_archivo):
        path = os.path.join(self.ruta_datos, nombre_archivo)
        if not os.path.exists(path):
            print(f"No se encontró: {path}")
            return []
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error cargando {nombre_archivo}: {e}")
            return []

    def guardar_json(self, nombre_archivo, datos):
        path = os.path.join(self.ruta_datos, nombre_archivo)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error guardando {nombre_archivo}: {e}")