import pandas as pd
import json


def read_csv_average_training():
    df = df = pd.read_csv('./datos/pisos_barcelona (1).csv')
    return df


def create_csv_average_training(data, file):
    with open('trained_average_rents.json', 'w') as file:
        json.dump(data, file, indent=4)


def read_csv_average_trained():
    with open('trained_average_rents.json') as file:
        trained_data_rents = json.load(file)

    return trained_data_rents
