from flaskr.Repository.DistrictsRepository import horta_guinardo_rents_repository as hgrr
import pandas as pd
from scipy import stats
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def get_coef_from_training_horta_guinardo():

    df_horta_guinardo = hgrr.read_csv_horta_guinardo_training()

    scale = StandardScaler()
    X = df_horta_guinardo[['superficie', 'baños', 'habitaciones']]
    Y = df_horta_guinardo['precio']

    X[['superficie', 'baños', 'habitaciones']] = scale.fit_transform(X[['superficie', 'baños', 'habitaciones']].values)

    X = sm.add_constant(X)
    est = sm.OLS(Y, X).fit()
    params = []
    for param in est.params:
        params = params.append(param)

    return params
