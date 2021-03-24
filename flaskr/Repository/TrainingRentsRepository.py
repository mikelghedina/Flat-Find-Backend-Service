import pandas as pd
import json as js


def read_csv_rents_training():

    df = pd.read_csv('...')
    return df

def create_csv_rents_trained(data, file):

    with open('trained_data_rents.json', 'w') as file:
    json.dump(data, file, indent=4)


def read_csv_rents_trained():

    with open('trained_data_rents.json') as file:
    trained_data_rents = json.load(file)

    return trained_data_rents


