import tkinter as tk
from ui.login_view import LoginView
from ui.main_view import MainView
from servicios.restaurante_servicio import RestauranteServicio

class Aplicacion:
    def __init__(self):
        self.servicio = RestauranteServicio()
        self.usuario_actual = None

    def iniciar(self):
        root = tk.Tk()
        root.withdraw() # Ocultar ventana raíz

        def login_exitoso(usuario):
            self.usuario_actual = usuario

        login_window = LoginView(root, login_exitoso)
        root.wait_window(login_window) # Esperar a que se cierre el login

        if self.usuario_actual:
            root.destroy()
            app_principal = MainView(self.servicio)
            app_principal.mainloop()
        else:
            root.destroy()

if __name__ == "__main__":
    app = Aplicacion()
    app.iniciar()