import networkx as nx

# se va a quitar el 3 o 4% de los elementos que tienen mas importancia para ver que pasa

def centralidad_de_grado(G, distribucion_de_grado):
    centralidad= {}
    n= len(G) # numero de nodos de la red
    for nodo in G.nodes():
        # grado del nodo / nodos de la red -1
        centralidad[nodo]= distribucion_de_grado[nodo] / (n-1)
    return centralidad


'''def centralidad_de_intermediacion(G):
    centralidad = {}
    n = len(G)
    for nodo in G.nodes():
        centralidad[nodo] = 0.0
    for nodo in G.nodes():
        caminos_mas_cortos = nx.shortest_path(G)
        for origen in G.nodes():
            for destino in G.nodes():
                if origen != destino and origen != nodo and destino != nodo:
                    num_caminos_mas_cortos = len(caminos_mas_cortos[origen][destino])
                    num_caminos_por_nodo = sum(1 for camino in caminos_mas_cortos[origen][destino] if nodo in camino)
                    centralidad[nodo] += num_caminos_por_nodo/num_caminos_mas_cortos
    return centralidad'''


def centralidad_de_intermediacion(G):
    centralidad = {}
    n = len(G)
    for nodo in G.nodes():
        centralidad[nodo] = 0.0
    for nodo in G.nodes():
        for origen in G.nodes():
            for destino in G.nodes():
                if origen != destino and origen != nodo and destino != nodo:
                    try:
                        caminos_mas_cortos = nx.shortest_path(G, source=origen, target=destino)
                        num_caminos_mas_cortos = len(caminos_mas_cortos)
                        num_caminos_por_nodo = sum(1 for camino in caminos_mas_cortos if nodo in camino)
                        centralidad[nodo] += num_caminos_por_nodo/num_caminos_mas_cortos
                    except nx.NetworkXNoPath:
                        pass
    return centralidad





red= "red.txt"
G= nx.read_edgelist(red)
distribucion_grados= dict(G.degree())
print(distribucion_grados)
centralidad_grado_personalizada= centralidad_de_grado(G, distribucion_grados)
print(centralidad_grado_personalizada)
centralidad_intermediacion_personalizada= centralidad_de_intermediacion(G)
print(centralidad_intermediacion_personalizada)
centralidad3= nx.betweenness_centrality(G)
print(centralidad3)