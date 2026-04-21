import os
import logging
from paramiko import RSAKey
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Configuración básica de logging
logging.basicConfig(level=logging.DEBUG)

# Ruta para almacenar los archivos
STORAGE_PATH = '/path/to/storage'

# Crear un autorizador
authorizer = DummyAuthorizer()

# Aseguramos que la carpeta de almacenamiento existe
if not os.path.exists(STORAGE_PATH):
    os.makedirs(STORAGE_PATH)

# Permitir acceso anónimo a la carpeta de almacenamiento
authorizer.add_anonymous(STORAGE_PATH, perm='elradfmw')

# Crear un manejador de FTP
handler = FTPHandler
handler.authorizer = authorizer

# Establecer las configuraciones de seguridad SFTP (opcional, podemos añadir claves)
private_key = RSAKey.generate(2048)
private_key.write_private_key_file('/path/to/private.key')

# Crear el servidor FTP
ftp_server = FTPServer(('0.0.0.0', 22), handler)

# Iniciar el servidor
ftp_server.serve_forever()

# Informar que el servidor está corriendo
print("Servidor SFTP iniciado correctamente")