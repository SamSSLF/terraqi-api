from flask import Flask, jsonify, request, abort
from functions import interp_inputs, get_windfc, is_outside_uk, get_daily_windfc

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({'message': 'Welcome to TerraQi API'})


@app.route('/windfc', methods=['POST'])
def get_fc():
    latitude = request.json['lat']
    longitude = request.json['lon']

    if is_outside_uk(latitude, longitude):
        abort(400, "Queried coordinates are beyond the geographical scope of this dataset.")

    df = interp_inputs(latitude, longitude)
    result = get_windfc(df).to_json()

    return result


@app.route('/windfc/daily', methods=['POST'])
def get_daily_fc():
    latitude = request.json['lat']
    longitude = request.json['lon']

    if is_outside_uk(latitude, longitude):
        abort(400, "Queried coordinates are beyond the geographical scope of this dataset.")

    df = interp_inputs(latitude, longitude)
    df = get_windfc(df)
    result = get_daily_windfc(df).to_json(orient='index')

    return result


if __name__ == '__main__':
    app.run()
