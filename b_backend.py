from core import *


def consulta(input_usuario):
    contexto = recuperar_documentos(input_usuario)
    resultado =  consultar_llm(input_usuario,contexto)
    return(resultado);