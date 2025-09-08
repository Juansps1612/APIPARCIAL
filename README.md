# CRUDRESTAPI - Jugadores de Fútbol  

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)](https://flask.palletsprojects.com/)  
[![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)](https://www.sqlite.org/)  

Este proyecto es una **API RESTful** desarrollada en Python usando **Flask**, diseñada para gestionar jugadores de fútbol y su información básica.  
Los datos se almacenan en una base de datos **SQLite** (a través de SQLAlchemy) y la API permite realizar operaciones CRUD sobre los jugadores.  

---

## Estructura del Proyecto  

- `src/app.py`: Punto de entrada de la aplicación Flask. Registra los blueprints y levanta el servidor.  
- `src/controllers/jugador_controller.py`: Define los endpoints de la API para gestionar jugadores.  
- `src/models/jugador.py`: Modelo de datos del jugador.  
- `src/config/database.py`: Configuración de la base de datos SQLite con SQLAlchemy.  
- `curl_examples.sh`: Ejemplos de comandos `curl` para probar la API.  
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.  

---

## Endpoints disponibles  

- **GET** `/jugadores`: Obtiene la lista de todos los jugadores.  
- **GET** `/jugadores/<id>`: Obtiene la información de un jugador por su ID.  
- **POST** `/jugadores`: Crea un nuevo jugador. Requiere un JSON con:  
  ```json
  {
    "nombre": "Lionel Messi",
    "edad": 37,
    "equipo": "Inter Miami",
    "posicion": "Delantero",
    "nacionalidad": "Argentina"
  }

- **PUT** `/jugadores/<id>`: Actualiza los datos de un jugador existente.

- **DELETE** `/jugadores/<id>`: Elimina un jugador por su ID.

## Ejemplos de uso

- Obtener todos los jugadores:

curl -i http://localhost:5000/jugadores

- Obtener un jugador por ID:

curl -i http://localhost:5000/jugadores/1

- Crear un nuevo jugador:

curl -i -X POST http://localhost:5000/jugadores \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Cristiano Ronaldo", "edad": 40, "equipo": "Al Nassr", "posicion": "Delantero", "nacionalidad": "Portugal"}'

- Actualizar un jugador existente:

curl -i -X PUT http://localhost:5000/jugadores/1 \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Kylian Mbappé", "edad": 26, "equipo": "Real Madrid", "posicion": "Delantero", "nacionalidad": "Francia"}'

- Eliminar un jugador:

curl -i -X DELETE http://localhost:5000/jugadores/1

## Requisitos

- Python 3.12+

## Instalación, depuración y ejecución

1. Ejecutar archivo con toda la configuración inicial: bash setup.sh

   1.1 Una vez se haya terminado de configurar todo correctamente, nos dirigimos al archivo .env recien creado y cambiamos la contraseña de la base datos por        la que se puso al momento de configurar

2. Ejecuta la aplicación: python3 src/app.py

## Notas

- Los datos se almacenan en SQLite, en un archivo jugadores.db.

- Los endpoints devuelven respuestas en formato JSON y usan los códigos de error HTTP apropiados.

- Puedes extender el modelo para agregar más campos o relaciones según tus necesidades.
