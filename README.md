# 🍬 DULCICAT - Sistema de Gestión de Golosinas 🍭

## 📌 Descripción

**DULCICAT** es una aplicación en Python que permite gestionar clientes de una tienda de golosinas utilizando una base de datos SQLite 🗄️.

El sistema crea automáticamente una base de datos llamada **`golosinas.db`** donde almacena la información de:

* 👤 Clientes
* 🍫 Productos
* 🧾 Pedidos

Actualmente, el menú implementado permite realizar operaciones CRUD sobre **clientes**.

---

## ⚙️ ¿Qué necesita para funcionar?

### ✅ Requisitos

* 🐍 Python 3.x
* 📦 Módulo `sqlite3` (incluido por defecto en Python)
* 💻 Consola o terminal para ejecutar el programa

No necesita instalar librerías externas 🎉

---

## 🗂️ Base de Datos

Al ejecutar el programa, se crea automáticamente el archivo:

```
golosinas.db
```

Y dentro se generan estas tablas:

### 👤 Tabla `clientes`

* `id_cliente` → Identificador único (AUTOINCREMENT)
* `nombre` → Nombre del cliente (obligatorio)
* `ciudad` → Ciudad del cliente
* `telefono` → Teléfono de contacto

### 🍭 Tabla `productos`

* `id_producto`
* `nombre`
* `precio`
* `stock`

*(Actualmente no se usa en el menú, pero está preparada para futuras mejoras 🚀)*

### 🧾 Tabla `pedidos`

* `id_pedido`
* `id_cliente` (clave foránea)
* `fecha`
* `total`

*(También preparada para ampliaciones futuras)*

---

## 🧠 ¿Qué hace el programa?

El sistema permite:

### 1️⃣ Crear cliente

Guarda un nuevo cliente en la base de datos.

### 2️⃣ Ver clientes

Muestra todos los clientes registrados.

### 3️⃣ Actualizar cliente

Permite modificar el nombre de un cliente mediante su ID.

### 4️⃣ Eliminar cliente

Elimina un cliente de la base de datos por ID.

### 5️⃣ Salir

Cierra el programa correctamente.

---

## ▶️ Cómo ejecutarlo

1. Guarda el archivo como por ejemplo:

```
dulcicat.py
```

2. Ejecuta en la terminal:

```
python dulcicat.py
```

3. Usa el menú interactivo 🎛️

---

## 🔄 Funcionamiento Interno

* 🔌 Se conecta a SQLite
* 🏗️ Crea las tablas si no existen
* 📋 Muestra un menú en bucle
* 💾 Guarda los cambios con `commit()`
* 🔒 Cierra la conexión al salir

---

## 🚀 Posibles mejoras

* 🛒 Gestión completa de productos
* 📦 Gestión de pedidos
* 🔎 Búsqueda de clientes
* ✏️ Actualizar más campos
* 🖥️ Interfaz gráfica (Tkinter o PyQt)
* 🌐 Versión web (Flask o Django)

---

## 📜 Licencia

Proyecto educativo 📚
Uso libre para prácticas y aprendizaje.

---

✨ **Autor:** (Jesus Clemente y David Mbado)
🍬 Proyecto: DULCICAT - Gestión de Golosinas
