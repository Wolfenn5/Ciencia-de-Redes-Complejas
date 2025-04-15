import networkx as nx
import matplotlib.pyplot as plt

#funcion para calcular la distribución de grados de una capa
def calcular_distribucion_de_grados(red):
    distribucion = {}
    for nodo, grado in red.degree():
        if grado in distribucion:
            distribucion[grado] += 1
        else:
            distribucion[grado] = 1
    return distribucion

#funcion para calcular el coeficiente de clustering de una capa
def calcular_coeficiente_de_clustering(red):
    return nx.average_clustering(red)

#funcion para calcular el diámetro de una capa
def calcular_diametro(red):
    return nx.diameter(red)

#funcion para calcular la densidad de una capa
def calcular_densidad(red):
    return nx.density(red)

#funcion para dibujar la red
def dibujar_capa(red, posiciones, color, titulo):
    nx.draw_networkx_nodes(red, posiciones, node_color=color, node_size=200)
    nx.draw_networkx_edges(red, posiciones)
    nx.draw_networkx_labels(red, posiciones)
    plt.title(titulo)

#aqui ahora si empieza lo bueno...

#creamos las capas de la red utilizando modelos de generación de reds
capa1 = nx.watts_strogatz_graph(100, 6, 0.1)  #red de mundo pequeño
capa2 = nx.barabasi_albert_graph(100, 5)      #red libre de escala
capa3 = nx.erdos_renyi_graph(100, 0.1)        #red aleatoria

#mandamos a calcular las medidas para cada capa
distribucion_c1 = calcular_distribucion_de_grados(capa1)
distribucion_c2 = calcular_distribucion_de_grados(capa2)
distribucion_c3 = calcular_distribucion_de_grados(capa3)

coeficiente_c1 = calcular_coeficiente_de_clustering(capa1)
coeficiente_c2 = calcular_coeficiente_de_clustering(capa2)
coeficiente_c3 = calcular_coeficiente_de_clustering(capa3)

diametro_c1 = calcular_diametro(capa1)
diametro_c2 = calcular_diametro(capa2)
diametro_c3 = calcular_diametro(capa3)

densidad_c1 = calcular_densidad(capa1)
densidad_c2 = calcular_densidad(capa2)
densidad_c3 = calcular_densidad(capa3)

####################OJOOOOOOOOOOO###################
#aqui deberan calcular los resultados combinados para la multicapa

#################### Distribucion de grados global ###################################
#En este diccionarios vamos a guardar todas las distribuciones de las 3 redes
distribucion_combinada = {}
#Recorremos las 3 redes y si el grado no existe en el diccionario se agrega la entrada al diccionario con la clave grado y el valor inicial 0
#En caso de que si este se incrementa el valor existente en el diccionario para el grado actual con la frecuencia
for grado, frecuencia in distribucion_c1.items():
    if grado not in distribucion_combinada:
        distribucion_combinada[grado] = 0
    distribucion_combinada[grado] += frecuencia

for grado, frecuencia in distribucion_c2.items():
    if grado not in distribucion_combinada:
        distribucion_combinada[grado] = 0
    distribucion_combinada[grado] += frecuencia

for grado, frecuencia in distribucion_c3.items():
    if grado not in distribucion_combinada:
        distribucion_combinada[grado] = 0
    distribucion_combinada[grado] += frecuencia

#Calculamos suma global de las frecuencias totales de las tres redes
distribucion_combinada_global = 0
distribucion_combinada_global += sum(valor for valor in distribucion_c1.values())
distribucion_combinada_global += sum(valor for valor in distribucion_c2.values())
distribucion_combinada_global += sum(valor for valor in distribucion_c2.values())

#Normalizamos la disstribucion combinada
distribucion_grados_normalizada = {}

for grado, frecuencia in distribucion_combinada.items():
    frecuencia_normalizada = frecuencia / distribucion_combinada_global
    distribucion_grados_normalizada[grado] = frecuencia_normalizada

################################### Coeficiente combinado ##########################################
#En caso de que la red sea independiente
#pondracion1 = coeficiente_c1 * C1
#pondracion2 = coeficiente_c2 * C2
#pondracion3 = coeficiente_c3 * C2
#Si es acoplada (multiplex) simplemente sacamos en promedio sin ponderar
coeficiente_combinado = (coeficiente_c1  + coeficiente_c2 + coeficiente_c3) / 3

########################################### Diametro multicapa #################################################3
#Bscamos el diametro mas grande y ese sera el de toda la red
diametro_combinado =  max(diametro_c1, diametro_c2, diametro_c3)

################################################################################################3
#Calculamos las conexiones posibles y las conexiones presentes y hacemos la division
conexiones_posibles = len(capa1) + len(capa2) + len(capa3)
conexiones_posibles *= conexiones_posibles -1
conexiones_presentes = (densidad_c1 * conexiones_posibles) + (densidad_c2 * conexiones_posibles) + ( densidad_c3 * conexiones_posibles)
densidad_combinada = conexiones_presentes / conexiones_posibles

#sacamos las posiciones con nx.spring_layout... si recuerdan, en clase les comenté que era como gephi hace fruchterman reingold
posiciones_c1 = nx.spring_layout(capa1)
posiciones_c2 = nx.spring_layout(capa2)
posiciones_c3 = nx.spring_layout(capa3)

plt.figure(figsize=(15, 5))
#hacemos los subplots
plt.subplot(131)
dibujar_capa(capa1, posiciones_c1, 'red', 'Capa 1')

plt.subplot(132)
dibujar_capa(capa2, posiciones_c2, 'blue', 'Capa 2')

plt.subplot(133)
dibujar_capa(capa3, posiciones_c3, 'green', 'Capa 3')

plt.tight_layout()
plt.show()

#asi impriman los resultados
print("Distribución de grados combinada:", distribucion_combinada)
print("Distribución de grados combinada normalizada:", distribucion_grados_normalizada)
print("Coeficiente de clustering combinado:", coeficiente_combinado)
print("Diámetro combinado:", diametro_combinado)
print("Densidad combinada:", densidad_combinada)

#####################OJOOOOO####################
#se podra mostrar la figura con los enlaces intercapa?

# La respuesta es si pero solo si se añaden los nodos y enlaces a mano
# si se hace de ese modo solo se podria cambiar el color con la funcion dibujar_capa
# pero como se crean las redes de forma directa, 
# graficamente no es posible mostrar los enlaces intercapa de forma correcta
# debido a que networkx esta diseñado para trabajar mas con redes mono capa
# igual que los algoritmos que usa por ejemplo para calular la centralidad de grado y cercania