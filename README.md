📚 Sistema de Gestión de Talleres (Workshops)
Este proyecto es una aplicación web completa desarrollada para la asignatura de Programación IV. 
Permite la administración de talleres (CRUD) y el registro de estudiantes, utilizando una arquitectura de microservicios con contenedores.

👥 Integrantes del Grupo
Base de Datos: [Erick Martínez]
Backend: [Raul Olaya]
Frontend: [Abdel Arteaga]

🛠️ Tecnologías Utilizadas
Backend: Python 3.10 con Flask y SQLAlchemy.
Base de Datos: PostgreSQL 15.
Frontend: HTML5, CSS3 (Bootstrap 5) y JavaScript Vanilla.
Despliegue: Docker y Docker Compose.
IDE: PyCharm Community Edition 2024.3.3.

📂 Estructura del Proyecto
text
talleres-formacion-pf/
├── backend/           # Lógica del servidor y API REST
├── frontend/          # Interfaz de usuario (Admin y Estudiantes)
├── database/          # Scripts de inicialización SQL
└── docker-compose.yml # Orquestador de contenedores

🚀 Instrucciones de Instalación y Uso
1. Requisitos Previos
Tener instalado Docker Desktop y que esté en ejecución.
Tener instalado Git (opcional, para clonar el repo).
2. Clonar y Preparar
Asegúrate de estar en la carpeta raíz del proyecto donde se encuentra el archivo docker-compose.yml.
3. Ejecución con Docker
Abre una terminal (puede ser la de PyCharm) y ejecuta el siguiente comando:
bash
docker-compose up --build
Usa el código con precaución.
Este comando realizará lo siguiente:
Descargará las imágenes de PostgreSQL y Nginx.
Construirá la imagen personalizada para el Backend de Flask.
Creará las tablas automáticamente en la base de datos.
Iniciará todos los servicios.

4. Acceso al Sistema
Una vez que la terminal muestre que los servicios están listos, accede a través de tu navegador:
Frontend (Estudiantes): http://localhost:8080/index.html
Panel de Administración: http://localhost:8080/admin.html
API Backend (JSON): http://localhost:5000/workshops

🛠️ Comandos
Detener el sistema: docker-compose down
Limpiar base de datos y reiniciar: docker-compose down -v && docker-compose up --build

