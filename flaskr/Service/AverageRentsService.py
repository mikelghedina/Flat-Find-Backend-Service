from flaskr.Repository.DistrictsRepository import TrainingAverageRentsRepository as tarr


def read_csv():
    return tarr.read_csv_rents_training()


print(read_csv())
