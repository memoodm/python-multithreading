from multiprocessing import Process, Queue
import os
import time

def saludar_worker_queue(nombre, q_resultados):
    """
    Función worker que se ejecuta en un proceso separado.
    Pone su resultado en la cola (q_resultados).
    """
    pid = os.getpid()
    # Simular trabajo
    time.sleep(0.1) 
    saludo = f"¡Hola, {nombre}! Te saludo desde el proceso PID: {pid}"
    
    # 1. Devolver el resultado usando la Queue
    q_resultados.put(saludo) 
    
    print(f"Worker {pid} terminó de procesar a {nombre}.")

if __name__ == '__main__':
    # 1. Crear la cola de resultados
    cola_resultados = Queue()
    
    personas = ["Alicia", "Beto", "Carla", "David"]
    N_TAREAS = len(personas)
    
    print(f"Proceso principal (PID: {os.getpid()}) iniciando {N_TAREAS} procesos.")

    processes = []
    
    # 2. Crear y arrancar procesos
    for nombre in personas:
        # Pasamos la cola como argumento a la función worker
        p = Process(target=saludar_worker_queue, args=(nombre, cola_resultados))
        processes.append(p)
        p.start()

    # 3. Esperar a que todos los procesos terminen (Join)
    for p in processes:
        p.join()

    # 4. Recolectar resultados de la cola
    # Debemos saber cuántos resultados esperar (N_TAREAS)
    resultados = []
    for _ in range(N_TAREAS):
        # .get() es bloqueante hasta que hay un elemento disponible
        resultados.append(cola_resultados.get()) 

    print("\n--- Resultados de la Queue ---")
    for resultado in resultados:
        print(resultado)
        
    print("\nProceso principal terminado.")