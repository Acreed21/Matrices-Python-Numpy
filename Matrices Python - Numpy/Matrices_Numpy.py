#Suma y Multiplicación de Matrices cuadradas para mirar el tiempo que dura cada operación
import numpy
from time import time
import matplotlib.pyplot as plt
promedios_Multi = [1,2,3,4,5,6,7,8,9,10]#,11,12,13,14,15,16,17,18,19,20]#Guardaremos los promedios acá
x = [1,2,3,4,5,6,7,8,9,10]
contador=0
for z in range(10,100,10):#Aumenta el tamaño de la matriz de 10 en 10 hasta 100
    print(z)
    tamaño_matrices = z
    tiempo_promedio_multi=0
    matriz1=numpy.zeros((tamaño_matrices,tamaño_matrices))#Se crean las matrices
    matriz2=numpy.zeros((tamaño_matrices,tamaño_matrices))#Se crean las matrices
    for i in range(tamaño_matrices):#Llena las filas
        for j in range(tamaño_matrices):#Llenas las columnas
            matriz1[i][j]=1
            matriz2[i][j]=2
    for f in range(10):#Ejecutará 10 veces el mismo problema
        #Operación de multiplicación
        matriz_Resultados_multi = numpy.zeros((tamaño_matrices,tamaño_matrices))#guardarán los resultados
        time1_multi = time()
        matriz_Resultados_multi=matriz1*matriz2
        time2_multi=time()
        tiempo_final_multi=(time2_multi-time1_multi)/(z*z*(2*z-1))
        tiempo_promedio_multi=tiempo_promedio_multi+tiempo_final_multi
    promedios_Multi[contador]=tiempo_promedio_multi/10
    contador=contador+1
    x[contador] = z
for i in range(len(promedios_Multi)):
    print(promedios_Multi[i])
promedios_Multi[contador]=tiempo_promedio_multi/10
plt.plot(x,promedios_Multi)
plt.show()