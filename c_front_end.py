#lanzar con streamlit run c_front_end.py en el terminal
import config
import b_backend
import streamlit as st
from streamlit_chat import message

# Set up the Streamlit app
st.title(config.TITLE)
st.write(config.DESCRIPTION)

# Initialize session state for questions and answers
if 'preguntas' not in st.session_state:
    st.session_state.preguntas = []
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = []

def click():
    """
    Handles the user's click event when submitting a question.
    Retrieves the response from the backend and updates the session state.
    """
    if st.session_state.user != '':
        pregunta = st.session_state.user
        try:
            respuesta = b_backend.consulta(pregunta)
            st.session_state.preguntas.append(pregunta)
            st.session_state.respuestas.append(respuesta)
        except Exception as e:
            st.error(f"Error al procesar la consulta: {e}")
        finally:
            # Limpiar el input de usuario después de enviar la pregunta (opcional)
            st.session_state.user = ''

def mostrar_conversacion():
    """
    Displays the conversation history in reverse order.
    """
    if st.session_state.preguntas:
        for i in range(len(st.session_state.respuestas) - 1, -1, -1):
            message(st.session_state.respuestas[i], key=str(i))

        # Opción para continuar la conversación
        continuar_conversacion = st.checkbox('¿Quieres hacer otra pregunta?')
        if not continuar_conversacion:
            st.session_state.preguntas = []
            st.session_state.respuestas = []

# Create a form for user input
with st.form('my-form'):
   query = st.text_input('¿En qué te puedo ayudar?:', key='user', help='Pulsa Enviar para hacer la pregunta')
   submit_button = st.form_submit_button('Enviar', on_click=click)

# Show conversation history
mostrar_conversacion()