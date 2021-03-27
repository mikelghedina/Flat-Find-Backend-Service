from flaskr.Repository.DistrictsRepository import nou_barris_rents_repository as nbrr
import pandas as pd
from scipy import stats
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def get_coef_from_training_nou_barris():

    df_nou_barris = nbrr.read_csv_nou_barris_training()

    scale = StandardScaler()
    X = df_nou_barris[['superficie', 'baños', 'habitaciones']]
    Y = df_nou_barris['precio']

    X[['superficie', 'baños', 'habitaciones']] = scale.fit_transform(X[['superficie', 'baños', 'habitaciones']].values)

    X = sm.add_constant(X)
    est = sm.OLS(Y, X).fit()
    params = []
    for param in est.params:
        params = params.append(param)

    return params
