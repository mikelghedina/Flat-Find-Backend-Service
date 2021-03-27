import pandas as pd
import json


def read_csv_ciutat_vella_training():
    # df_ciutat_vella = pd.read_csv('../../datos/datasets_Pisos.com/alquiler_ciutat_vella.csv')
    df_ciutat_vella = pd.read_csv('https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquiler_ciutat_vella.csv')
    return df_ciutat_vella


print(read_csv_ciutat_vella_training())


def create_csv_ciutat_vella_training(ciutat_vella_coef_data):
    with open('ciutat_vella_coef_data.json', 'w') as outfile:
        json.dump(ciutat_vella_coef_data, outfile, indent=4)

def read_csv_ciutat_vella_trained():
    with open('trained_ciutat_vella_rents.json') as file:
        trained_ciutat_vella_rents = json.load(file)

    return trained_ciutat_vella_rents
