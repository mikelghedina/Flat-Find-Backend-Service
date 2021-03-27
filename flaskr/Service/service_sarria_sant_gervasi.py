from flaskr.Repository.DistrictsRepository import sarria_sant_gervasi_rents_repository as ssgrr
import pandas as pd
from scipy import stats
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def get_coef_from_training_sarria_sant_gervasi():

    df_sarria_sant_gervasi = ssgrr.read_csv_sarria_sant_gervasi_training()

    scale = StandardScaler()
    X = df_sarria_sant_gervasi[['superficie', 'baños', 'habitaciones']]
    Y = df_sarria_sant_gervasi['precio']

    X[['superficie', 'baños', 'habitaciones']] = scale.fit_transform(X[['superficie', 'baños', 'habitaciones']].values)

    X = sm.add_constant(X)
    est = sm.OLS(Y, X).fit()
    params = []
    for param in est.params:
        params = params.append(param)

    return params