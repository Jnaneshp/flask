from flask import Flask, render_template, request, jsonify
import requests
from models.health_prediction_model import predict_health_risks

app = Flask(__name__)

def get_weather_data(city):
    api_key = 'your_api_key'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    city = request.form['city']
    weather_data = get_weather_data(city)
    health_risks = predict_health_risks(weather_data)
    return jsonify(health_risks)

if __name__ == '__main__':
    app.run(debug=True)
