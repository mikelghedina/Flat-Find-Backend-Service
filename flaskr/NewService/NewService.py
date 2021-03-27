from .NewRepo import Repository
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def get_coef_from_training():
    url = 'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquiler_ciutat_vella.csv'
    df_les_corts = Repository.read_csv_ciutat_vella_training(url)



    X = df_les_corts[['superficie', 'baños', 'habitaciones']]
    Y = df_les_corts['precio']

    X = sm.add_constant(X)
    est = sm.OLS(Y, X).fit()
    params = []
    for param in est.params:
        params.append(param)

    return params
