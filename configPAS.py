import os

def borrar_contenido_archivo(ruta_archivo):
    """
    Borra el contenido de un archivo especificado.

    Args:
        ruta_archivo (str): La ruta completa del archivo a editar.
    """
    try:
        # Abrimos el archivo en modo de escritura ('w').
        # Si el archivo existe, su contenido se borrará.
        # Si no existe, se creará un archivo vacío.
        with open(ruta_archivo, 'w') as archivo:
            # No necesitamos escribir nada, ya que el objetivo es borrar el contenido.
            # El archivo se truncará al abrirlo en modo 'w'.
            pass
        print(f"El contenido del archivo '{ruta_archivo}' ha sido borrado exitosamente.")
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al intentar borrar el contenido del archivo: {e}")

# Definimos la ruta completa del archivo
ruta_del_archivo = r"C:\ProgramData\InTouch Health\Carestation\config\LocalSipContacts.xml"

# Llamamos a la función para borrar el contenido del archivo
borrar_contenido_archivo(ruta_del_archivo)