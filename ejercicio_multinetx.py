import numpy as np
import matplotlib.pyplot as plt
import multinetx as mx
import networkx as nx # to use graphs
import pandas as pd
import community as cm

N = 32

g1=mx.read_edgelist('2018_complementaria_aristas.txt',nodetype=int,data=(("weight", int),))#de momento no sabemos que cumplen
g2=nx.read_edgelist('2019_complementaria_aristas.txt',nodetype=int,data=(("weight", int),))
g3=nx.read_edgelist('2020_complementaria_aristas.txt',nodetype=int,data=(("weight", int),))
g4=nx.read_edgelist('2021_complementaria_aristas.txt',nodetype=int,data=(("weight", int),))
g5=mx.generators.erdos_renyi_graph(32,0.7)#aleatoria
g6=mx.generators.watts_strogatz_graph(32, 10, 0.8)#mundo pequeño
g7=mx.generators.barabasi_albert_graph(32, 15)#libre de escala
print(g1.nodes())
print(g2.nodes())
print(g3.nodes())
print(g4.nodes())
print(g5.nodes())
print(g6.nodes())
print(g7.nodes())
print(type(g1))
numcapas=7
adj_block = mx.lil_matrix(np.zeros((N*numcapas,N*numcapas)))#lista de listas (lil)

adj_block[0: N, N:2*N] = np.identity(N) #generamos las conexiones entre la capa 1 y la capa 2
adj_block[N:2*N, 2*N:3*N] = np.identity(N) # L_23
adj_block[2*N:3*N, 3*N:4*N] = np.identity(N) # L_34
adj_block[3*N:4*N, 4*N:5*N] = np.identity(N) # L_45
adj_block[4*N:5*N, 5*N:6*N] = np.identity(N) # L_56
adj_block[5*N:6*N, 6*N:7*N] = np.identity(N) # L_67



adj_block += adj_block.T#al hacer la transpuesta, hacemos los vinculos alreves (de regreso)

mg = mx.MultilayerGraph(list_of_layers=[g1,g2,g3,g4,g5,g6,g7],inter_adjacency_matrix=adj_block)
print(type(mg))

mg.set_edges_weights(inter_layer_edges_weight=8)#esto es para el peso de los enlaces intercapa (l1 a l2, l2 a l3, ... l6 a l7)
mg.set_intra_edges_weights(layer=4,weight=5)
mg.set_intra_edges_weights(layer=5,weight=6)
mg.set_intra_edges_weights(layer=6,weight=7)
print(g1)
print(g2)
print(g3)
print(g4)
print(g5)
print(g6)
print(g7)
print(mg)
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(211)
ax1.imshow(mx.adjacency_matrix(mg,weight='weight').todense(),cmap=plt.cm.jet_r)
ax1.set_title('Matriz de supra-adyacencia')
plt.savefig('matriz_supraadyacencia.png')
ax2 = fig.add_subplot(122)
ax2.axis('off')
ax2.set_title('Red multiplex')
pos = mx.get_position(mg,
mx.fruchterman_reingold_layout(mg.get_layer(0)),
layer_vertical_shift=1.4,
layer_horizontal_shift=0.0,
proj_angle=7)
print(pos)
mx.draw_networkx(mg,pos=pos,ax=ax2,node_size=80,with_labels=False,
edge_color=[mg[a][b]['weight'] for a,b in mg.edges()],
edge_cmap=plt.cm.jet_r)
plt.savefig('red_comp_cnombres.png')



# metricas (densidad, clustering, distribucion de grado, modularidad, diametro) de cada capa
mg.list_of_layers #g1,g2,g3,g4,g5,g6,g7
for i, capa in enumerate(mg.list_of_layers):
  print(f"Clustering de capa {i}: ", nx.clustering(capa))
  print(f"Densidad de la capa {i}: ", nx.density(capa))
  print(f"Modularidad de la capa {i}: ", nx.community.modularity(capa, nx.community.label_propagation_communities(capa)))
  distribucion_grado= nx.degree_histogram(capa)
  print(f"Distribución de grado de la capa {i}: ")
  for grado, cantidad in enumerate(distribucion_grado):
        print(f"Grado {grado}: {cantidad} nodos")
  print(f"Diametro de la capa {i}: ", nx.diameter(capa)) 
  # centralidades (vector propio, intermediacion, grado y cercania) de cada capa
  print(f"Centralidad de grado de la capa {i}: ", nx.degree_centrality(capa))
  print(f"Centralidad de intermediacion de la capa {i}: ", nx.betweenness_centrality(capa))
  print(f"Centralidad de vector propio de la capa {i}: ", nx.eigenvector_centrality(capa))
  print(f"Centralidad de cercania de la capa {i}: ", nx.closeness_centrality(capa)) 
  print("\n")





# red completa
print(f"Coeficiente de clustering de la general: ", mx.average_clustering(mg))
print(f"Promedio de los caminos mas cortos: ",mx.average_shortest_path_length(mg))
print(f"Diametro de la red: ", mx.average_shortest_path_length(mg))
print(f"Densidad de la red: ", mx.density(mg))
#print(f"Modularidad", mx.community.modularity(mg))
# centralidades (vector propio, intermediacion, grado y cercania) de cada capa
print(f"Centralidad de intermediacion: ", mx.betweenness_centrality(mg))
print(f"Centralidad de vector propio: ", mx.eigenvector_centrality(mg, max_iter=100, tol=0.0006)) # en algun punto puede que falle
print(f"Centralidad de cercania: ",mx.closeness_centrality(mg))
print(f"Centralidad de grado: ", mx.degree_centrality(mg))
