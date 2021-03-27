import pandas as pd
import json

def read_csv_sants_montjuic_training():
    # ../../datos/datasets_Pisos.com/alquileres_sants_montjuic.csv
    df_sants_montjuic = pd.read_csv('https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquileres_sants_montjuic.csv')
    return df_sants_montjuic

print(read_csv_sants_montjuic_training())

def create_csv_sants_montjuic_training(sants_montjuic_coef_data):
    with open('sants_montjuic_coef_data.json', 'w') as outfile:
        json.dump(sants_montjuic_coef_data, outfile, indent=4)

def read_csv_sants_montjuic_trained():
    with open('trained_sants_montjuic_rents.json') as file:
        trained_sants_montjuic_rents = json.load(file)

    return trained_sants_montjuic_rents