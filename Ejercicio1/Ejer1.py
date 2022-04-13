# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


    
def cuartil(k, n, ls):
    if n%2 != 0:
        return ls[int(k*(n-1)/4)]
    else:
        return (ls[int(n/2)-1]+ls[int(n/2)])/2;
    
dfcovid = pd.read_csv('dataCOVID19.csv')
columnas = list(dfcovid.columns)
dfcovid.describe
#numeros = [n for n in columnas if type(n) != str]
col_num = ['new_cases','tests_done','population','testing_rate','positivity_rate']
num_reg = len(dfcovid.index)

"""
1. Seleccione un dataset del area medica o de abogacia 
    (datos tabulares). Realice lo siguiente:

   a. El calculo del 1er cuartil de datos, 
   el percentil 50 por columna; 
   explique qué significa en cada caso mediante Python sin uso de librerías
"""

#creando lista con las columnas de datos numericos
lista_reg=[]
lista_reg.append(sorted(list(dfcovid['new_cases'])))
lista_reg.append(sorted(list(dfcovid['tests_done'])))
lista_reg.append(sorted(list(dfcovid['population'])))
lista_reg.append(sorted(list(dfcovid['testing_rate'])))
lista_reg.append(sorted(list(dfcovid['positivity_rate'])))

#convirtiendo a float las columnas que son string
copia_reg = []
for i in lista_reg:
    copia_reg.append(list(map(float, i)))


for k in range(1,3):    
    print("\n---cuartil ", k)
    for reg in copia_reg:
        print(cuartil(k, num_reg, reg))



#   b. Realice lo mismo del inciso (a) con el uso de numpy y pandas

for k in [25, 50]:
    print('\n----percentil: ', k)
    for reg in copia_reg:
        print(np.percentile(reg, k))

#dfcovid['new_cases'].mean()

#con pandas
print('cuartil 1')
print(dfcovid.quantile(0.25))
print('percentil 50')
print(dfcovid.quantile(0.5))



#   c. Grafique los datos y explique su comportamiento (PYTHON)
