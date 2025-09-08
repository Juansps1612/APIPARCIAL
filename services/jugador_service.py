from config.database import SessionLocal
from models.jugador import Jugador
from collections import OrderedDict

def get_all_jugadores():
    session = SessionLocal()
    jugadores = session.query(Jugador).all()
    result = []
    for j in jugadores:
        result.append(OrderedDict([
            ("id", j.id),
            ("nombre", j.nombre),
            ("edad", j.edad),
            ("equipo", j.equipo),
            ("nacionalidad", j.nacionalidad),
            ("posicion", j.posicion),
        ]))
    session.close()
    return result

def get_jugador_by_id(jugador_id):
    session = SessionLocal()
    jugador = session.query(Jugador).filter(Jugador.id == jugador_id).first()
    result = None
    if jugador:
        result = OrderedDict([
            ("id", jugador.id),
            ("nombre", jugador.nombre),
            ("edad", jugador.edad),
            ("equipo", jugador.equipo),
            ("nacionalidad", jugador.nacionalidad),
            ("posicion", jugador.posicion),
        ])
    session.close()
    return result

def create_jugador(data):
    session = SessionLocal()

    existing = session.query(Jugador).filter(
        Jugador.nombre == data["nombre"],
        Jugador.equipo == data["equipo"]
    ).first()

    if existing:
        session.close()
        return {"error": f"El jugador '{data['nombre']}' ya está registrado en el equipo '{data['equipo']}'"}

    jugador = Jugador(
        nombre=data["nombre"],
        posicion=data["posicion"],
        equipo=data["equipo"],
        nacionalidad=data["nacionalidad"],
        edad=data["edad"]
    )
    session.add(jugador)
    session.commit()
    session.refresh(jugador)

    result = OrderedDict([
        ("id", jugador.id),
        ("nombre", jugador.nombre),
        ("edad", jugador.edad),
        ("equipo", jugador.equipo),
        ("nacionalidad", jugador.nacionalidad),
        ("posicion", jugador.posicion),
    ])
    session.close()
    return result

def update_jugador(jugador_id, data):
    session = SessionLocal()
    jugador = session.query(Jugador).filter(Jugador.id == jugador_id).first()
    if not jugador:
        session.close()
        return None

    jugador.nombre = data.get("nombre", jugador.nombre)
    jugador.posicion = data.get("posicion", jugador.posicion)
    jugador.equipo = data.get("equipo", jugador.equipo)
    jugador.nacionalidad = data.get("nacionalidad", jugador.nacionalidad)
    jugador.edad = data.get("edad", jugador.edad)

    session.commit()
    session.refresh(jugador)

    result = OrderedDict([
        ("id", jugador.id),
        ("nombre", jugador.nombre),
        ("edad", jugador.edad),
        ("equipo", jugador.equipo),
        ("nacionalidad", jugador.nacionalidad),
        ("posicion", jugador.posicion),
    ])
    session.close()
    return result

def delete_jugador(jugador_id):
    session = SessionLocal()
    jugador = session.query(Jugador).filter(Jugador.id == jugador_id).first()
    if not jugador:
        session.close()
        return False
    session.delete(jugador)
    session.commit()
    session.close()
    return True
