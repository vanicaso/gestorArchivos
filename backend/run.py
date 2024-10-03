# backend/run.py
from flask import Flask
from flask_cors import CORS  # Importa la extensión CORS
from app import create_app

app = create_app()

# Habilita CORS para permitir solicitudes desde el frontend
CORS(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
