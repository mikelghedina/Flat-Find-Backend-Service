import pandas as pd
import json

def read_csv_sant_andreu_training():
    # ../../datos/datasets_Pisos.com/alquileres_sant_andreu.csv
    df_sant_andreu = pd.read_csv('https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquileres_sant_andreu.csv')
    return df_sant_andreu

print(read_csv_sant_andreu_training())

def create_csv_sant_andreu_training(sant_andreu_coef_data):
    with open('sant_andreu_coef_data.json', 'w') as outfile:
        json.dump(sant_andreu_coef_data, outfile, indent=4)

def read_csv_sant_andreu_trained():
    with open('trained_sant_andreu_rents.json') as file:
        trained_sant_andreu_rents = json.load(file)

    return trained_sant_andreu_rents