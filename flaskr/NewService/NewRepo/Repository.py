import pandas as pd


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
        df = pd.read_csv(url)
        data = (name,df)
        dataframes.append(data)
    return dataframes


def read_csv_eixample_trained():
    with open('trained_eixample_rents.json') as file:
        trained_eixample_rents = json.load(file)

    return trained_eixample_rents