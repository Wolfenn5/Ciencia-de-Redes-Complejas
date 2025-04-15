import networkx as nx
import matplotlib.pyplot as plt


red= "red.txt"
G= nx.watts_strogatz_graph(20,4,0.6) # red de mundo pequeño

# centralidad de grado
centralidad_grado= nx.degree_centrality(G)

# centralidad de intermediacion
centralidad_intermediacion= nx.betweenness_centrality(G)

# centralidad de vector propio
centralidad_vector_propio= nx.eigenvector_centrality(G)

# centralidad de cercania
centralidad_cercania= nx.closeness_centrality(G)

#print(centralidad_grado)
#print(centralidad_intermediacion)
#print(centralidad_vector_propio)
#print(centralidad_cercania)

# se necesita rankear ordenando de mayor a menor
# centralidad de grado
centralidad_grado_ordenada = sorted(centralidad_grado.items(), key=lambda x: x[1], reverse=True) # se ordenan los elementos en base a su valor de centralidad, reverse= true es para ordenar de mayor a menor
print(centralidad_grado_ordenada)
print(type(centralidad_grado_ordenada))


centralidad_dic= {n: centralidad for n, centralidad in centralidad_grado_ordenada}
colores = [centralidad_dic[nodo] for nodo in G.nodes()]

nx.draw(G,with_labels=True, node_color=colores, cmap=plt.cm.Blues, node_size=200, font_size=12, font_weight='bold') # cmap=plt.cm.Blues entre mas oscuro es mas central
plt.show()



# centralidad de intermediacion
centralidad_intermediacion_ordenada = sorted(centralidad_intermediacion.items(), key=lambda x: x[1], reverse=True) # se ordenan los elementos en base a su valor de centralidad, reverse= true es para ordenar de mayor a menor
print(centralidad_intermediacion_ordenada)
print(type(centralidad_intermediacion_ordenada))


centralidad_dic= {n: centralidad for n, centralidad in centralidad_intermediacion_ordenada}
colores = [centralidad_dic[nodo] for nodo in G.nodes()]

nx.draw(G,with_labels=True, node_color=colores, cmap=plt.cm.Blues, node_size=200, font_size=12, font_weight='bold') # cmap=plt.cm.Blues entre mas oscuro es mas central
plt.show()


# centralidad de vector propio
centralidad_vector_propio_ordenada = sorted(centralidad_vector_propio.items(), key=lambda x: x[1], reverse=True) # se ordenan los elementos en base a su valor de centralidad, reverse= true es para ordenar de mayor a menor
print(centralidad_vector_propio_ordenada)
print(type(centralidad_vector_propio_ordenada))


centralidad_dic= {n: centralidad for n, centralidad in centralidad_vector_propio_ordenada}
colores = [centralidad_dic[nodo] for nodo in G.nodes()]

nx.draw(G,with_labels=True, node_color=colores, cmap=plt.cm.Blues, node_size=200, font_size=12, font_weight='bold') # cmap=plt.cm.Blues entre mas oscuro es mas central
plt.show()


# centralidad de cercania
centralidad_cercania_ordenada = sorted(centralidad_cercania.items(), key=lambda x: x[1], reverse=True) # se ordenan los elementos en base a su valor de centralidad, reverse= true es para ordenar de mayor a menor
print(centralidad_cercania_ordenada)
print(type(centralidad_cercania_ordenada))


centralidad_dic= {n: centralidad for n, centralidad in centralidad_cercania_ordenada}
colores = [centralidad_dic[nodo] for nodo in G.nodes()]

nx.draw(G,with_labels=True, node_color=colores, cmap=plt.cm.Blues, node_size=200, font_size=12, font_weight='bold') # cmap=plt.cm.Blues entre mas oscuro es mas central
plt.show()