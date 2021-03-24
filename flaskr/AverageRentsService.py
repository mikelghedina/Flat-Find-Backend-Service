import TrainingRentsRepository as trs

def read_csv():
    return trs.read_csv_rents_training()


print(read_csv())