import networkx as nx
import matplotlib.pyplot as plt

# A mano
'''G= nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=5)

print(G.edges())

camino= nx.shortest_path(G, 'A', 'D', weight='weight')
longitud= nx.shortest_path_length(G, 'A', 'D', weight='weight')

print(camino)
print(longitud)

print("El camino mas corto")'''


# desde archivos

G= nx.read_weighted_edgelist("red_ponderada.txt", nodetype=str) # formato nodo1 nodo2 peso

print(G.nodes())
print(G.edges())

caminos= dict(nx.all_pairs_dijkstra_path_length(G))
print(type(caminos))
print(caminos)

for fuente in G.nodes():
    for destino in G.nodes():
        if fuente != destino:
            print(f"El camino mas corto entre {fuente} y {destino} es: {nx.shortest_path(G, fuente, destino)}")
            print(f"La longitud del camino mas corto es:{caminos[fuente][destino]}")