import NewService as s
from flask import Flask 

app = Flask(__name__)


coefsDict = s.get_coefs_by_district("Eixample")

#Dictionario de coeficientes, N de m2, N de Baños, N de habs
print(s.model_inference(coefsDict,sup,baths,rooms))

@app.route('/est/<int:sup>/<int:baths>/<int:rooms>')
def estimated_price(sup, baths, rooms):
    return s.model_inference(coefsDict,sup,baths,rooms)

