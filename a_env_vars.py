# a_env_vars.py
import os
# Clave API de OpenAI - Considera almacenarla en un archivo .env para mayor seguridad
OPENAI_API_KEY = 'tu clave'
# Nombre del modelo de incrustación utilizado
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

# Ruta a los datos
DATA_PATH = r""

# Ruta al repositorio de Chroma
CHROMA_PATH = r""

# Variables de entorno para la configuración del proyecto
#os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY  # Clave API de OpenAI
#os.environ['CHROMA_PATH'] = CHROMA_PATH        # Ruta al directorio de Chroma para almacenamiento persistente
#os.environ['DATA_PATH'] = DATA_PATH            # Ruta al directorio donde se almacenan los documentos