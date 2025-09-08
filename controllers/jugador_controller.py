from flask import Blueprint, jsonify, request
from services.jugador_service import (
    get_all_jugadores,
    get_jugador_by_id,
    create_jugador,
    update_jugador,
    delete_jugador
)

jugador_bp = Blueprint("jugador_bp", __name__)

@jugador_bp.route("/jugadores", methods=["GET"])
def get_jugadores():
    return jsonify(get_all_jugadores()), 200

@jugador_bp.route("/jugadores/<int:jugador_id>", methods=["GET"])
def get_jugador(jugador_id):
    jugador = get_jugador_by_id(jugador_id)
    if jugador is None:
        return jsonify({"error": "Jugador no encontrado"}), 404
    return jsonify(jugador), 200

@jugador_bp.route("/jugadores", methods=["POST"])
def create_jugador_route():
    if not request.json:
        return jsonify({"error": "Datos inválidos"}), 400
    
    required_fields = ["nombre", "posicion", "equipo", "nacionalidad", "edad"]
    if not all(field in request.json for field in required_fields):
        return jsonify({"error": "Faltan campos requeridos"}), 400
    
    jugador = create_jugador(request.json)
    
    # 🔹 Si la respuesta contiene un error, devolvemos 400
    if "error" in jugador:
        return jsonify(jugador), 400

    return jsonify(jugador), 201

@jugador_bp.route("/jugadores/<int:jugador_id>", methods=["PUT"])
def update_jugador_route(jugador_id):
    if not request.json:
        return jsonify({"error": "Datos inválidos"}), 400
    
    jugador = update_jugador(jugador_id, request.json)
    if jugador is None:
        return jsonify({"error": "Jugador no encontrado"}), 404
    return jsonify(jugador), 200

@jugador_bp.route("/jugadores/<int:jugador_id>", methods=["DELETE"])
def delete_jugador_route(jugador_id):
    success = delete_jugador(jugador_id)
    if not success:
        return jsonify({"error": "Jugador no encontrado"}), 404
    return jsonify({"resultado": "Jugador eliminado"}), 200
