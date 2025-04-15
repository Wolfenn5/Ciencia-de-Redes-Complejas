import networkx as nx
import numpy as np

matriz = np.array([[0, 1, 0], 
                   [1, 0, 1], 
                   [0, 1, 0]])


miNuevaRed = nx.from_numpy_array(matriz) #convierte la matriz en un objeto de red NetworkX

print(type(miNuevaRed))
