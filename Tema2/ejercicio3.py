from multiprocessing import Process, Queue
import time
import os

def crear_fichero_datos(nombre_fichero):
    valores = [1, 2, 3, 5]
    with open(nombre_fichero, "w") as f:
        for v in valores:
            f.write(f"{v}\n")
    print(f"--- Fichero '{nombre_fichero}' creado con datos ---")

# --- Función PRODUCTOR (Lee del fichero y pone en la cola) ---
def leer_numeros_fichero(nombre_fichero, cola):
    print(f"[LECTOR] Iniciando lectura. PID={os.getpid()}")
    
    try:
        with open(nombre_fichero, "r") as f:
            for linea in f:
                numero = int(linea.strip())
                # Ponemos el número en la cola para que el otro proceso lo coja
                cola.put(numero)
                print(f"[LECTOR] Leído y encolado: {numero}")
        
    except FileNotFoundError:
        print(f"[LECTOR] Error: El fichero {nombre_fichero} no existe.")

    # IMPORTANTE: Señal de fin.
    # Añadimos None para indicar al consumidor que no hay más datos.
    cola.put(None)
    print(f"[LECTOR] Fin de lectura. Enviando señal de terminación (None).")

# --- Función CONSUMIDOR (Saca de la cola y procesa) ---
def sumar_numeros_cola(cola):
    print(f"[CALCULADOR] Esperando datos en la cola... PID={os.getpid()}")
    
    while True:
        # Obtenemos el siguiente elemento de la cola.
        # get() bloquea el proceso hasta que haya algo disponible.
        item = cola.get()
        
        # Comprobamos si es la señal de parada (Sentinel)
        if item is None:
            print("[CALCULADOR] Recibido None. Terminando proceso.")
            break
        
        # Si no es None, realizamos el cálculo
        resultado = sum(range(1, item + 1))
        print(f"   -> [CALCULADOR] Suma hasta {item} = {resultado}")

if __name__ == "__main__":
    archivo = "numeros.txt"
    crear_fichero_datos(archivo)

    print(f"[PADRE] Iniciando programa con Queue. PID={os.getpid()}")

    # 1. Creamos la Cola de comunicación
    cola_comunicacion = Queue()

    # 2. Definimos los dos procesos
    # El proceso lector necesita el nombre del archivo y la cola para escribir en ella
    p_lector = Process(target=leer_numeros_fichero, args=(archivo, cola_comunicacion))
    
    # El proceso calculador solo necesita la cola para leer de ella
    p_calculador = Process(target=sumar_numeros_cola, args=(cola_comunicacion,))

    # Iniciamos el contador de tiempo
    inicio = time.perf_counter()

    # 3. Arrancamos los procesos
    p_lector.start()
    p_calculador.start()

    # 4. Esperamos a que terminen (Sincronización)
    p_lector.join()
    p_calculador.join()

    # Paramos el contador
    fin = time.perf_counter()
    tiempo_proceso = fin - inicio

    print("[PADRE] Todos los procesos han terminado.")
    print(f"El tiempo total de ejecución ha sido {tiempo_proceso:.4f} segundos")
    
    # Limpieza (opcional)
    if os.path.exists(archivo):
        os.remove(archivo)