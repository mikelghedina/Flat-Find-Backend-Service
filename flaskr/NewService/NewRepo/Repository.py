import pandas as pd
import json


def read_csv_ciutat_vella_training(url):
    # df_ciutat_vella = pd.read_csv('../../datos/datasets_Pisos.com/alquiler_ciutat_vella.csv')
    df_ciutat_vella = pd.read_csv(url)
    return df_ciutat_vella


def read_csv_eixample_trained():
    with open('trained_eixample_rents.json') as file:
        trained_eixample_rents = json.load(file)

    return trained_eixample_rents