import pandas as pd
import json

def read_csv_average_training():
    df_nou_barris = pd.read_csv('../../datos/datasets_Pisos.com/alquiler_nou_barris.csv')
    return df_nou_barris


print(read_csv_average_training())


def create_csv_average_training(nou_barris_coef_data):
    with open('nou_barris_coef_data.json', 'w') as outfile:
        json.dump(nou_barris_coef_data, outfile, indent=4)


def read_csv_average_trained():
    with open('trained_average_rents.json') as file:
        trained_data_rents = json.load(file)

    return trained_data_rents