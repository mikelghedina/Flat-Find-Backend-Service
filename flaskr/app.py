import NewService as s
import Flask 

app = Flask(__name__)


coefsDict = s.get_coefs_by_district("Eixample")

#Dictionario de coeficientes, N de m2, N de Baños, N de habs
estimated_price = 
print(estimated_price)

@app.route('/est/<int:sup>/<int:baths>/<int:rooms>')
def estimated_price(sup, baths, rooms):
    return s.model_inference(coefsDict,sup,baths,rooms)

