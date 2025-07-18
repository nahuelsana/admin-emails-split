import subprocess
import time

def reiniciar_explorer():
    """
    Reinicia el proceso explorer.exe en Windows.
    """
    print("Intentando terminar el proceso explorer.exe...")
    try:
        # Terminar el proceso explorer.exe
        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=True)
        print("explorer.exe terminado exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al terminar explorer.exe: {e}")
        print("Asegúrate de ejecutar el script con privilegios de administrador si el problema persiste.")
        return

    # Dar un pequeño tiempo para que el sistema termine el proceso completamente
    time.sleep(2)

    print("Intentando iniciar el proceso explorer.exe...")
    try:
        # Iniciar el proceso explorer.exe
        # El comando 'start' es una función incorporada del shell de comandos de Windows.
        # Shell=True es necesario para que subprocess pueda interpretar el comando 'start'.
        subprocess.Popen("explorer.exe", shell=True)
        print("explorer.exe iniciado exitosamente.")
    except Exception as e:
        print(f"Error al iniciar explorer.exe: {e}")
        print("Puede que necesites reiniciar manualmente si el problema persiste.")

if __name__ == "__main__":
    reiniciar_explorer()
    print("\nEl proceso de reinicio de explorer.exe ha finalizado.")