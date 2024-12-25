from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

# Route to fetch the list of locations
@app.route("/getlocationnames", methods=['GET'])
def getlocationnames():
    response = jsonify({
        'locations': utils.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# Route to predict the home price based on given data
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimatedprice': utils.get_est_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

    

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    utils.load_saved_art()  # Loading necessary resources like the model
    print(app.url_map)
    app.run(debug=True)
