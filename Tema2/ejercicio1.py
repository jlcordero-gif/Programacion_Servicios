from multiprocessing import Process
import os
import time 

def saludar(nombre: str) -> None:
    print(f"[HIJO] Hola {nombre}. PID={os.getpid()}")

if __name__ == "__main__":
    print(f"[PADRE]. PID={os.getpid()}")

    # Nota la coma en args=("Ana",). Es fundamental para que sea una tupla.
    p = Process(target = saludar, args=("Ana",))
    inicio = time.perf_counter()
    p.start()
    p.join()
    fin = time.perf_counter()
    tiempo_proceso = fin - inicio

    print("[PADRE] El proceso ha terminado")
    print(f"El proceso ha tardado {tiempo_proceso:.2} segundos")