# 📚 Sistema de Gestión de Talleres Universitarios

Este proyecto es una aplicación web integral desarrollada para la asignatura de **Programación IV**. Permite la administración completa (CRUD) de talleres de formación y el registro de estudiantes, utilizando una arquitectura de microservicios basada en contenedores.

## 👥 Integrantes del Grupo
* **Base de Datos:** Erick Martínez
* **Backend:** Raul Olaya
* **Frontend:** Abdel Arteaga

## 🛠️ Tecnologías Utilizadas
* **Backend:** Python 3.10 con el framework **Flask** y **SQLAlchemy** como ORM.
* **Base de Datos:** **PostgreSQL 15** (Contenerizada).
* **Frontend:** HTML5, CSS3 (**Bootstrap 5**) y JavaScript Vanilla.
* **Despliegue y Orquestación:** **Docker** y **Docker Compose**.
* **IDE de Desarrollo:** PyCharm Community Edition 2024.3.3.

## 📂 Estructura del Proyecto
```text
talleres-formacion-pf/
├── backend/           # Lógica del servidor, modelos y API REST
├── frontend/          # Interfaz de usuario (Admin y Estudiantes)
├── database/          # Scripts SQL de inicialización de la BD
└── docker-compose.yml # Orquestador de todos los servicios
```
## 🚀 Instrucciones de Instalación y Uso

### 1. Requisitos Previos
* Tener instalado **Docker Desktop** y que esté en ejecución.
* Tener instalado **Git** (opcional, para clonar el repo).

### 2. Clonar y Preparar
Asegúrarse de estar en la carpeta raíz del proyecto donde se encuentra el archivo `docker-compose.yml`.

### 3. Ejecución con Docker
Abrir terminal de PyCharm y ejecutar el siguiente comando:
```bash
docker-compose up --build
```
## Este comando realizará lo siguiente:
* Descargará las imágenes de PostgreSQL y Nginx.
* Construirá la imagen personalizada para el Backend de Flask.
* Creará las tablas automáticamente en la base de datos.
* Iniciará todos los servicios.

### 4. Acceso al Sistema
Una vez que la terminal muestre que los servicios están listos, accede a través de tu navegador:
* Frontend (Estudiantes): http://localhost:8080/index.html
* Panel de Administración: http://localhost:8080/admin.html
* API Backend (JSON): http://localhost:5000/workshops

### 🛠️ Comandos
* Detener el sistema: docker-compose down
* Limpiar base de datos y reiniciar: docker-compose down -v && docker-compose up --build


