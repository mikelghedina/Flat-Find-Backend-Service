import pandas as pd
import json

def read_csv_nou_barris_training():
    df_nou_barris = pd.read_csv('flaskr/datos/datasets_Pisos.com/alquiler_nou_barris.csv')
    return df_nou_barris


print(read_csv_nou_barris_training())


def create_csv_nou_barris_training(nou_barris_coef_data):
    with open('nou_barris_coef_data.json', 'w') as outfile:
        json.dump(nou_barris_coef_data, outfile, indent=4)


def read_csv_nou_barris_trained():
    with open('trained_nou_barris_rents.json') as file:
        trained_nou_barris_rents = json.load(file)

    return trained_nou_barris_rents