import pandas as pd
import json

def read_csv_horta_guinardo_training():
    # df_horta_guinardo = pd.read_csv('../../datos/datasets_Pisos.com/alquiler_horta_guinardo.csv')
    df_horta_guinardo = pd.read_csv('flaskr/datos/datasets_Pisos.com/alquiler_horta_guinardo.csv')
    return df_horta_guinardo


print(read_csv_horta_guinardo_training())


def create_csv_horta_guinardo_training(horta_guinardo_coef_data):
    with open('horta_guinardo_coef_data.json', 'w') as outfile:
        json.dump(horta_guinardo_coef_data, outfile, indent=4)


def read_csv_horta_guinardo_trained():
    with open('trained_horta_guinardo_rents.json') as file:
        trained_horta_guinardo_rents = json.load(file)

    return trained_horta_guinardo_rents