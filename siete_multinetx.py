#importamos nuestras bibliotecas
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('Qt5Agg')
import multinetx as mx
import networkx as nx # to use graphs
#generamos nuestras redes
N = 5
g1 = mx.generators.erdos_renyi_graph(N,0.5,seed=218)#seed es la semilla para el generador de números aleatorios (predeterminado = Ninguno).
g2 = mx.generators.erdos_renyi_graph(N,0.6,seed=211)
g3 = mx.generators.erdos_renyi_graph(N,0.7,seed=208)

#Creamos una matriz dispersa LIL de dimensiones 3N x 3N, que nos servirá para describir la interconexión de capas.
adj_block = mx.lil_matrix(np.zeros((N*3,N*3)))
#Definimos el tipo de interconexión entre las capas (aquí usamos matrices de identidad conectando así uno a uno los nodos entre capas)
adj_block[0:N,N:2*N] = np.identity(N)    #L_12
adj_block[0:N,2*N:3*N] = np.identity(N)  #L_13
#adj_block[0:N,3*N:4*N] = np.identity(N)#L_14
adj_block[N:2*N,2*N:3*N] = np.identity(N)#L_23
#adj_block[N:2*N,3*N:4*N] = np.identity(N)#L_24
#adj_block[2*N:3*N,3*N:4*N] = np.identity(N)#L_34


#creamos una matriz de inter-adyacencia simétrica
adj_block += adj_block.T

#creamos la instancia del objeto MultilayerGraph
mg = mx.MultilayerGraph(list_of_layers=[g1,g2,g3],inter_adjacency_matrix=adj_block)

#damos los pesos a nuestros enlaces
mg.set_edges_weights(intra_layer_edges_weight=2,inter_layer_edges_weight=3)




#comenzamos a dibujar
fig = plt.figure()
#sacamos los ejes
ax = fig.add_subplot()
ax.axis('off')
ax.set_title('Red interconectada')

#obtenemos las posiciones
pos = mx.get_position(mg,mx.fruchterman_reingold_layout(mg.get_layer(0)),layer_vertical_shift=1.4,layer_horizontal_shift=0.0, proj_angle=7)
#dibujamos nuestros elementos
mx.draw_networkx(mg,pos=pos,ax=ax,node_size=50,with_labels=False,edge_color=[mg[a][b]['weight'] for a,b in mg.edges()],edge_cmap=plt.cm.jet_r)
#mostramos la red
plt.savefig('red_original.png')