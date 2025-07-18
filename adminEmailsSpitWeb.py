import streamlit as st
import re


def extract_and_clean_emails(contact_list_text):
    """
    Extrae los correos electrónicos de la lista de contactos,
    corrige los formatos '.dup' y los devuelve como una cadena.
    """
    emails = []

    # Expresión regular para encontrar el patrón de correo electrónico.
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')

    lines = contact_list_text.strip().splitlines()
    for line in lines:
        found_emails_in_line = email_pattern.findall(line)

        for email in found_emails_in_line:
            # Limpiar explícitamente ".dup" del correo encontrado
            cleaned_email = email.replace(".dup", "")
            emails.append(cleaned_email)

    return "; ".join(emails)


# --- Interfaz de Usuario con Streamlit ---

st.set_page_config(layout="wide")  # Configura el diseño para usar todo el ancho de la página

st.title("✉️ Extractor de Correos Electrónicos")

st.write(
    "Copia y pega tu lista de contactos en el cuadro de la izquierda y automáticamente obtendrás los correos listos para tu email.")

# Divide la página en dos columnas
col1, col2 = st.columns(2)

with col1:
    st.header("Entrada de Contactos")
    # `st.text_area` es el widget de Streamlit para entrada de texto multilínea
    # key="input_contacts" es importante para mantener el estado del widget
    # height=300 ajusta la altura del área de texto
    input_text = st.text_area(
        "Pega tu lista de contactos aquí:",
        height=300,
        key="input_contacts"
    )

with col2:
    st.header("Correos Listos para Pegar")
    # La lógica de procesamiento se ejecuta automáticamente cada vez que `input_text` cambia
    output_emails = extract_and_clean_emails(input_text)

    # `st.text_area` para mostrar el resultado, deshabilitado para edición
    st.text_area(
        "Correos extraídos:",
        value=output_emails,
        height=300,
        disabled=True,  # El usuario no puede escribir aquí
        key="output_emails"
    )

st.markdown("---")
st.markdown("Hecho con ❤️ en Python y Streamlit.")