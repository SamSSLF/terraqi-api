from flask import Flask, jsonify, request
from functions import interp_inputs, get_windfc

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({'message': 'TerraQi API'})


@app.route('/windfc', methods=['POST'])
def get_fc():
    latitude = request.json['lat']
    longitude = request.json['lon']

    df = interp_inputs(latitude, longitude)
    result = get_windfc(df)

    return result


if __name__ == '__main__':
    app.run()
