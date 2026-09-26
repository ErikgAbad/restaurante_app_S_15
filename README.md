# 🍽️ Sistema de Gestión de Restaurante y Comandas

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge)
![JSON](https://img.shields.io/badge/Database-JSON%20Local-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)

Un sistema de escritorio moderno, rápido e intuitivo para la administración integral de un restaurante. Permite controlar el menú de platillos, gestionar usuarios y personal, registrar comandas en tiempo real y visualizar métricas con una interfaz gráfica basada en estándares de diseño tipo Dashboard.

---

## 📸 Características de la Interfaz

* 🔐 **Módulo de Autenticación:** Pantalla de inicio de sesión segura con validación de credenciales, ventana flotante centrada y opción de visibilidad para la contraseña.
* 📊 **Dashboard Ejecutivo:** Métricas en tiempo real que muestran indicadores clave (KPIs) como el total de platillos del menú, clientes/personal registrados y ventas/comandas totales.
* 🍔 **Menú de Platillos y Bebidas:** Catálogo estructurado con lista zebra intercalada, encabezados oscuros y estados de disponibilidad.
* 👥 **Gestión de Clientes y Personal:** Visualización clara y ordenada para la administración de meseros, administradores y clientes.
* 🧾 **Registro de Comandas:** Formulario dinámico con combos desplegables para la selección rápida de clientes y platillos al registrar pedidos.
* 🎨 **Diseño Moderno:** Menú lateral plano (*Flat Dark Sidebar*), paleta de colores limpia y recursos visuales optimizados.

---

## 🔐 Credenciales de Acceso por Defecto

| Usuario | Contraseña | Rol |
| :--- | :--- | :--- |
| `admin` | `1234` | Administrador del Sistema |

---

## 🛠️ Estructura del Proyecto

El proyecto está organizado siguiendo el patrón Módulo/Servicio para separar los modelos de datos, la lógica de negocio, la persistencia y la interfaz gráfica:

```text
restaurante_app_S_15/
│
├── assets/                 # Recursos gráficos y multimedia
│   ├── Icono.png           # Icono de la aplicación
│   └── logo.png            # Logotipo del restaurante
│
├── datos/                  # Persistencia de datos en formato JSON
│   ├── productos.json      # Catálogo de platillos, bebidas y menús
│   ├── usuarios.json       # Registro de clientes, meseros y personal
│   └── ventas.json         # Historial de ventas y comandas
│
├── modelos/                # Clases de dominio y entidad
│   ├── __init__.py
│   ├── producto.py         # Modelo de Producto / Platillo
│   ├── usuario.py          # Modelo de Usuario / Cliente / Personal
│   └── venta.py            # Modelo de Venta / Comanda
│
├── servicios/              # Lógica de negocio e integración
│   ├── __init__.py
│   ├── archivo_servicio.py # Lectura y escritura de archivos JSON
│   └── restaurante_servicio.py # Gestión centralizada de operaciones
│
├── ui/                     # Interfaz de usuario (Tkinter)
│   ├── __init__.py
│   ├── login_view.py       # Ventana de autenticación (Login)
│   └── main_view.py        # Dashboard principal y vistas conmutables
│
├── main.py                 # Punto de entrada de la aplicación
└── README.md               # Documentación general del proyecto

```

---

## 🚀 Instalación y Ejecución

### Requisitos Previos

* **Python 3.8+** instalado en el equipo.
* Módulo **Tkinter** (incluido por defecto en las instalaciones estándar de Python).

### Pasos para Ejecutar

1. **Clonar o descargar el repositorio:**
```bash
git clone [https://github.com/tu-usuario/restaurante_app_S_15.git](https://github.com/tu-usuario/restaurante_app_S_15.git)
cd restaurante_app_S_15

```


2. **Iniciar la aplicación:**
```bash
python main.py

```



---

## 📝 Flujo de Uso

1. **Autenticación:** Inicie sesión utilizando el usuario `admin` y la contraseña `1234`.
2. **Navegación:** Utilice la barra lateral izquierda para alternar entre las secciones:
* **Inicio:** Visualice el resumen ejecutivo e indicadores de rendimiento.
* **Clientes / Personal:** Consulte los usuarios registrados en el sistema.
* **Menú / Platos:** Revise el catálogo de comida y bebida disponible.
* **Ventas / Comandas:** Registre un nuevo pedido seleccionando al cliente y el producto correspondiente.
