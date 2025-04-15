import networkx as nx
import matplotlib.pyplot as plt

# Redes Regulares
# red anillo de 10 nodos
'''grafica_anillo = nx.cycle_graph(10)
print(grafica_anillo)

nx.draw(grafica_anillo, with_labels=True, node_color='red', node_size=700, font_size=12, font_weight='bold')
plt.show()'''


# red malla
'''grafica_malla = nx.grid_2d_graph(10,10)
print(grafica_malla)

nx.draw(grafica_malla, with_labels=True, node_color='red', node_size=700, font_size=12, font_weight='bold')
plt.show()'''


# red arbol donde cada nodo tendra 2 hijos y 5 niveles 2^5 en el ultimo nivel habra 32 nodos, en el 4to nivel 2^4 16 nodos
'''grafica_arbol = nx.balanced_tree(2,5)
print(grafica_arbol)

nx.draw(grafica_arbol, with_labels=True, node_color='red', node_size=700, font_size=12, font_weight='bold')
plt.show()'''






# red aleatoria de 10 nodos con probabilidad de 0.2
grafica_aleatoria = nx.erdos_renyi_graph(10, 0.2)
print(grafica_aleatoria)
nx.draw(grafica_aleatoria, with_labels=True, node_color='red', node_size=700, font_size=12, font_weight='bold')
plt.show()