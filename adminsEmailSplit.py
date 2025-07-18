import tkinter as tk
from tkinter import scrolledtext
import re

last_input_text = ""


def procesar_contactos():
    global last_input_text
    print("DEBUG: La función procesar_contactos ha sido llamada.")
    input_text = input_textbox.get("1.0", tk.END)
    print(f"DEBUG: Contenido crudo del input_textbox:\n---INICIO---\n{input_text}---FIN---")

    stripped_input_text = input_text.strip()
    if not stripped_input_text:
        print("DEBUG: Cuadro de entrada vacío o solo espacios en blanco. Vaciando output.")
        output_textbox.config(state=tk.NORMAL)
        output_textbox.delete("1.0", tk.END)
        output_textbox.config(state=tk.DISABLED)
        last_input_text = stripped_input_text
        return

    emails = []
    lines = stripped_input_text.splitlines()

    # Expresión regular para encontrar el patrón de correo electrónico.
    # Esta vez, no nos preocupamos por el .dup en la expresión regular
    # porque lo eliminaremos después. Esto la hace más robusta para la captura.
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')

    for line in lines:
        print(f"DEBUG: Procesando línea: '{line}'")
        found_emails_in_line = email_pattern.findall(line)  # findall devuelve una lista de todas las coincidencias

        if found_emails_in_line:
            print(f"DEBUG: Correos encontrados en la línea (antes de limpieza): {found_emails_in_line}")
            for email in found_emails_in_line:
                # Limpiar explícitamente ".dup" del correo encontrado
                cleaned_email = email.replace(".dup", "")
                emails.append(cleaned_email)
            print(f"DEBUG: Correos añadidos (después de limpieza): {emails[-len(found_emails_in_line):]}")
        else:
            print("DEBUG: No se encontraron correos en esta línea.")

    output_email_list = "; ".join(emails)
    print(f"DEBUG: Correos extraídos (final): {output_email_list}")

    output_textbox.config(state=tk.NORMAL)
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, output_email_list)
    output_textbox.config(state=tk.DISABLED)


def check_for_input_changes():
    global last_input_text
    current_input_text = input_textbox.get("1.0", tk.END).strip()

    if current_input_text != last_input_text:
        print("DEBUG: Se detectó un cambio en el input_textbox.")
        procesar_contactos()
        last_input_text = current_input_text

    app.after(100, check_for_input_changes)


app = tk.Tk()
app.title("Procesador de Contactos y Correos")
app.geometry("1000x500")

input_textbox = scrolledtext.ScrolledText(app, width=60, height=20, wrap=tk.WORD, undo=True, font=('Consolas', 8))
input_textbox.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

output_textbox = scrolledtext.ScrolledText(app, width=60, height=20, wrap=tk.WORD, state=tk.DISABLED, font=('Consolas', 8))
output_textbox.pack(side=tk.RIGHT, padx=10, pady=10, expand=True, fill=tk.BOTH)

input_textbox.bind("<Tab>", lambda event: output_textbox.focus_set())
output_textbox.bind("<Tab>", lambda event: input_textbox.focus_set())

check_for_input_changes()

app.mainloop()