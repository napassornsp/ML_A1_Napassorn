from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to load pickled models
def load_model(file_path):
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Failed to load model {file_path}: {e}")
        return None

loaded_scaler = load_model('./model/pk_scale.model')
loaded_model = load_model('./model/pk_selling_price.model')
default_value = load_model('./model/pk_default_value.model')
print(default_value)
# when user open first time
@app.route('/')
def index():
    return render_template('main.html')

# when user click 
@app.route('/receive_data', methods=['POST'])
def receive_data():
    # Retrieve values from the form inputs; provide default values if inputs are empty
    
    engine = request.form.get('engine', default_value['engine'])  # Default to median if not provided
    power = request.form.get('max_power', default_value['max_power'])  # Ensure this matches the 'name' attribute in the HTML
    year = request.form.get('year', default_value['year'])
    km_driven = request.form.get('km_driven', default_value['km_driven'])  # Default value if not provided
    mileage = request.form.get('mileage', default_value['mileage'])  # Default value if not provided
    # Replace empty strings with default values
    if not engine:
        engine = default_value['engine']
    if not power:
        power = default_value['max_power']
    if not year:
        year = default_value['year']
    if not km_driven:
        km_driven = default_value['km_driven']
    if not mileage:
        mileage = default_value['mileage']
    print(engine, power, year, km_driven, mileage)
    try:
        # Convert the input to floats for model prediction
        input_values = pd.DataFrame([{
            'year': float(year),
            'km_driven': float(km_driven),
            'mileage': float(mileage),
            'engine': float(engine),
            'max_power': float(power)
        }])

        if loaded_scaler and loaded_model:
            scaled_input = loaded_scaler.transform(input_values)
            predicted_price = loaded_model.predict(scaled_input)
            exp_price = np.exp(predicted_price)[0]  # Assuming model outputs log prices
            print(exp_price)

            return render_template('response.html',
                                   predicted_price=f"${exp_price:.2f}")

            # return f"Predicted Price: ${exp_price:.2f}"
        else:
            raise ValueError("Model or Scaler not loaded properly.")

    except Exception as e:
        print(f"Error during request processing: {e}")
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=600)
