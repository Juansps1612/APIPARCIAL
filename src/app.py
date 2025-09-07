from flask import Flask
import sys
import os

# Aseguramos que el proyecto vea los módulos (carpetas fuera de src)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.jugador_controller import jugador_bp
from config.database import engine, Base

# Crear tablas si no existen
def create_tables():
    Base.metadata.create_all(bind=engine)

app = Flask(__name__)

# 🔹 Esto evita que Flask jsonify reordene las claves
app.config["JSON_SORT_KEYS"] = False

# Registrar blueprint
app.register_blueprint(jugador_bp)

if __name__ == "__main__":
    create_tables()
    app.run(debug=True, host="0.0.0.0", port=5000)

