import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Tk):
    def __init__(self, restaurante_servicio):
        super().__init__()
        self.servicio = restaurante_servicio
        self.title("Sistema de Gestión - Restaurante")
        self.geometry("900x580")
        self.configure(bg="#f0f2f5")

        self.botones_nav = {}
        self._crear_interfaz()
        self.mostrar_vista("inicio") # Vista por defecto

    def _crear_interfaz(self):
        # ----------------------------------------------------
        # PANEL LATERAL IZQUIERDO (SIDEBAR)
        # ----------------------------------------------------
        sidebar = tk.Frame(self, bg="#1e293b", width=200)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        lbl_titulo_app = tk.Label(
            sidebar, text="RESTAURANTE", font=("Segoe UI", 16, "bold"), 
            fg="white", bg="#1e293b", anchor="w"
        )
        lbl_titulo_app.pack(padx=20, pady=(20, 2))

        lbl_rol = tk.Label(
            sidebar, text="Administrador", font=("Segoe UI", 9), 
            fg="#94a3b8", bg="#1e293b", anchor="w"
        )
        lbl_rol.pack(padx=20, pady=(0, 20), anchor="w")

        # Botones de navegación
        self.botones_nav["inicio"] = tk.Button(
            sidebar, text="  🏠  Inicio", font=("Segoe UI", 10, "bold"),
            fg="white", bg="#1e293b", bd=0, activebackground="#334155", 
            activeforeground="white", anchor="w", padx=15,
            command=lambda: self.mostrar_vista("inicio")
        )
        self.botones_nav["inicio"].pack(fill="x", pady=2)

        self.botones_nav["usuarios"] = tk.Button(
            sidebar, text="  👥  Clientes / Personal", font=("Segoe UI", 10, "bold"),
            fg="white", bg="#1e293b", bd=0, activebackground="#334155", 
            activeforeground="white", anchor="w", padx=15,
            command=lambda: self.mostrar_vista("usuarios")
        )
        self.botones_nav["usuarios"].pack(fill="x", pady=2)

        self.botones_nav["libros"] = tk.Button(
            sidebar, text="  🍔  Menú / Platos", font=("Segoe UI", 10, "bold"),
            fg="white", bg="#1e293b", bd=0, activebackground="#334155", 
            activeforeground="white", anchor="w", padx=15,
            command=lambda: self.mostrar_vista("libros")
        )
        self.botones_nav["libros"].pack(fill="x", pady=2)

        self.botones_nav["ventas"] = tk.Button(
            sidebar, text="  🧾  Ventas / Comandas", font=("Segoe UI", 10, "bold"),
            fg="white", bg="#1e293b", bd=0, activebackground="#334155", 
            activeforeground="white", anchor="w", padx=15,
            command=lambda: self.mostrar_vista("ventas")
        )
        self.botones_nav["ventas"].pack(fill="x", pady=2)

        btn_cerrar = tk.Button(
            sidebar, text="  ➔  Cerrar sesión", font=("Segoe UI", 10, "bold"),
            fg="white", bg="#e11d48", bd=0, activebackground="#be123c", 
            activeforeground="white", anchor="w", padx=15,
            command=self._cerrar_sesion
        )
        btn_cerrar.pack(side="bottom", fill="x", pady=20)

        # BARRA DE ESTADO INFERIOR
        self.lbl_estado = tk.Label(
            self, text="Platos: 0 | Clientes: 0 | Ventas: 0 | Datos JSON locales",
            font=("Segoe UI", 9, "bold"), fg="#475569", bg="#e2e8f0", 
            anchor="w", padx=15, pady=5
        )
        self.lbl_estado.pack(side="bottom", fill="x")

        # ÁREA DE CONTENIDO DINÁMICO
        self.main_content = tk.Frame(self, bg="#f0f2f5", padx=25, pady=20)
        self.main_content.pack(side="right", fill="both", expand=True)

    def _actualizar_estilo_botones(self, vista_activa):
        for nombre, btn in self.botones_nav.items():
            if nombre == vista_activa:
                btn.config(bg="#2563eb", activebackground="#2563eb")
            else:
                btn.config(bg="#1e293b", activebackground="#334155")

    def _limpiar_contenido(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def mostrar_vista(self, nombre_vista):
        self._actualizar_estilo_botones(nombre_vista)
        self._limpiar_contenido()

        if nombre_vista == "inicio":
            self._vista_inicio()
        elif nombre_vista == "usuarios":
            self._vista_usuarios()
        elif nombre_vista == "libros":
            self._vista_libros()
        elif nombre_vista == "ventas":
            self._vista_ventas()

        self._actualizar_barra_estado()

    # ----------------------------------------------------
    # VISTAS INDIVIDUALES (RESTAURANTE)
    # ----------------------------------------------------
    def _vista_inicio(self):
        lbl_encabezado = tk.Label(
            self.main_content, text="Panel de Control", 
            font=("Segoe UI", 22, "bold"), fg="#0f172a", bg="#f0f2f5"
        )
        lbl_encabezado.pack(anchor="w", pady=(0, 15))

        # BANNER RESTAURANTE
        banner = tk.Frame(self.main_content, bg="#e11d48", padx=20, pady=20)
        banner.pack(fill="x", pady=(0, 20))

        lbl_bienvenida = tk.Label(
            banner, text="¡Bienvenido al Sistema de Restaurante!", 
            font=("Segoe UI", 16, "bold"), fg="white", bg="#e11d48"
        )
        lbl_bienvenida.pack(anchor="w")

        lbl_sub = tk.Label(
            banner, text="Gestiona el menú de platillos, comandas, personal y ventas en tiempo real.", 
            font=("Segoe UI", 10), fg="#fecdd3", bg="#e11d48"
        )
        lbl_sub.pack(anchor="w", pady=(5, 0))

        # TARJETAS DE MÉTRICAS (KPIs)
        num_productos = len(self.servicio.obtener_productos())
        num_usuarios = len(self.servicio.obtener_usuarios())
        num_ventas = len(self.servicio.obtener_ventas())

        kpi_container = tk.Frame(self.main_content, bg="#f0f2f5")
        kpi_container.pack(fill="x", pady=(0, 25))

        def crear_tarjeta(parent, titulo, valor, icono, color_borde):
            card = tk.Frame(parent, bg="white", highlightbackground=color_borde, highlightthickness=2, padx=15, pady=15)
            card.pack(side="left", fill="both", expand=True, padx=5)

            lbl_ico = tk.Label(card, text=icono, font=("Segoe UI", 20), bg="white")
            lbl_ico.pack(anchor="w")

            lbl_val = tk.Label(card, text=str(valor), font=("Segoe UI", 22, "bold"), fg="#0f172a", bg="white")
            lbl_val.pack(anchor="w", pady=(2, 0))

            lbl_tit = tk.Label(card, text=titulo, font=("Segoe UI", 9, "bold"), fg="#64748b", bg="white")
            lbl_tit.pack(anchor="w")

        crear_tarjeta(kpi_container, "Platos / Menú", num_productos, "🍔", "#f59e0b")
        crear_tarjeta(kpi_container, "Clientes / Personal", num_usuarios, "👥", "#10b981")
        crear_tarjeta(kpi_container, "Comandas / Ventas", num_ventas, "🧾", "#e11d48")

        # ACCIONES RÁPIDAS
        lbl_acciones = tk.Label(
            self.main_content, text="Acciones Rápidas", 
            font=("Segoe UI", 12, "bold"), fg="#0f172a", bg="#f0f2f5"
        )
        lbl_acciones.pack(anchor="w", pady=(0, 10))

        btn_grid = tk.Frame(self.main_content, bg="#f0f2f5")
        btn_grid.pack(fill="x")

        btn_go_ventas = tk.Button(
            btn_grid, text="📝 Registrar Nueva Venta", font=("Segoe UI", 10, "bold"),
            fg="white", bg="#0f172a", activebackground="#1e293b", activeforeground="white",
            bd=0, height=2, padx=15, command=lambda: self.mostrar_vista("ventas")
        )
        btn_go_ventas.pack(side="left", padx=(0, 10))

        btn_go_libros = tk.Button(
            btn_grid, text="🍕 Ver Menú de Platos", font=("Segoe UI", 10, "bold"),
            fg="#0f172a", bg="#e2e8f0", activebackground="#cbd5e1", activeforeground="#0f172a",
            bd=0, height=2, padx=15, command=lambda: self.mostrar_vista("libros")
        )
        btn_go_libros.pack(side="left")

    # ----------------------------------------------------
    # VISTA: CLIENTES Y PERSONAL
    # ----------------------------------------------------
    def _vista_usuarios(self):
        lbl_encabezado = tk.Label(
            self.main_content, text="Gestión de Clientes y Personal", 
            font=("Segoe UI", 20, "bold"), fg="#0f172a", bg="#f0f2f5"
        )
        lbl_encabezado.pack(anchor="w", pady=(0, 15))

        container = tk.Frame(self.main_content, bg="#f0f2f5")
        container.pack(fill="both", expand=True)

        # Configuración de estilos para la tabla
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#1e293b", foreground="white")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=30)
        style.map("Treeview", background=[("selected", "#2563eb")])

        # Card / Tabla derecha
        frame_tabla = ttk.LabelFrame(container, text=" Lista de Usuarios Registrados ", padding=15)
        frame_tabla.pack(side="right", fill="both", expand=True)

        tabla = ttk.Treeview(
            frame_tabla, 
            columns=("ID", "Nombre", "Rol"), 
            show="headings"
        )
        tabla.heading("ID", text="ID / Código")
        tabla.heading("Nombre", text="Nombre Completo")
        tabla.heading("Rol", text="Tipo / Rol")

        tabla.column("ID", width=100, anchor="center")
        tabla.column("Nombre", width=220, anchor="w")
        tabla.column("Rol", width=140, anchor="center")

        # Cargar datos
        for idx, u in enumerate(self.servicio.obtener_usuarios()):
            if isinstance(u, dict):
                tag = "even" if idx % 2 == 0 else "odd"
                rol = u.get("rol", "Cliente" if "Cliente" in u.get("nombre", "") else "Personal")
                tabla.insert("", "end", values=(u.get("id_usuario"), u.get("nombre"), rol), tags=(tag,))

        tabla.tag_configure("even", background="#ffffff")
        tabla.tag_configure("odd", background="#f8fafc")

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=scrollbar.set)

        tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # ----------------------------------------------------
    # VISTA: MENÚ Y PLATOS
    # ----------------------------------------------------
    def _vista_libros(self):
        lbl_encabezado = tk.Label(
            self.main_content, text="Menú de Platillos y Bebidas", 
            font=("Segoe UI", 20, "bold"), fg="#0f172a", bg="#f0f2f5"
        )
        lbl_encabezado.pack(anchor="w", pady=(0, 15))

        container = tk.Frame(self.main_content, bg="#f0f2f5")
        container.pack(fill="both", expand=True)

        # Configuración de estilos para la tabla
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#1e293b", foreground="white")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=30)
        style.map("Treeview", background=[("selected", "#2563eb")])

        # Card / Tabla derecha
        frame_tabla = ttk.LabelFrame(container, text=" Catálogo del Menú ", padding=15)
        frame_tabla.pack(side="right", fill="both", expand=True)

        tabla = ttk.Treeview(
            frame_tabla, 
            columns=("ID", "Producto", "Estado"), 
            show="headings"
        )
        tabla.heading("ID", text="Código")
        tabla.heading("Producto", text="Platillo / Bebida")
        tabla.heading("Estado", text="Disponibilidad")

        tabla.column("ID", width=100, anchor="center")
        tabla.column("Producto", width=260, anchor="w")
        tabla.column("Estado", width=120, anchor="center")

        # Cargar datos
        for idx, p in enumerate(self.servicio.obtener_productos()):
            if isinstance(p, dict):
                tag = "even" if idx % 2 == 0 else "odd"
                tabla.insert("", "end", values=(p.get("id_producto"), p.get("nombre"), "Disponible"), tags=(tag,))

        tabla.tag_configure("even", background="#ffffff")
        tabla.tag_configure("odd", background="#f8fafc")

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=scrollbar.set)

        tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def _vista_ventas(self):
        lbl_encabezado = tk.Label(self.main_content, text="Ventas / Comandas", font=("Segoe UI", 22, "bold"), fg="#0f172a", bg="#f0f2f5")
        lbl_encabezado.pack(anchor="w", pady=(0, 15))

        content_grid = tk.Frame(self.main_content, bg="#f0f2f5")
        content_grid.pack(fill="both", expand=True)

        # Formulario
        frame_form = ttk.LabelFrame(content_grid, text="Registrar pedido / venta", padding=15)
        frame_form.pack(side="left", fill="y", anchor="n", padx=(0, 15))

        ttk.Label(frame_form, text="Cliente / Mesero", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 2))
        self.combo_usuarios = ttk.Combobox(frame_form, state="readonly", width=32)
        self.combo_usuarios.pack(fill="x", pady=(0, 12))

        ttk.Label(frame_form, text="Platillo / Producto", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 2))
        self.combo_productos = ttk.Combobox(frame_form, state="readonly", width=32)
        self.combo_productos.pack(fill="x", pady=(0, 15))

        btn_registrar = tk.Button(
            frame_form, text="+  Registrar Venta", font=("Segoe UI", 10, "bold"),
            fg="white", bg="#2563eb", activebackground="#1d4ed8", activeforeground="white",
            bd=0, height=2, command=self._on_registrar_venta_click
        )
        btn_registrar.pack(fill="x", pady=(5, 8))

        btn_pdf = tk.Button(
            frame_form, text="📄  Generar Ticket / Reporte", font=("Segoe UI", 10, "bold"),
            fg="white", bg="#0f172a", activebackground="#1e293b", activeforeground="white",
            bd=0, height=2, command=self._generar_pdf
        )
        btn_pdf.pack(fill="x", pady=5)

        # Tabla
        frame_tabla = ttk.LabelFrame(content_grid, text="Ventas registradas", padding=10)
        frame_tabla.pack(side="right", fill="both", expand=True)

        self.tabla = ttk.Treeview(frame_tabla, columns=("Venta", "Usuario", "Libro", "Fecha"), show="headings")
        self.tabla.heading("Venta", text="N° Venta")
        self.tabla.heading("Usuario", text="Cliente / Mesero")
        self.tabla.heading("Libro", text="Platillo / Menú")
        self.tabla.heading("Fecha", text="Fecha")

        self.tabla.column("Venta", width=60, anchor="center")
        self.tabla.column("Usuario", width=120)
        self.tabla.column("Libro", width=180)
        self.tabla.column("Fecha", width=90, anchor="center")

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self._cargar_combos()
        self._actualizar_tabla_ventas()

    # ----------------------------------------------------
    # FUNCIONES Y AUXILIARES
    # ----------------------------------------------------
    def _cargar_combos(self):
        usuarios_data = self.servicio.obtener_usuarios()
        productos_data = self.servicio.obtener_productos()

        usuarios = [f"{u['id_usuario']} - {u['nombre']}" if isinstance(u, dict) else str(u) for u in usuarios_data]
        productos = [f"{p['id_producto']} - {p['nombre']}" if isinstance(p, dict) else str(p) for p in productos_data]

        self.combo_usuarios['values'] = usuarios
        self.combo_productos['values'] = productos

    def _on_registrar_venta_click(self):
        usuario = self.combo_usuarios.get()
        producto = self.combo_productos.get()

        try:
            self.servicio.registrar_venta(usuario, producto)
            self._actualizar_tabla_ventas()
            self._actualizar_barra_estado()
            messagebox.showinfo("Éxito", "Venta registrada correctamente.")
            self.combo_usuarios.set("")
            self.combo_productos.set("")
        except ValueError as err:
            messagebox.showwarning("Atención", str(err))
        except Exception as err:
            messagebox.showerror("Error", f"Error inesperado: {err}")

    def _actualizar_tabla_ventas(self):
        if not hasattr(self, 'tabla'):
            return
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        ventas = self.servicio.obtener_ventas()
        for v in ventas:
            cod_venta = f"V{v.id_venta:03d}" if isinstance(v.id_venta, int) else v.id_venta
            fecha_corta = v.fecha.split(" ")[0] if " " in str(v.fecha) else v.fecha
            self.tabla.insert("", "end", values=(cod_venta, v.usuario, v.producto, fecha_corta))

    def _actualizar_barra_estado(self):
        num_libros = len(self.servicio.obtener_productos())
        num_usuarios = len(self.servicio.obtener_usuarios())
        num_ventas = len(self.servicio.obtener_ventas())
        self.lbl_estado.config(
            text=f"Platos: {num_libros} | Clientes: {num_usuarios} | Ventas: {num_ventas} | Datos JSON locales"
        )

    def _generar_pdf(self):
        messagebox.showinfo("Reporte PDF", "Reporte generado correctamente.")

    def _cerrar_sesion(self):
        respuesta = messagebox.askyesno("Cerrar Sesión", "¿Está seguro de que desea salir del sistema?")
        if respuesta:
            self.destroy()