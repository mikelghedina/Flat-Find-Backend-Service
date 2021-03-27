from flaskr.Repository.DistrictsRepository import eixample_rents_repository as err
import pandas as pd
from scipy import stats
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def get_coef_from_training_eixample():

    df_eixample = err.read_csv_eixample_training()

    scale = StandardScaler()
    X = df_eixample[['superficie', 'baños', 'habitaciones']]
    Y = df_eixample['precio']

    X[['superficie', 'baños', 'habitaciones']] = scale.fit_transform(X[['superficie', 'baños', 'habitaciones']].values)

    X = sm.add_constant(X)
    est = sm.OLS(Y, X).fit()
    params = []
    for param in est.params:
        params = params.append(param)

    return params
