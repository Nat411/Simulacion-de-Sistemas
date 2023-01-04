import random as r
import numpy as np

n = [100, 1000,10000,100000,1000000] #Los diferentes nùmeros de casos de prueba que se van a realizar.
probabilidad_final = np.array([[100, 1000,10000,100000, 1000000]]) #Matriz que contendrá todas las probabilidades que resulten de las simulaciones.

#Para un mejor análisis, se repetirán las simulaciones varias veces
for k in range(50):
    probabilidad_k = [] #Acá se almacenará las probabilidades resultantes de la repetición número k
    for j in n:
        c = 0 #Creamos el número de casos de éxito
        for i in range(j):
            #Por cada simulación genero los puntos de quiebre aleatorios
            r1 = r.random() 
            r2 = r.random()

            a = min(r1,r2)
            b = max(r1,r2)
            #Se calculan las 3 particiones del palito
            l1 = a
            l2 = b-a
            l3 = 1-b
            
            #Se verifica que con los 3 pedazos oueda formar un triángulo
            if (l1+l2)>l3 and (l1+l3)>l2 and (l2+l3)>l1:
                c+=1 #Si si se puede formar el triángulo, incremento en 1 al contador de los casos de exito
                
        probabilidad=c/j #Se calcula la probabilidad
        probabilidad_k.append(probabilidad) #Se agrega a la lista de probabilidades
    probabilidad_final = np.append(probabilidad_final, [probabilidad_k], axis =0) #La lista de probabilidades de la tanda k, se agrega a la matriz final de probabilidades
probabilidad_final = np.delete(probabilidad_final, 0, axis = 0) #Se elimina el header inicial, ya que solo se usó como guía de las dimensiones de la matriz.
print(probabilidad_final) 

#Cálculos para poder realizar el análisis.
for m in range(5):
    #Se hace el calculo de minimo, maximo y el promedio de las probabilidades de cada columna ( de cuando se simula 100 veces, cuando se simla 1000 veces y así)
    minimo = min(probabilidad_final[:,m]) 
    maximo = max(probabilidad_final[:,m])
    promedio = sum(probabilidad_final[:,m])/50
    
    print(f"para {n[m]}: minimo: {minimo}, maximo: {maximo}, promedio: {promedio}, {round(promedio,2)}")
