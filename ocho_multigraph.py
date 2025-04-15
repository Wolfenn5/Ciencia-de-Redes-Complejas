import networkx as nx
import matplotlib.pyplot as plt

# G= nx.MultiGraph()
# G.add_edges_from([(1,2), (1,2), (2,3), (3,4), (1,1)])
# print(G.edges())
# pos= nx.spring_layout(G)
# print(pos)
# nx.draw_networkx_nodes(G,pos)
# #plt.show()

# for edge in G.edges():
#     nx.draw_networkx_edges(G, pos, edgelist=[edge], width=G.number_of_edges(edge[0], edge[1]))

# plt.show()

# print(nx.degree(G))



G=nx.MultiGraph ([(1,2),(1,2),(1,2),(3,1),(3,2)])
pos = nx.random_layout(G)
nx.draw_networkx_nodes(G, pos, node_color = 'g', node_size = 100, alpha = 1)#
ax = plt.gca()
for e in G.edges:#pasamos todos los atributos
    ax.annotate("",
                xy=pos[e[0]], xycoords='data',
                xytext=pos[e[1]], textcoords='data',
                arrowprops=dict(arrowstyle="-", color="r",
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
                                ),
                                ),
                )
plt.axis('off')
plt.show()