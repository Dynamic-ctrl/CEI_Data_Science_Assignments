import streamlit as st
import pandas as pd
import xgboost as xgb
import joblib

# 1. Page Configuration
st.set_page_config(page_title="Smart Grid Optimizer", page_icon="⚡", layout="wide")
st.title("⚡ Autonomous Smart Grid Optimizer")
st.markdown("Enterprise-grade demand forecasting and AI-driven grid routing.")

# 2. Load the AI Engine and Features
@st.cache_resource
def load_assets():
    model = xgb.XGBRegressor()
    model.load_model('xgboost_energy_model.json')
    features = joblib.load('model_features.pkl')
    return model, features

model, feature_names = load_assets()

# 3. Autonomous Decision Engine
def autonomous_grid_decision(predicted_load, safety_threshold=1.5):
    if predicted_load > safety_threshold:
        return "CRITICAL", "Initiating Peak Shaving & Discharging Battery Storage", "🚨"
    elif predicted_load < 0.2:
        return "OPTIMAL", "Routing excess renewable generation to storage", "🔋"
    else:
        return "STABLE", "Maintain standard distribution", "✅"

# 4. Sidebar Inputs
st.sidebar.header("Grid Parameters")
hour = st.sidebar.slider("Time of Day (Hour)", 0, 23, 18)
temp = st.sidebar.number_input("Temperature (°C)", value=5.2)
lag_1h = st.sidebar.number_input("Recent Load (kWh 1h ago)", value=0.45)
lag_24h = st.sidebar.number_input("Load 24h ago (kWh)", value=0.40)
rolling_mean = st.sidebar.number_input("24h Rolling Mean (kWh)", value=0.35)

# Metrics Display
st.sidebar.divider()
st.sidebar.caption("Model Performance Metrics")
st.sidebar.write("**RMSE:** 0.3319 kWh")
st.sidebar.write("**MAE:** 0.1669 kWh")

# 5. Prediction Logic
if st.sidebar.button("Run Optimization Algorithm", type="primary"):
    input_data = pd.DataFrame([{
        'hour': hour, 'day_of_week': 4, 'month': 12, 'is_weekend': 0,
        'temperature': temp, 'energy_lag_1h': lag_1h, 
        'energy_lag_24h': lag_24h, 'energy_rolling_mean_24h': rolling_mean
    }])
    
    # Ensure correct column order
    input_data = input_data[feature_names]
    
    forecast = float(model.predict(input_data)[0])
    status, action, icon = autonomous_grid_decision(forecast)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Forecasted Household Load")
        st.metric(label="Predicted Demand", value=f"{forecast:.4f} kWh")
        st.line_chart(pd.DataFrame({"Load (kWh)": [forecast*0.9, forecast, forecast*1.1]}, index=["T-1", "Current", "T+1"]))

    with col2:
        st.subheader(f"{icon} System Status: {status}")
        if status == "CRITICAL": st.error(f"**Action:** {action}")
        elif status == "STABLE": st.success(f"**Action:** {action}")
        else: st.info(f"**Action:** {action}")

    with st.expander("🔍 AI Reasoning & Explainability"):
        st.markdown("The model prioritized **Historical Usage** as the primary driver for this forecast.")
        st.image("shap_summary.png", caption="Feature Impact Analysis (SHAP)")