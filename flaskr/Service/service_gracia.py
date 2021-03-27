from flaskr.Repository.DistrictsRepository import gracia_rents_repository as grr
import pandas as pd
from scipy import stats
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def get_coef_from_training_gracia():

    df_gracia = grr.read_csv_gracia_training()

    scale = StandardScaler()
    X = df_gracia[['superficie', 'baños', 'habitaciones']]
    Y = df_gracia['precio']

    X[['superficie', 'baños', 'habitaciones']] = scale.fit_transform(X[['superficie', 'baños', 'habitaciones']].values)

    X = sm.add_constant(X)
    est = sm.OLS(Y, X).fit()
    params = []
    for param in est.params:
        params = params.append(param)

    return params
