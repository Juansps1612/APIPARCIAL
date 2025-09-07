#!/bin/bash

# 1. Obtener todos los jugadores
curl -i http://localhost:5000/jugadores

# 2. Obtener un jugador por ID (ejemplo: 1)
curl -i http://localhost:5000/jugadores/1

# 3. Obtener un jugador inexistente (ejemplo: 99)
curl -i http://localhost:5000/jugadores/99

# 4. Crear un nuevo jugador
curl -i -X POST http://localhost:5000/jugadores \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Lionel Messi", "posicion": "Delantero", "equipo": "Inter Miami", "nacionalidad": "Argentina", "edad": 37}'

# 5. Crear un jugador con datos incompletos
curl -i -X POST http://localhost:5000/jugadores \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Cristiano Ronaldo"}'

# 6. Actualizar un jugador existente (ejemplo: 1)
curl -i -X PUT http://localhost:5000/jugadores/1 \
  -H "Content-Type: application/json" \
  -d '{"equipo": "FC Barcelona"}'

# 7. Actualizar un jugador inexistente (ejemplo: 99)
curl -i -X PUT http://localhost:5000/jugadores/99 \
  -H "Content-Type: application/json" \
  -d '{"equipo": "Equipo Fantasma"}'

# 8. Eliminar un jugador existente (ejemplo: 1)
curl -i -X DELETE http://localhost:5000/jugadores/1

# 9. Eliminar un jugador inexistente (ejemplo: 99)
curl -i -X DELETE http://localhost:5000/jugadores/99

# 10. Crear un jugador con edad inválida (texto en vez de número)
curl -i -X POST http://localhost:5000/jugadores \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Jugador Prueba", "posicion": "Defensa", "equipo": "Prueba FC", "nacionalidad": "Colombiana", "edad": "treinta"}'
