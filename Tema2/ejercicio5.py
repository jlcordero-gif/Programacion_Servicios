from multiprocessing import Process
import time
import os

def sumar_intervalo(valor1, valor2):
    """
    Suma todos los números comprendidos entre valor1 y valor2 (ambos incluidos).
    Maneja el caso en que el primer argumento sea mayor que el segundo.
    
    """
    # 1. Ordenamos los valores para saber inicio y fin
    if valor1 > valor2:
        inicio = valor2
        fin = valor1
    else:
        inicio = valor1
        fin = valor2
        
    # 2. Realizamos la suma (fin + 1 para incluir el último número)
    total = sum(range(inicio, fin + 1))
    
    print(f"[Proceso PID={os.getpid()}] Suma entre {inicio} y {fin} = {total}")

if __name__ == "__main__":
    # Pares de números para probar (incluyendo casos invertidos)
    datos_prueba = [
        (1, 5),       # Orden normal
        (5, 1),       # Orden invertido (primero > segundo)
        (10, 20),           # Rango pequeño
        (100, 200) # Rango grande
    ]
    
    lista_procesos = []
    
    print("--- Iniciando los procesos ---")
    inicio_tiempo = time.perf_counter()

    # Creación y lanzamiento de procesos
    for v1, v2 in datos_prueba:
        # Pasamos los dos argumentos a la función
        p = Process(target=sumar_intervalo, args=(v1, v2)) 
        lista_procesos.append(p)
        p.start() 

    # Sincronización: Esperar a que terminen todos
    for p in lista_procesos:
        p.join() 

    fin_tiempo = time.perf_counter()
    tiempo_total = fin_tiempo - inicio_tiempo

    print("--- Todos los procesos han terminado ---")
    print(f"Tiempo de ejecución total: {tiempo_total:.4f} segundos")