import logging
import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain import hub

import a_env_vars

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuración de variables globales
EMBEDDING_MODEL_NAME = a_env_vars.EMBEDDING_MODEL_NAME
DATA_PATH = a_env_vars.DATA_PATH
CHROMA_PATH = a_env_vars.CHROMA_PATH
os.environ["OPENAI_API_KEY"] = a_env_vars.OPENAI_API_KEY

# Inicialización de la base de datos Chroma y el modelo de incrustación
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=OpenAIEmbeddings())
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})
llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18")
prompt = hub.pull("rlm/rag-prompt")

def recuperar_documentos(query):
    """
    Recupera documentos relevantes en base a la consulta proporcionada.
    
    :param query: Consulta en formato de texto.
    :return: Lista de documentos relevantes.
    """
    try:
        docs = retriever.invoke(query)
        for documento in docs:
            logging.info(f"Documento recuperado: {documento.metadata}")
        return docs
    except Exception as e:
        logging.error(f"Error al recuperar documentos: {e}")
        return []

def consultar_llm(context, question):
    """
    Consulta al modelo de lenguaje con el contexto y la pregunta proporcionados.
    
    :param context: Contexto en formato de texto.
    :param question: Pregunta en formato de texto.
    :return: Respuesta generada por el modelo de lenguaje.
    """
    try:
        template = f"Eres un asistente que siempre cita las fuentes que utiliza.\nCon el contexto que te doy, responde la pregunta.\nContexto: {context}\nPregunta: {question}\nSi no lo puedes resolver a partir del contexto que te doy, dime que la información es insuficiente."
        logging.info("Template creado para la consulta al LLM")
        result = llm.invoke(template)
        logging.info(f"Respuesta generada: {result.content}")
        return result.content
    except Exception as e:
        logging.error(f"Error al consultar el LLM: {e}")
        return "Lo siento, no pude procesar tu solicitud en este momento."
