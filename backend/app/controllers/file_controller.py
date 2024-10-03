from app.schemas.file_schema import FileSchema
from app.services.redis_service import RedisService
from werkzeug.utils import secure_filename

class FileController:
    def __init__(self, redis_client):
        self.redis_service = RedisService(redis_client)

    def upload_files(self, files):
        file_info_list = []
        for file in files:
            filename = secure_filename(file.filename)

            # Leer el contenido del archivo
            file_content = file.read()

            # Crear una instancia del esquema del archivo
            file_schema = FileSchema(name=filename, content=file_content)

            # Almacenar la información del archivo en Redis
            self.redis_service.save_file(file_schema)

            file_info_list.append(file_schema.to_dict())

        return {"message": "Archivos subidos a Redis con éxito", "files": file_info_list}

    def get_file_info(self, file_id):
        """
        Recupera la información del archivo por su ID.
        """
        file_info = self.redis_service.get_file(file_id)
        if not file_info:
            return {"message": "Archivo no encontrado."}, 404
        return file_info
    
    def get_all_keys(self):
        return self.redis_service.get_all_files()
