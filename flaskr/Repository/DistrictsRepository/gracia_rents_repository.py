import pandas as pd
import json

def read_csv_gracia_training():
    # df_gracia = pd.read_csv('../../datos/datasets_Pisos.com/alquiler_gracia.csv')
    df_gracia = pd.read_csv('flaskr/datos/datasets_Pisos.com/alquiler_gracia.csv')
    return df_gracia


print(read_csv_gracia_training())


def create_csv_gracia_training(gracia_coef_data):
    with open('gracia_coef_data.json', 'w') as outfile:
        json.dump(gracia_coef_data, outfile, indent=4)


def read_csv_gracia_trained():
    with open('trained_gracia_rents.json') as file:
        trained_gracia_rents = json.load(file)

    return trained_gracia_rents