
from flaskr.Repository.DistrictsRepository import TrainingAverageRentsRepository as tarr
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler


def get_coef_from_training():

    df_eixample = tarr.read_csv_eixample_training()

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

print(get_coef_from_training())

def get_prediction_from_trained(sup, baths, rooms):
    params = tarr.read_csv_average_trained()

    prediction = params[0]
