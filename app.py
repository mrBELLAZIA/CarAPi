import json

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

import requests

app = Flask(__name__)
api = Api(app)


class findWaysPoints(Resource):
    def get(self):
        lat = float(request.args.get('lat'))
        lng = float(request.args.get('lng'))
        limite = int(request.args.get('limite'))
        response = requests.get(
            "https://opendata.reseaux-energies.fr/api/records/1.0/search/?dataset=bornes-irve&q=&sort=-dist&facet=region&geofilter.distance=" + str(
                lng) + "%2C" + str(lat) + "%2C" + str(limite))
        data = [response.json()["records"]]  # [0]["fields"]["ylatitude"] , [0]["fields"]["xlongitude"]
        return jsonify(data)


api.add_resource(findWaysPoints, '/findWaysPoints')

if __name__ == '__main__':
    print("wollah ca marche")
    app.run(debug=True)
