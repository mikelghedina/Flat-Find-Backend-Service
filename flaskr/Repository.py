import pandas as pd
import json
import os

UrlDictionari = {
    "Ciutat Vella" : 'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquiler_ciutat_vella.csv',
    "Eixample" : 'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquiler_eixample.csv',
    "Gracia" : 'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquiler_gracia.csv',
    "Horta" : 'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquiler_horta_guinardo.csv',
    "Les Corts" : 'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/Alquileres_les_corts.csv',
    "Nou Barris" : 'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquiler_nou_barris.csv',
    "Sant Andreu" : 'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquileres_sant_andreu.csv',
    "Sant Marti" : 'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquileres_sant_marti.csv',
    "Sants Montjuic" : 'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/alquileres_sants_montjuic.csv',
    "Sarria" :'https://raw.githubusercontent.com/mikelghedina/Flat-Find-Backend-Service/master/flaskr/datos/datasets_Pisos.com/Alquileres_sarria_sant_gervasi.csv'
}
def read_training_data():
    dataframes = []
    for name,url in UrlDictionari.items():
        print(url)
        df = pd.read_csv(url)
        data = (name,df)
        dataframes.append(data)
    return dataframes

read_training_data()

def read_trained_data():
    trained_data = {}
    save_path = 'flaskr\datos'
    file_name = "coefs.json"
    completeName = os.path.join(save_path, file_name)
    with open(completeName) as json_file:
        trained_data = json.load(json_file)
    return trained_data

