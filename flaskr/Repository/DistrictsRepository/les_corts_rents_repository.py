import pandas as pd
import json


def read_csv_les_corts_training():
    # ../../ datos / datasets_Pisos.com / Alquileres_les_corts.csv
    df_les_corts = pd.read_csv(
        'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/Alquileres_les_corts.csv')

    return df_les_corts
# print(read_csv_les_corts_training())

def create_csv_les_corts_training(les_corts_coef_data):
    with open('les_corts_coef_data.json', 'w') as outfile:
        json.dump(les_corts_coef_data, outfile, indent=4)


def read_csv_les_corts_trained():
    with open('trained_les_corts_rents.json') as file:
        trained_les_corts_rents = json.load(file)

    return trained_les_corts_rents
