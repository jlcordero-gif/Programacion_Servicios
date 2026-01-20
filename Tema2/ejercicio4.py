# ejercicio4.py
from multiprocessing import Process, Pipe
import time
import os

# --- Función auxiliar para generar el fichero ---
def crear_fichero_datos(nombre_fichero):
    valores = [1, 2, 3, 5]
    with open(nombre_fichero, "w") as f:
        for v in valores:
            f.write(f"{v}\n")
    print(f"--- Fichero '{nombre_fichero}' creado ---")

# --- Proceso EMISOR (Lee fichero y envía por Pipe) ---
def leer_numeros_fichero(nombre_fichero, conn):
    """
    Lee del fichero y envía datos por el extremo de la tubería (conn).
    [cite_start]Usa send() como indica la documentación[cite: 58, 61].
    """
    print(f"[LECTOR] Iniciando. PID={os.getpid()}")
    try:
        with open(nombre_fichero, "r") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    numero = int(linea)
                    # Enviamos el número por la tubería
                    conn.send(numero)
                    print(f"[LECTOR] Enviado: {numero}")
        
    except FileNotFoundError:
        print(f"[LECTOR] Error: Fichero no encontrado.")

    # Enviamos None para avisar de que no hay más datos
    conn.send(None)
    print(f"[LECTOR] Fin de lectura. Enviado None.")
    conn.close() # Es buena práctica cerrar la conexión 

# --- Proceso RECEPTOR (Recibe por Pipe y suma) ---
def sumar_numeros_pipe(conn):
    """
    Recibe datos por el extremo de la tubería (conn) y calcula la suma.
    Usa recv() como indica la documentación[cite: 58, 63].
    """
    print(f"[CALCULADOR] Esperando datos... PID={os.getpid()}")
    
    while True:
        try:
            # Recibimos el dato usando recv(). Bloquea hasta recibir algo.
            dato = conn.recv()
            
            if dato is None:
                print("[CALCULADOR] Recibido None. Terminando.")
                break
            
            # Realizamos la suma
            resultado = sum(range(1, dato + 1))
            print(f"   -> [CALCULADOR] Suma hasta {dato} = {resultado}")

        except EOFError:
            print("[CALCULADOR] La conexión se cerró inesperadamente.")
            break
    
    conn.close() # Cerramos conexión al terminar 

if __name__ == "__main__":
    archivo = "numeros_pipe.txt"
    crear_fichero_datos(archivo)

    print(f"[PADRE] Iniciando comunicación con PIPE. PID={os.getpid()}")

    # 1. Creación de la Tubería (Pipe)
    # [cite_start]Pipe devuelve dos objetos de conexión [cite: 58, 68]
    left, right = Pipe()

    # 2. Definición de Procesos
    # [cite_start]Pasamos un extremo al lector y el otro al calculador [cite: 69, 70]
    p1 = Process(target=leer_numeros_fichero, args=(archivo, left))
    p2 = Process(target=sumar_numeros_pipe, args=(right,))

    inicio = time.perf_counter()

    # [cite_start]3. Ejecución [cite: 71, 72]
    p1.start()
    p2.start()

    # [cite_start]4. Sincronización [cite: 10]
    p1.join()
    p2.join()

    fin = time.perf_counter()
    print("[PADRE] Todos los procesos han terminado.")
    print(f"Tiempo total: {fin - inicio:.4f} segundos")
    
    # Limpieza del fichero creado
    if os.path.exists(archivo):
        os.remove(archivo)