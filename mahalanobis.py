import numpy as np
import pandas as pd

#funcion para calcular la distancia de Mahalanobis entre dos vectores
def mahalanobis_distance(x, y, inv_cov_matrix):
    diff = x - y
    return np.sqrt(np.dot(np.dot(diff, inv_cov_matrix), diff.T))

# Leer datos del archivo CSV
datos_df = pd.read_csv('archivo.csv')  #recuerda que la idea es que los datos estén asi

#carac1_elemento_1  carac2_elemento_1   carac3_elemento_1  ... ... carac_m_elemento1
#carac1_elemento_2  carac2_elemento_2   carac3_elemento_2  ... ... carac_m_elemento2
#carac1_elemento_3  carac2_elemento_3   carac3_elemento_3  ... ... carac_m_elemento3
#...                         ...                ...                     ...
#...                         ...                ...                     ...
#carac1_elemento_n  carac2_elemento_n   carac3_elemento_n  ... ... carac_m_elementon

#extraemos las características y convertimos a matriz numpy
datos = datos_df.iloc[:, 1:].to_numpy()

#calculamos la matriz de covarianza
cov_matrix = np.cov(datos, rowvar=False)

#calculamos la matriz de covarianza regularizada
#para evitar problemas de singularidad o no invertibilidad cuando... esto es especialmente importante cuando el número de nodos (filas en tus datos) es menor que el número de características (columnas en tus datos).


reg_cov_matrix = cov_matrix + 0.01 * np.eye(cov_matrix.shape[0])

#calculamos la inversa de la matriz de covarianza regularizada
inv_cov_matrix = np.linalg.inv(reg_cov_matrix)

#calculamos el vector de medias
mean_vector = np.mean(datos, axis=0)

#calculamos las distancias de Mahalanobi
distancias = []
for i in range(datos.shape[0]):
    for j in range(i + 1, datos.shape[0]):
        dist = mahalanobis_distance(datos[i], datos[j], inv_cov_matrix)
        distancias.append(dist)
mediana = np.median(distancias)#calculamos la mediana

#creamos matriz de adyacencia
num_elementos = datos.shape[0]
matriz_adyacencia = np.zeros((num_elementos, num_elementos))

#ahora si, con base en la mediana calculamos los vínculos
for i in range(num_elementos):
    for j in range(i + 1, num_elementos):
        dist = mahalanobis_distance(datos[i], datos[j], inv_cov_matrix)
        if dist < mediana:
            matriz_adyacencia[i][j] = 1
            matriz_adyacencia[j][i] = 1

#guardamos la matriz de adyacencia en un archivo CSV
matriz_adyacencia_df = pd.DataFrame(matriz_adyacencia, index=range(1, num_elementos+1), columns=range(1, num_elementos+1))
matriz_adyacencia_df.to_csv('matriz_adyacencia.csv')
print("Terminé de forma correcta =)")