# app.py
from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the dataset
df = pd.read_csv('data/crime_data.csv')

# Route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Utility to filter options
@app.route('/get_cities', methods=['POST'])
def get_cities():
    state = request.json['state']
    cities = sorted(df[df['State'] == state]['City'].unique().tolist())
    return jsonify(cities)

# Predict crime rate for next 3 years
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    state = data['state']
    city = data['city']
    crime = data['crime']

    city_df = df[(df['State'] == state) & (df['City'] == city)]
    X = city_df[['Year']]
    y = city_df[crime]

    if len(X) < 2:
        return jsonify({"error": "Not enough data to train model."})

    model = LinearRegression()
    model.fit(X, y)

    future_years = [[2025], [2026], [2027]]
    preds = model.predict(future_years)
    preds = [round(p, 2) for p in preds]

    avg_crime = sum(y) / len(y)
    latest_pred = preds[-1]
    status = "Safe" if latest_pred < avg_crime else "Unsafe"

    return jsonify({
        "predictions": preds,
        "years": [2025, 2026, 2027],
        "status": status
    })

if __name__ == '__main__':
    app.run(debug=True)
