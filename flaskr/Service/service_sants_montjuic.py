from flaskr.Repository.DistrictsRepository import sants_montjuic_rents_repository as smrr
import pandas as pd
from scipy import stats
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def get_coef_from_training():

    df_sants_montjuic = smrr.read_csv_sants_montjuic_training()

    scale = StandardScaler()
    X = df_sants_montjuic[['superficie', 'baños', 'habitaciones']]
    Y = df_sants_montjuic['precio']

    X[['superficie', 'baños', 'habitaciones']] = scale.fit_transform(X[['superficie', 'baños', 'habitaciones']].values)

    X = sm.add_constant(X)
    est = sm.OLS(Y, X).fit()
    params = []
    for param in est.params:
        params = params.append(param)

    return params