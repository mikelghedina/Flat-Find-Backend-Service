from flaskr.Repository.DistrictsRepository import sant_andreu_rents_repository as sarr
import pandas as pd
from scipy import stats
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def get_coef_from_training_sant_andreu():

    df_sant_andreu = sarr.read_csv_sant_andreu_training()

    scale = StandardScaler()
    X = df_sant_andreu[['superficie', 'baños', 'habitaciones']]
    Y = df_sant_andreu['precio']

    X[['superficie', 'baños', 'habitaciones']] = scale.fit_transform(X[['superficie', 'baños', 'habitaciones']].values)

    X = sm.add_constant(X)
    est = sm.OLS(Y, X).fit()
    params = []
    for param in est.params:
        params = params.append(param)

    return params