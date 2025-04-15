import networkx as nx
import matplotlib.pyplot as plt
# Graph usa una red no dirigida
# DiGraph usa red dirigida
# MultiGraph permite multiples enlaces no dirigidos entre pares de nodos
# Tambien existe multinetx pero es mas dificil de instalar


redNoDirigida= nx.Graph()

redNoDirigida.add_node("1")
redNoDirigida.add_node("1234")

redNoDirigida.add_nodes_from(["2","3"])
redNoDirigida.add_nodes_from("5678")
redNoDirigida.add_nodes_from("12349")

redNoDirigida.add_edge(1,2) # asi se generan 2 nodos nuevos
redNoDirigida.add_edge("1","2")

print("Los nodos son: ", redNoDirigida.nodes)
print("Los enlaces son: ", redNoDirigida.edges)
print("Lista de adyacencia: ",redNoDirigida.adj)
print("El grado es:", redNoDirigida.degree("1")) # el grado del nodo 1

