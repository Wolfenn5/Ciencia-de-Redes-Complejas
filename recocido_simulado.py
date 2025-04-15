import random
import math
import csv

def leer_grafo_desde_csv(nombre_archivo):
    grafo = {}
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        matriz_adyacencia = list(lector_csv)
        
        for i in range(len(matriz_adyacencia)):
            grafo[i] = set()
            for j in range(len(matriz_adyacencia[i])):
                if matriz_adyacencia[i][j] == '1':  # Asumimos que el CSV contiene '1' para adyacencias y '0' para no adyacencias
                    grafo[i].add(j)
    
    return grafo

def vertex_separator_simulated_annealing(graph, initial_solution=None, max_iterations=1000, initial_temperature=100, cooling_rate=0.95):
    # Inicializamos el conjunto separador y su tamaño
    best_separator = initial_solution if initial_solution else set(random.sample(list(graph.keys()), random.randint(1, len(graph)-1)))
    best_separator_size = len(best_separator)

    # Inicializamos la temperatura actual
    temperature = initial_temperature

    for _ in range(max_iterations):
        # Generamos una solución vecina intercambiando un vértice entre el conjunto separador y el resto del grafo
        separator_candidate = best_separator.copy()
        vertex_to_remove = random.choice(list(separator_candidate))
        vertex_to_add = random.choice(list(set(graph.keys()) - separator_candidate))
        separator_candidate.remove(vertex_to_remove)
        separator_candidate.add(vertex_to_add)

        # Calculamos el tamaño del conjunto separador vecino
        separator_candidate_size = len(separator_candidate)

        # Calculamos la diferencia en el tamaño del conjunto de separación entre la solución actual y la vecina
        delta_size = separator_candidate_size - best_separator_size

        # Verificamos si la solución vecina es mejor que la actual o si se acepta con una cierta probabilidad
        if delta_size < 0 or random.random() < math.exp(-delta_size / temperature):
            best_separator = separator_candidate
            best_separator_size = separator_candidate_size
        
        # Actualizamos la temperatura
        temperature *= cooling_rate
    
    return best_separator

# Ejemplo de uso
nombre_archivo = 'matriz_adyacencia_2023_01_cuantificado.csv'  # Nombre del archivo CSV
grafo = leer_grafo_desde_csv(nombre_archivo)
separator = vertex_separator_simulated_annealing(grafo)
print("Conjunto separador encontrado por recocido simulado:", separator)
