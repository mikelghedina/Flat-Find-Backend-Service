import pandas as pd
import json

def read_csv_sant_marti_training():
    df_sant_marti = pd.read_csv('flaskr/datos/datasets_Pisos.com/alquileres_sant_marti.csv')
    return df_sant_marti

print(read_csv_sant_marti_training())

def create_csv_sant_marti_training(sant_marti_coef_data):
    with open('sant_marti_coef_data.json', 'w') as outfile:
        json.dump(sant_marti_coef_data, outfile, indent=4)

def read_csv_sant_marti_trained():
    with open('trained_sant_marti_rents.json') as file:
        trained_sant_marti_rents = json.load(file)

    return trained_sant_marti_rents