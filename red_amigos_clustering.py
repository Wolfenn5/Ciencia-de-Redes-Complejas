###################################
# Alumnos: 
#     Alejandro Trejo Cienfuegos
#     2193076829
#     Omar Soto Valles
#     2193077022
#     Pablo Roberto Garcia Torres
#     219303560                  
####################################

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community

# Definir la red de amistades
amistades = {
    'Alejandro': ['Brandon Juarez', 'Valery Martinez', 'Sara Garcia'],
    'Omar': ['Brandon Juarez', 'Carlos Reyes', 'Daniel Flores'],
    'Roberto': ['Giovanni Saldivar', 'Daniel Reyes', 'Iñaki Garcia', 'Felipe Juarez','Brandon Juarez']
}

# Crear el grafo
G = nx.Graph()

# Agregar nodos y aristas según la definición de amistades
for persona, amigos in amistades.items():
    G.add_node(persona)
    for amigo in amigos:
        G.add_edge(persona, amigo)

# Calcular coeficiente de clustering
clustering = nx.average_clustering(G)
print("Coeficiente de clustering:", clustering)

# Calcular diámetro
diametro = nx.diameter(G)
print("Diametro: ", diametro)


# Calcular densidad
densidad = nx.density(G)
print("Densidad:", densidad)

# Calcular componentes conexos
componentes_conectados = nx.number_connected_components(G)
print("Componentes conexos:", componentes_conectados)

#calcular la modularidad


# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_weight='bold')
plt.title("Red de amistades")
plt.show()

# Dibujar el histograma
distribucion = nx.degree_histogram(G)
plt.bar(range(len(distribucion)), distribucion)
plt.xlabel('Grado')
plt.ylabel('Número de nodos')
plt.title('Distribución de grado')
plt.show()
