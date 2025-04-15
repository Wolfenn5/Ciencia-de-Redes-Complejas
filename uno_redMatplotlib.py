import networkx as nx
import matplotlib.pyplot as plt

G= nx.Graph()

G.add_nodes_from([1,2,3,4])

G.add_edges_from([(1,2), (1,3), (2,3), (3,4)])

nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=12, font_weight='bold')

plt.show()