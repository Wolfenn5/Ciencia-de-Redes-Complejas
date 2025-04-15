import networkx as nx
import matplotlib.pyplot as plt

G= nx.DiGraph() # DiGraph porque es dirigido

G.add_nodes_from(['A','B','C','D','E'])

G.add_edges_from([('A','B'), ('A','C'), ('B','C'), ('C','D'), ('D','E'), ('E','A')])

nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=12, font_weight='bold')

print(type (G))
print(G)
print("Mis nodos son: ",G.nodes)
print("Mis enlaces son: ",G.edges)

plt.show()
