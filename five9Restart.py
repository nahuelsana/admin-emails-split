import subprocess
import time
import os

def reiniciar_proceso_five9(ruta_completa_ejecutable, nombre_proceso_taskkill):
    """
    Reinicia un proceso específico de Five9 en Windows usando su ruta completa y nombre de ejecutable.
    Argumentos:
        ruta_completa_ejecutable (str): La ruta completa al archivo .exe para iniciar el proceso.
        nombre_proceso_taskkill (str): El nombre del ejecutable para terminar el proceso (ej. "Five9Softphone.exe").
    """
    print(f"Intentando terminar el proceso: {nombre_proceso_taskkill}...")
    try:
        # Usamos /im para especificar la imagen del proceso a terminar
        subprocess.run(["taskkill", "/f", "/im", nombre_proceso_taskkill], check=True)
        print(f"{nombre_proceso_taskkill} terminado exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al terminar {nombre_proceso_taskkill}: {e}")
        # No retornamos aquí, intentaremos iniciar incluso si no se pudo terminar
        # porque a veces el proceso ya no está corriendo.

    time.sleep(6) # Espera un poco para asegurar que el proceso se cerró

    print(f"Intentando iniciar el proceso: {ruta_completa_ejecutable}...")
    try:
        # Aseguramos que la ruta esté entre comillas por si contiene espacios
        comando_inicio = f'start "" "{ruta_completa_ejecutable}"'
        # Usamos shell=True para que 'start' funcione correctamente
        subprocess.Popen(comando_inicio, shell=True)
        print(f"{os.path.basename(ruta_completa_ejecutable)} iniciado exitosamente.")
    except Exception as e:
        print(f"Error al iniciar {ruta_completa_ejecutable}: {e}")
        print("Puede que necesites iniciarlo manualmente si el problema persiste.")

if __name__ == "__main__":
    print("Reiniciando procesos de Five9...")

    # Definir los procesos de Five9 con sus rutas completas y nombres para taskkill
    procesos_five9 = [
        {
            "ruta_completa": r"C:\Users\NSanabria\AppData\Roaming\Five9\Five9Softphone-10.0\Five9SoftphoneSupervisor.exe",
            "nombre_taskkill": "Five9SoftphoneSupervisor.exe"
        },
        {
            "ruta_completa": r"C:\Users\NSanabria\AppData\Local\Five9\Five9Softphone-10.0\bin\14.0.1\Five9Softphone.exe",
            "nombre_taskkill": "Five9Softphone.exe"
        },
        {
            "ruta_completa": r"C:\Users\NSanabria\AppData\Local\Five9\Five9Softphone-10.0\bin\14.0.1\Five9SoftphoneService.exe",
            "nombre_taskkill": "Five9SoftphoneService.exe"
        },
        {
            "ruta_completa": r"C:\Users\NSanabria\AppData\Local\Five9\Five9Softphone-10.0\bin\14.0.1\Five9SoftphoneTray.exe",
            "nombre_taskkill": "Five9SoftphoneTray.exe"
        }
    ]

    # for proceso in procesos_five9:
    #     reiniciar_proceso_five9(proceso["ruta_completa"], proceso["nombre_taskkill"])
    #     print("-" * 30) # Separador visual entre procesos

    reiniciar_proceso_five9(r"C:\Users\NSanabria\AppData\Roaming\Five9\Five9Softphone-10.0\Five9SoftphoneSupervisor.exe","Five9SoftphoneSupervisor.exe")

    print("\nProceso de reinicio de Five9 finalizado.")