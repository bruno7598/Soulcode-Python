import numpy as np
import time
import datetime
# Creating 5x4 array
"""array1 = np.arange(1000)
array2 = np.arange(1000)

tempo_inicial = time.time()

for i in array1:
    for j in array2:
        print(i+j)

tempo_final = time.time()

resultado = tempo_final - tempo_inicial
print(round(resultado, 2))"""
        
time1 = datetime.datetime.now()      

lista1 = list(range(1, 1000)) 
lista2 = list(range(1, 1000)) 


for i in range(len(lista1)):
    for j in range(len(lista2)):
        print(i+j)
        
time = datetime.datetime.now()
print(time-time1)