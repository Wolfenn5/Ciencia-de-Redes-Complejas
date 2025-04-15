import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist ("red.txt")
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

# Dibujo del grafo
nx.draw(G, with_labels=True, node_color='red', node_size=700, font_size=12, font_weight='bold')
plt.show()


# Probabilidad de grados
total_nodos = len(G.nodes())
print("Numero total de nodos: ", total_nodos)
probas= [frecuencia / total_nodos for frecuencia in distribucion]
print(probas)

print('Grado\tProbabilidad')
for i in range (len(probas)):
    print(f"{i}\t {probas[i]}")
# O tambien
print('Grado\tProbabilidad')
for i, proba in enumerate(probas):
    print(f"{i}\t {probas[i]}")