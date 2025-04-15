import networkx as nx
import matplotlib.pyplot as plt

G= nx.Graph()
nodos = ['A', 'B', 'C', 'D', 'E']
enlaces = [('A', 'B'), ('C', 'D'), ('B', 'C'), ('A', 'E'), ('A', 'A')]
G.add_nodes_from(nodos)
G.add_edges_from(enlaces)
print(G)
print(G.nodes())
print(G.edges())


distribucion = nx.degree_histogram(G)
print(distribucion)
# generar el histograma
plt.bar(range(len(distribucion)), distribucion, width=0.8, color='red')
plt.title("Grafica de distribucion de grados")
plt.xlabel("Grado")
plt.ylabel("Numero de nodos")
plt.grid(True) # muestra rejillas y aparte se puede cambiar el color, numero de rejillas etc
plt.show()

posiciones = {'A':(0,0), 'B':(1,1), 'C':(2,2), 'D':(3,1), 'E':(4,0)} #clave (nodo), valor (coordenadas)

nx.draw(G, pos= posiciones, with_labels=True, node_color='red', node_size=1000, font_size=12, font_weight='bold')
plt.show()