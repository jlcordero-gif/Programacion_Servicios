from multiprocessing import Pool
import os
import time

def saludar(nombre: str) -> None:
    """
    Función que ejecuta cada proceso del Pool.
    """
    # Imprimimos el saludo y el PID para ver qué proceso lo atiende
    print(f"[HIJO] Hola {nombre}. PID={os.getpid()}")
    
    # Simula una pequeña pausa para que la concurrencia sea más evidente
    # Si quitamos esto, el overhead de crear procesos podría tardar más que la tarea misma.
    time.sleep(0.1) 

def ejecutar_prueba_pool(num_procesos, lista_nombres):
    """
    Ejecuta la salutación concurrentemente con un tamaño de Pool específico.
    """
    print(f"\n--- Iniciando Pool con {num_procesos} proceso(s) ---")
    
    inicio = time.perf_counter()
    
    with Pool(processes=num_procesos) as pool:
        pool.map(saludar, lista_nombres)
        
    fin = time.perf_counter()
    tiempo = fin - inicio
    
    print(f"-> Tiempo total con {num_procesos} procesos: {tiempo:.4f} segundos")

if __name__ == "__main__":
    print(f"[PADRE] Iniciando programa. PID={os.getpid()}")

    nombres = ["Juan", "Pedro", "Carlos"] * 4
    
    ejecutar_prueba_pool(num_procesos=1, lista_nombres=nombres)

    ejecutar_prueba_pool(num_procesos=2, lista_nombres=nombres)

    ejecutar_prueba_pool(num_procesos=4, lista_nombres=nombres)

    print("\n[PADRE] Todas las ejecuciones han terminado.")