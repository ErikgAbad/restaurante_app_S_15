import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(tk.Toplevel):
    def __init__(self, parent, on_login_success):
        super().__init__(parent)
        self.title("Sistema de Restaurante - Iniciar Sesión")
        self.geometry("420x480")
        self.resizable(False, False)
        self.configure(bg="#1e293b")
        self.on_login_success = on_login_success
        self.mostrar_pass = False

        # Centrar la ventana
        self._centrar_ventana(420, 480)

        self._crear_interfaz()

    def _centrar_ventana(self, ancho, alto):
        self.update_idletasks()
        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def _crear_interfaz(self):
        # Contenedor Principal (Card grande)
        card = tk.Frame(self, bg="white", padx=30, pady=30)
        card.pack(fill="both", expand=True, padx=20, pady=20)

        # Encabezado
        lbl_icono = tk.Label(card, text="🍔", font=("Segoe UI", 42), bg="white")
        lbl_icono.pack()

        lbl_titulo = tk.Label(card, text="Acceso al Sistema", font=("Segoe UI", 16, "bold"), fg="#0f172a", bg="white")
        lbl_titulo.pack(pady=(0, 20))

        # Campo: Usuario
        lbl_user = tk.Label(card, text="Usuario:", font=("Segoe UI", 10, "bold"), fg="#475569", bg="white")
        lbl_user.pack(anchor="w")

        self.ent_usuario = ttk.Entry(card, font=("Segoe UI", 11))
        self.ent_usuario.pack(fill="x", ipady=4, pady=(4, 15))
        self.ent_usuario.insert(0, "admin")
        self.ent_usuario.focus()

        # Campo: Contraseña
        lbl_pass = tk.Label(card, text="Contraseña:", font=("Segoe UI", 10, "bold"), fg="#475569", bg="white")
        lbl_pass.pack(anchor="w")

        frame_pass = tk.Frame(card, bg="white")
        frame_pass.pack(fill="x", pady=(4, 20))

        self.ent_password = ttk.Entry(frame_pass, show="*", font=("Segoe UI", 11))
        self.ent_password.pack(side="left", fill="x", expand=True, ipady=4)
        self.ent_password.insert(0, "1234")

        btn_eye = tk.Button(
            frame_pass, text="👁", font=("Segoe UI", 10), 
            bd=0, bg="#e2e8f0", activebackground="#cbd5e1", padx=8,
            command=self._toggle_password
        )
        btn_eye.pack(side="right", padx=(5, 0), fill="y")

        # Botón Ingresar
        btn_ingresar = tk.Button(
            card, text="Iniciar Sesión", font=("Segoe UI", 11, "bold"),
            fg="white", bg="#2563eb", activebackground="#1d4ed8", activeforeground="white",
            bd=0, height=2, command=self._validar_login
        )
        btn_ingresar.pack(fill="x", pady=(5, 0))

        # Permite presionar 'Enter' para iniciar sesión
        self.bind('<Return>', lambda event: self._validar_login())

    def _toggle_password(self):
        if self.mostrar_pass:
            self.ent_password.config(show="*")
            self.mostrar_pass = False
        else:
            self.ent_password.config(show="")
            self.mostrar_pass = True

    def _validar_login(self):
        usuario = self.ent_usuario.get().strip()
        password = self.ent_password.get().strip()

        # Validación básica de credenciales
        if usuario == "admin" and password == "1234":
            self.on_login_success(usuario)
            self.destroy()
        else:
            messagebox.showerror(
                "Error de Autenticación", 
                "Usuario o contraseña incorrectos.\n\nPrueba con:\nUsuario: admin\nContraseña: 1234"
            )