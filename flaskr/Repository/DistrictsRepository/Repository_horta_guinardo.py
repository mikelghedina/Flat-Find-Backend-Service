def read_csv_average_training():
    df_horta_guinardo = pd.read_csv('../../datos/datasets_Pisos.com/alquiler_horta_guinardo.csv')
    return df_horta_guinardo


print(read_csv_average_training())


def create_csv_average_training(horta_guinardo_coef_data):
    with open('horta_guinardo_coef_data.json', 'w') as outfile:
        json.dump(horta_guinardo_coef_data, outfile, indent=4)


def read_csv_average_trained():
    with open('trained_average_rents.json') as file:
        trained_data_rents = json.load(file)

    return trained_data_rents