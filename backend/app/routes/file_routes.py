from flask import Blueprint, request, jsonify, current_app
from app.controllers.file_controller import FileController

main_bp = Blueprint('files', __name__)

@main_bp.route('/files/all', methods=['GET'])
def get_all_files():
    # Obtiene el cliente de Redis de la aplicación actual
    redis_client = current_app.redis_client
    file_controller = FileController(redis_client)

    all_keys = file_controller.get_all_keys()  # Usa el controlador para obtener todas las claves
    return jsonify(all_keys), 200

@main_bp.route('/files/add', methods=['POST'])
def add_files():
    # Obtiene el cliente de Redis de la aplicación actual
    redis_client = current_app.redis_client
    file_controller = FileController(redis_client)
    print( "--------1--------")

    if 'files' not in request.files:
        return jsonify({"message": "No se han proporcionado archivos."}), 400
    
    files = request.files.getlist('files')
    if not files:
        return jsonify({"message": "No se han seleccionado archivos."}), 400
    
    result = file_controller.upload_files(files)
    return jsonify(result), 201

@main_bp.route('/files/<string:file_id>', methods=['GET'])
def get_file(file_id):
    """
    Recupera la información del archivo por su ID.
    """
    # Obtiene el cliente de Redis de la aplicación actual
    redis_client = current_app.redis_client
    file_controller = FileController(redis_client)

    file_info = file_controller.get_file_info(file_id)
    if isinstance(file_info, tuple):  # Si es un mensaje de error
        return jsonify(file_info[0]), file_info[1]
    return jsonify(file_info)
