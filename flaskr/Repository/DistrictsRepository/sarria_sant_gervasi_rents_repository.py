import pandas as pd
import json

def read_csv_sarria_sant_gervasi_training():
    df_sarria_sant_gervasi = pd.read_csv('flaskr/datos/datasets_Pisos.com/Alquileres_sarria_sant_gervasi.csv')
    return df_sarria_sant_gervasi

print(read_csv_sarria_sant_gervasi_training())

def create_csv_sarria_sant_gervasi_training(sarria_sant_gervasi_coef_data):
    with open('sarria_sant_gervasi_coef_data.json', 'w') as outfile:
        json.dump(sarria_sant_gervasi_coef_data, outfile, indent=4)

def read_csv_sarria_sant_gervasi_trained():
    with open('trained_sarria_sant_gervasi.json') as file:
        trained_sarria_sant_gervasi = json.load(file)

    return trained_sarria_sant_gervasi