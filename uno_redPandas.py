import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

matriz = pd.DataFrame({
    'A': [0, 1, 1, 0],
    'B': [1, 0, 1, 0],
    'C': [1, 1, 0, 1],
    'D': [0, 0, 1, 0],
}, index=['A', 'B', 'C', 'D']) 

miRedPandas = nx.from_pandas_adjacency(matriz)

print(matriz)
print(miRedPandas)
print("Mis nodos son: ",miRedPandas.nodes)
print("Mis enlaces son: ",miRedPandas.edges)

nx.draw(miRedPandas, with_labels=True, node_color='skyblue', node_size=1000, font_size=12, font_weight='bold')