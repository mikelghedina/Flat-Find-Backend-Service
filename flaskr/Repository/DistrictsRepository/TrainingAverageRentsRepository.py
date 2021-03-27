import pandas as pd
import json


def read_csv_eixample_training():
    df_eixample = pd.read_csv('flaskr/datos/datasets_Pisos.com/alquiler_ciutat_vella.csv')
    return df_eixample


print(read_csv_eixample_training())


# def create_json_eixample_coef(eixample_coef_data):
#     with open('eixample_coef_data.json', 'w') as outfile:
#         json.dump(eixample_coef_data, outfile, indent=4)
#
# def read_csv_average_trained():
#     with open('trained_average_rents.json') as file:
#         trained_data_rents = json.load(file)
#
#     return trained_data_rents
