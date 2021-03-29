from flaskr import NewService as s
from flask import Flask, jsonify, request
import math
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# coefsDict = s.get_coefs_by_district("Eixample")

#Dictionario de coeficientes, N de m2, N de Baños, N de habs
# print(s.model_inference(coefsDict,sup,baths,rooms))fla

@app.route("/est/", methods=["GET", "POST"])
def estimated_price():
    district_name = request.args.get('district_name')
    sup = request.args.get('sup')
    baths = request.args.get('baths')
    rooms = request.args.get('rooms')
    price = s.model_inference(s.get_coefs_by_district(str(district_name)),float(sup),float(baths),float(rooms))
    return jsonify({"estimed price": round(price, 2)})


@app.route("/train", methods=["GET"])
def train():
    coefs = s.trainModels()
    return coefs

