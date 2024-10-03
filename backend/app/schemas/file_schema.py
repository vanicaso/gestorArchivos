import base64
import hashlib
import time

class FileSchema:
    def __init__(self, name, content):
        date = time.time()
        self.id = self.generate_hash_key(date, name) # Genera un identificador único
        self.name = name
        self.date = date  # Guarda la fecha actual como timestamp
        self.size = len(content)  # Tamaño del contenido del archivo
        self.content = base64.b64encode(content).decode('utf-8')  # Contenido del archivo, puede ser binario o string

    def to_dict(self):
        """
        Convierte el esquema a un diccionario para ser almacenado en Redis.
        """
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "size": self.size,
            "content": self.content  # Asegúrate de que el contenido sea adecuado para Redis
        }
    
    def generate_hash_key(self,date: str, filename: str) -> str:
        # Concatenar la fecha y el nombre del archivo
        combined_string = f"{date}{filename}"

        # Crear un hash SHA256
        hash_object = hashlib.sha256(combined_string.encode())
        
        # Obtener el hash en hexadecimal
        hex_dig = hash_object.hexdigest()
        
        # Tomar los primeros 8 caracteres del hash
        return hex_dig[:8]
