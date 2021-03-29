from flaskr import NewService as s
from flask import Flask, jsonify
import math

app = Flask(__name__)


# coefsDict = s.get_coefs_by_district("Eixample")

#Dictionario de coeficientes, N de m2, N de Baños, N de habs
# print(s.model_inference(coefsDict,sup,baths,rooms))

@app.route("/est/<string:district_name>-<int:sup>-<int:baths>-<int:rooms>", methods=["GET"])
def estimated_price(district_name,sup,baths,rooms):
    price = s.model_inference(s.get_coefs_by_district(district_name),sup,baths,rooms)
    return jsonify({"estimed price": round(price, 2)})


@app.route("/train", methods=["GET"])
def train():
    coefs = s.trainModels()
    return coefs

