from flaskr.Repository.DistrictsRepository import les_corts_rents_repository
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def get_coef_from_training():

    df_les_corts = les_corts_rents_repository.read_csv_les_corts_training()

    scale = StandardScaler()

    X = df_les_corts[['superficie', 'baños', 'habitaciones']]
    Y = df_les_corts['precio']

    X[['superficie', 'baños', 'habitaciones']] = scale.fit_transform(X[['superficie', 'baños', 'habitaciones']].values)

    X = sm.add_constant(X)
    est = sm.OLS(Y, X).fit()
    params = []
    for param in est.params:
        params = params.append(param)

    return params


