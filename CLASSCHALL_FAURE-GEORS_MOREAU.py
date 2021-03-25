# -*- coding: utf-8 -*-
"""
@author: Faure-Geors H
"""

import math
import pandas
from pandas import read_csv
data = "data.csv"
dataset = read_csv(data,sep = ";")
array = dataset.values
a = array[:,0]
b = array[:,1]
c = array[:,2]
d = array[:,3]
typeplante = array[:,4]

dataf = "finalTest.csv"
datasetf = read_csv(dataf,sep = ";")
arrayf = datasetf.values

af = arrayf[:,0]
bf = arrayf[:,1]
cf = arrayf[:,2]
df = arrayf[:,3]




        
def distance(a1,b1,c1,d1,a2,b2,c2,d2):
    somme = 0
    somme = math.pow((a2-a1),2) + math.pow((b2-b1),2) + math.pow((c2-c1),2) + math.pow((d2-d1),2)
    return(math.sqrt(somme))


def lesKplusProchesVoisins(aa,ba,ca,da, k):
  listeDesDistances = []
  for i in range(len(a)-1):
    listeDesDistances.append(distance (a[i],b[i],c[i],d[i],aa,ba,ca,da)) 

  
  Kppv = []
  for i in range(k):
    p=float('inf')
    for j in range (len(a)-1):
      if listeDesDistances[j] != 0 and listeDesDistances[j] < p and j not in Kppv:
        p = listeDesDistances[j]
        indice = j
    Kppv.append(indice)
  return(Kppv)



def  classefreq(Kppv):
      typep = ['A', 'B', 'C','D','E','F','G','H','I','J']
      decomptes = [0, 0, 0,0,0,0,0,0,0,0]
      for exemple in Kppv :
        for i in range(10):
          if typeplante[exemple] == typep[i]:
 
            decomptes [i] += 1
      plusGrandDecompte = decomptes [0]
      indice = 0
      for i in range(10):
        if decomptes [i] > plusGrandDecompte:
          plusGrandDecompte = decomptes [i]
          indice = i
      return(typep[indice])
 
    
if __name__=='__main__':

    nomfichier = "label.txt"
    fichier = open(nomfichier,"w")
    count = 0
    print(bf[0])

    for i in range(len(af)):
        kppv = lesKplusProchesVoisins(af[i],bf[i],cf[i],df[i],30)
        fichier.write(classefreq(kppv))
        fichier.write("\n")
    fichier.close
    
    
    
    
    
        
    