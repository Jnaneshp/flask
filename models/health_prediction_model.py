# Placeholder for actual machine learning model
def predict_health_risks(weather_data):
    # Extract necessary weather data
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    air_quality = weather_data.get('air_quality', 'unknown')  # Assuming you have this data

    # Example prediction logic (replace with actual model)
    risks = {
        "asthma": "Low" if humidity < 50 else "High",
        "allergies": "Moderate" if air_quality == 'poor' else "Low",
        "heat_stroke": "High" if temperature > 30 else "Low"
    }
    
    return risks
