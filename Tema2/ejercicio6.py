from multiprocessing import Pool
import time
import os

def sumar_intervalo(valor1, valor2):
    """
    Función trabajadora: Suma el intervalo entre dos números.
    Gestiona internamente cuál es el mayor y cuál el menor.
    """
    # Determinamos el inicio y el fin independientemente del orden de entrada
    inicio = min(valor1, valor2)
    fin = max(valor1, valor2)
    
    # Realizamos la suma
    total = sum(range(inicio, fin + 1))
    
    print(f"[PID {os.getpid()}] Suma del intervalo {inicio}-{fin} = {total}")
    return total

if __name__ == "__main__":
    # Datos de entrada: Una lista de TUPLAS.
    # Cada tupla contiene los dos argumentos (valor1, valor2) que espera la función.
    datos_para_procesar = [
        (1, 10),      # Orden normal
        (20, 10), # Orden invertido (mayor, menor)
        (5, 1),            # Rango pequeño
        (1, 25) # Otro rango grande
    ]
    
    print(f"--- Iniciando Pool con starmap para {len(datos_para_procesar)} tareas ---")
    
    inicio_tiempo = time.perf_counter()

    # Creamos el Pool. Python decidirá cuántos procesos usar (suele ser el nº de CPUs)
    # o podemos forzarlo con processes=X
    with Pool() as pool:
        # Usamos starmap porque la función 'sumar_intervalo' recibe 2 argumentos.
        # starmap desempaqueta cada tupla de la lista en los argumentos de la función.
        pool.starmap(sumar_intervalo, datos_para_procesar)

    fin_tiempo = time.perf_counter()
    tiempo_total = fin_tiempo - inicio_tiempo

    print("--- Todos los procesos han terminado ---")
    print(f"Tiempo de ejecución total: {tiempo_total:.4f} segundos")