from flaskr.Repository.DistrictsRepository import ciutat_vella_rents_repository as cvrr
import pandas as pd
from scipy import stats
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def get_coef_from_training_ciutat_vella():

    df_ciutat_vella = cvrr.read_csv_ciutat_vella_training()

    scale = StandardScaler()
    X = df_ciutat_vella[['superficie', 'baños', 'habitaciones']]
    Y = df_ciutat_vella['precio']

    X[['superficie', 'baños', 'habitaciones']] = scale.fit_transform(X[['superficie', 'baños', 'habitaciones']].values)

    X = sm.add_constant(X)
    est = sm.OLS(Y, X).fit()
    params = []
    for param in est.params:
        params = params.append(param)

    return params
