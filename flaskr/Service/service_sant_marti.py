from flaskr.Repository.DistrictsRepository import sant_marti_rents_repository as smarr
import pandas as pd
from scipy import stats
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def get_coef_from_training():

    df_sant_marti = smarr.read_csv_sant_marti_training()

    scale = StandardScaler()
    X = df_sant_marti[['superficie', 'baños', 'habitaciones']]
    Y = df_sant_marti['precio']

    X[['superficie', 'baños', 'habitaciones']] = scale.fit_transform(X[['superficie', 'baños', 'habitaciones']].values)

    X = sm.add_constant(X)
    est = sm.OLS(Y, X).fit()
    params = []
    for param in est.params:
        params = params.append(param)

    return params
