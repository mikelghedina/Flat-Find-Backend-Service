from .NewRepo import Repository as r
import statsmodels.api as sm
import json
import os

coefs = {}
def trainModels():
    dataframes = r.read_training_data()
    for df in dataframes: 
        X = df[1][['superficie', 'baños', 'habitaciones']]
        Y = df[1]['precio']

        X = sm.add_constant(X)
        est = sm.OLS(Y, X).fit()
        coefs[str(df[0])] = {
            "const": est.params[0], 
            "superficie":est.params[1],
            "baths":est.params[2],
            "habitaciones":est.params[3] 
        }

    save_path = 'flaskr\datos'
    file_name = "coefs.json"
    completeName = os.path.join(save_path, file_name)
    with open(completeName, 'w') as json_file:
        json.dump(coefs,json_file)

def get_coefs_by_district(districtName):
    coefsDict = r.read_trained_data()
    for district in coefsDict:
        if district == districtName:
            subDict = coefsDict[districtName]
    return subDict

def model_inference(coefsDict,surface,baths,habs):
    price = coefsDict['const'] + (surface * coefsDict['superficie']) + (baths * coefsDict['baths']) + (habs * coefsDict['habitaciones'])
    return price