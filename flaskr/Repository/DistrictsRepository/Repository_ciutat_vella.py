import pandas as pd
import json


def read_csv_average_training():
    df_ciutat_vella = pd.read_csv('../../datos/datasets_Pisos.com/alquiler_ciutat_vella.csv')
    return df_ciutat_vella


print(read_csv_average_training())


def create_csv_average_training(ciutat_vella_coef_data):
    with open('ciutat_vella_coef_data.json', 'w') as outfile:
        json.dump(ciutat_vella_coef_data, outfile, indent=4)

def read_csv_average_trained():
    with open('trained_average_rents.json') as file:
        trained_data_rents = json.load(file)

    return trained_data_rents
