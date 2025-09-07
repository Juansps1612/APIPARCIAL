from sqlalchemy import Column, Integer, String, UniqueConstraint
from config.database import Base

class Jugador(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    posicion = Column(String(50), nullable=False)
    equipo = Column(String(100), nullable=False)
    nacionalidad = Column(String(50), nullable=False)
    edad = Column(Integer, nullable=False)

    # 🔹 Restricción única: no puede repetirse el mismo jugador en el mismo equipo
    __table_args__ = (
        UniqueConstraint("nombre", "equipo", name="uq_nombre_equipo"),
    )

