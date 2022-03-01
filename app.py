import json

from flask import Flask, jsonify ,request
from flask_restful import reqparse,Api,Resource

import requests
import googlemaps
gmaps = googlemaps.Client(key="AIzaSyAw2wtEBHUuMMik8_jq_TixPz9B5mD0Xws")



app = Flask(__name__)
api = Api(app)

@app.route('/findWaysPoints/<float:lat>/<float:lng>/<int:limite>',methods=['GET'])
def findWaysPoints(lat,lng,limite):
    response = requests.get("https://opendata.reseaux-energies.fr/api/records/1.0/search/?dataset=bornes-irve&q=&sort=-dist&facet=region&geofilter.distance="+str(lng)+"%2C"+str(lat)+"%2C"+str(limite))
    data = [response.json()["records"]] #[0]["fields"]["ylatitude"] , [0]["fields"]["xlongitude"]
    return jsonify(data)


if __name__ == '__main__':
    print("wollah ca marche")
    app.run(debug=True)