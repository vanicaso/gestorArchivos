from flask import Flask
import redis

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Inicializa el cliente de Redis
    app.redis_client = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], decode_responses=True)

    # Importa y registra las rutas
    from app.routes.file_routes import main_bp
    app.register_blueprint(main_bp)

    return app
