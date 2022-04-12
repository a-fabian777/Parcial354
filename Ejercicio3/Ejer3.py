# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:21:41 2022

@author: HP
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


"""
3. Del dataset anterior realice en PYTHON, 
tres algoritmos de preprocesamiento.
"""

#usando los datos de tests_done del dataset

dfcovid = pd.read_csv('dataCOVID19.csv')

df2 = dfcovid[['new_cases','tests_done','population','testing_rate','positivity_rate']]
df2['new_cases'] = dfcovid['new_cases'].map(float)
df2['positivity_rate'] = dfcovid['positivity_rate'].map(float)



# ----------primer algoritmo, completando valores faltantes
prepro = SimpleImputer(missing_values = np.nan, strategy = "mean")
x = df2.iloc[:100, 1:12]

x2 = prepro.fit_transform(x)


#----------segundo algoritmo, discretizacion
#usando el array anterior x
prepro = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')
y2=prepro.fit_transform(x)



#----------tercer algoritmo, label encoder para el nombre de pais y numero de pruebas realizadas
#'country', 'postivity_rate'
df3 = dfcovid[['country', 'tests_done']]

#paises en total
#setx = set(df3['country'])

encoder = OneHotEncoder(categories=[0])
df3 = encoder.fit_transform(df3).toarray()


