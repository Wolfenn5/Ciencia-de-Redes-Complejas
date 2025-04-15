import networkx as nx
import matplotlib.pyplot as plt
import community 
#importamos la biblioteca para calcular la modularidad
#se instala con pip install modularity

#funcion para calcular y mostrar las métricas estructurales
def calcular_y_mostrar_metricas(G):
    #distribucion de grados
    grados = [grado for nodo, grado in G.degree()]
    plt.hist(grados, bins='auto', color='skyblue', alpha=0.7)
    plt.title("Distribución de Grados")
    plt.xlabel("Grado")
    plt.ylabel("Frecuencia")
    plt.show()

    #coeficiente de clustering para cada nodo
    clustering = nx.clustering(G)
    print("Coeficiente de Clustering para cada nodo:")
    for nodo, coeficiente in clustering.items():
        print(f"Nodo {nodo}: {coeficiente}")

    #diametro de la red
    diametro = nx.diameter(G)
    print(f"\nDiámetro de la red: {diametro}")

    #densidad de la red
    densidad = nx.density(G)
    print(f"Densidad de la red: {densidad}")

    #caminos más cortos entre cualquier par de nodos
    caminos_cortos = dict(nx.all_pairs_shortest_path_length(G))
    print("\nCaminos más cortos entre cualquier par de nodos:")
    for origen, destinos in caminos_cortos.items():
        for destino, longitud in destinos.items():
            print(f"De {origen} a {destino}: {longitud}")

    #centralidad de grado
    centralidad_grado = nx.degree_centrality(G)
    print("\nCentralidad de Grado:")
    for nodo, centralidad in centralidad_grado.items():
        print(f"Nodo {nodo}: {centralidad}")

    #centralidad de cercanía
    centralidad_cercania = nx.closeness_centrality(G)
    print("\nCentralidad de Cercanía:")
    for nodo, centralidad in centralidad_cercania.items():
        print(f"Nodo {nodo}: {centralidad}")

    #modularidad (utilizando python-louvain)
    particion = community.best_partition(G)
    modularidad = community.modularity(particion, G)
    print(f"\nModularidad de la red: {modularidad}")


G = nx.read_edgelist("red.txt")

calcular_y_mostrar_metricas(G)
