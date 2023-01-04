import pandas as pd
import numpy as np
import scipy
bd = open("SUPERBOLITA-2017-2022.csv")
datos= pd.read_csv(bd, sep=".", header = None) 
#Se convierte la secuencia de datos a un array de numpy 
auxd=datos.to_numpy()
n = len(auxd) #Numero de observaciones

#Tabla de frecuencias
numero, frecuencia = np.unique(auxd, return_counts=True) #Cuenta la freecuencia de cada objeto
frecuencias = dict(zip(numero, frecuencia)) #Se comprimen las listas anteriores a un diccionario


#CHI CUADRADO
ei = n/16  #Frecuencia esperada
chi =((frecuencia-ei)**2)/ei #Se aplica la formula a cada observación
chisq = sum(chi) #Chi cuadrado
print("El estadístico de Prueba de chi-cuadrado es:", chisq)
#valor critico
Vchisq= scipy.stats.chi2.ppf(0.95,15)
print("El valor critico es :",Vchisq)