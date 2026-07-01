from flask import Flask, request, jsonify
import xgboost as xgb
import pandas as pd
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

# 1. Load the pre-trained AI Engine
model = xgb.XGBRegressor()
model.load_model('xgboost_energy_model.json')

# 2. The Autonomous Decision Engine
def autonomous_grid_decision(predicted_load, safety_threshold=1.5):
    if predicted_load > safety_threshold:
        return {"status": "CRITICAL", "action": "Initiating Peak Shaving & Discharging Battery Storage"}
    elif predicted_load < 0.2:
        return {"status": "OPTIMAL", "action": "Routing excess renewable generation to storage"}
    else:
        return {"status": "STABLE", "action": "Maintain standard distribution"}

# 3. Create the API Endpoint
@app.route('/api/predict', methods=['POST'])
def predict_demand():
    try:
        # Get the real-time data from the request (e.g., from your React dashboard)
        data = request.get_json()
        
        # Convert the incoming JSON into a DataFrame
        # Expected features: ['hour', 'day_of_week', 'month', 'is_weekend', 'temperature', 'energy_lag_1h', 'energy_lag_24h', 'energy_rolling_mean_24h']
        input_features = pd.DataFrame([data])
        
        # Ask the AI for a forecast
        forecast = float(model.predict(input_features)[0])
        
        # Pass the forecast to the autonomous logic
        decision = autonomous_grid_decision(forecast)
        
        # Return the insights as a JSON response
        return jsonify({
            "forecasted_kwh": round(forecast, 4),
            "grid_status": decision['status'],
            "autonomous_action": decision['action']
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    print("Starting Autonomous Energy Optimization API...")
    app.run(debug=True, port=5000)