Sistema de Gestión de Notas de Laboratorio
Descripción

El Sistema de Gestión de Notas de Laboratorio es una aplicación de escritorio desarrollada en Python con Tkinter, diseñada para crear, buscar, visualizar y eliminar notas de forma sencilla y organizada.

Este proyecto está dividido en dos módulos principales:

logica.py: Maneja toda la lógica y estructura de datos.

main_gui.py: Proporciona la interfaz gráfica para el usuario.

Funcionalidades

Agregar nuevas notas con título y descripción

Buscar notas en tiempo real

Eliminar notas seleccionadas

Visualizar todas las notas en una tabla

Contador automático de notas guardadas

IDs únicos generados automáticamente

Estructura del Proyecto
📂 SistemaNotasLaboratorio
│── logica.py        # Lógica de datos: agregar, eliminar, buscar, listar
│── main_gui.py      # Interfaz gráfica en Tkinter
│── README.md        # Archivo de documentación


(Puedes quitar el ícono de la carpeta si también lo deseas, dime y lo ajusto)

Requisitos

Python 3.8 o superior

Tkinter (incluido en la instalación estándar de Python en la mayoría de sistemas)

Instalación y Ejecución

Clona o descarga este repositorio.

Abre la carpeta del proyecto en tu equipo.

Ejecuta el archivo principal con el siguiente comando:

python main_gui.py

Funcionamiento Interno

El proyecto usa almacenamiento interno basado en una lista en memoria:

notas_laboratorio = [
    {"id": 1, "titulo": "Ejemplo", "descripcion": "Texto de ejemplo"}
]


Cada vez que se agrega una nota, se asigna un ID incremental automático.

Nota: Actualmente los datos no se guardan en un archivo ni base de datos. Al cerrar la aplicación, las notas se eliminan. (Esto puede mejorarse en futuras versiones.)

Mejoras Futuras (Propuestas)

Guardar notas en archivo JSON o base de datos SQLite

Posibilidad de editar notas existentes

Control de usuarios

Sistema de categorías

Exportación de notas a PDF o TXT

Autor

Juan Manuel Londoño Ríos
Año: 2025
