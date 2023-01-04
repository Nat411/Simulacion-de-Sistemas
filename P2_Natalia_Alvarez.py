import random 
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def rueda1(): #Se crea una funcion que simula la primera rueda
  r = random.random()
  if r<=2/22:
    res = 2
  elif r<=4/22:
    res = 2
  elif r<= 9/22:
    res = 3
  elif r <= 19/22:
    res = 4
  elif r <= 21/22:
    res = 5
  else:
    res = 6
  return res

def rueda2(): #Se crea una funcion que simula la segunda rueda
  r = random.random()
  if r<=5/22:
    res = 1
  elif r<=8/22:
    res = 2
  elif r<= 9/22:
    res = 3
  elif r <= 11/22:
    res = 4
  elif r <= 21/22:
    res = 5
  else:
    res = 6
  return res

def rueda3(): #Se crea una funcion que simula la tercera rueda
  r = random.random()
  if r<=2/22:
    res = 1
  elif r<=9/22:
    res = 2
  elif r<= 19/22:
    res = 3
  elif r <= 20/22:
    res = 4
  elif r <= 21/22:
    res = 5
  else:
    res = 6
  return res

N = int(input("ingrese el número de lanzamientos \n")) #Numero de juegos
pruebas = [] #Se almacena el numero de resultados

for i in range(N):
  d = 0 #dinero
  r = [] #Lista que guarda los resultados
  d -=1 #Cada jueo cuesta $1
  r.append(rueda1()) #Gira rueda 1
  r.append(rueda2()) #Gira rueda 2
  r.append(rueda3()) #Gira rueda 3

  if r[0] == 1 and r.count(1)==1: #Cereza izquierda
    d+=2
  if r[2] == 1 and r.count(1)==1: #Cereza derecha
    d+=2
  if r.count(1)==2: #Dos cerezas
    d+=5
  if r.count(1) ==3: #Tres cerezas
    d+=20
  if r.count(2)==3: #tres naranjas
    d+= 20
  if r[0]==2 and r[1]==2 and r[2]==5 or r[0]==5 and r[1]==2 and r[2]==2: #Naranja naranja barra o Barra naranja naranja
    d+= 10
  if r.count(3) == 3: #Tres ciruelas
    d +=20
  if r[0]==3 and r[1]==3 and r[2]==5 or r[0]==5 and r[1]==3 and r[2]==3: #Ciruela ciruela barra o Ciruela ciruela barra
    d +=14
  if r.count(4) == 3: #Tres campanas
    d +=20
  if r[0]==4 and r[1]==4 and r[2]==5 or r[0]==5 and r[1]==4 and r[2]==4: #Campana campana barra o Barra campana campana
    d +=18
  if r.count(5) == 3: #Tres Barras
    d +=50
  if r.count(6) ==3: #Tres 7's
    d +=100
  
  pruebas.append(d) #El resultado se agrega a las pruebas

#Creación del Intervalo confianza
prom = 1/N*sum(pruebas) #Promedio
sd = np.std(pruebas) #Desviación estandar
I = 1.960*sd/(sqrt(N)) #Mitad del intervalo
der = prom + I #Extremo derecho
izq = prom - I #Extremo izquierdo
print(prom,sd)

print(izq, der)
plt.hist(pruebas)
plt.xlim(-1, 100)
plt.show()
