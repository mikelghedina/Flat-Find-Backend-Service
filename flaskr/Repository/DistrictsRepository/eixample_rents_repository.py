import pandas as pd
import json

def read_csv_eixample_training():
    # df_eixample = pd.read_csv('../../datos/datasets_Pisos.com/alquiler_eixample.csv')
    df_eixample = pd.read_csv('flaskr/datos/datasets_Pisos.com/alquiler_eixample.csv')
    return df_eixample


print(read_csv_eixample_training())


def create_csv_eixample_training(eixample_coef_data):
    with open('eixample_coef_data.json', 'w') as outfile:
        json.dump(eixample_coef_data, outfile, indent=4)


def read_csv_eixample_trained():
    with open('trained_eixample_rents.json') as file:
        trained_eixample_rents = json.load(file)

    return trained_eixample_rents