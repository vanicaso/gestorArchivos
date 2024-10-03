class RedisService:
    def __init__(self, redis_client):
        self.redis = redis_client

    def save_file(self, file_schema):
        """
        Guarda el archivo en Redis usando su ID como clave.
        """
        self.redis.hset(file_schema.id, mapping=file_schema.to_dict())

    def get_file(self, file_id):
        """
        Recupera la información del archivo por su ID.
        """
        return self.redis.hgetall(file_id)

    def get_all_files(self):
        cursor = 0
        all_files = []

        while True:
            cursor, keys = self.redis.scan(cursor)  # Obtiene las claves
            for key in keys:
                # Suponiendo que las claves son hashes, obtenemos todos los campos del hash
                file_info = self.redis.hgetall(key)
                file_info['id'] = key  # Añadir la clave como el ID del archivo
                all_files.append(file_info)

            if cursor == 0:
                break

        return all_files