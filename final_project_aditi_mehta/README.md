# ⚡ Autonomous Energy Optimization Platform for Smart Grids

## 🚀 Project Overview
This project delivers an **AI-powered energy analytics system** designed to modernize smart grid operations. By integrating high-resolution smart meter data with real-time environmental context, the platform provides autonomous, actionable insights that enable smarter energy management, peak-load reduction, and grid stability.

## 🎯 What This App Does
* **Predictive Analytics:** Employs machine learning to forecast household energy consumption with high precision.
* **Autonomous Decisioning:** Integrates a decision engine that maps forecasted load to autonomous grid actions (e.g., peak shaving, battery routing).
* **Explainable AI (XAI):** Uses SHAP analysis to provide real-time reasoning for every AI-driven insight, ensuring transparency for grid operators.
* **Optimization Insights:** Identifies usage patterns across diverse demographic groups to facilitate efficient energy distribution.

## 🎥 System Demo
Watch a short demonstration of the platform functionality here: https://youtu.be/sfbyIz3iAYE

## 🛠 Tech Stack
* **Language:** Python 3.10
* **Machine Learning:** XGBoost (Gradient Boosting Regressor)
* **Deployment/UI:** Streamlit
* **Middleware:** Flask (API)
* **Explainability:** SHAP (SHapley Additive exPlanations)
* **Version Control:** Git & GitHub

## 🧠 Why This Approach?
| Technology | Justification |
| :--- | :--- |
| **XGBoost** | Superior performance for structured time-series data and excellent handling of non-linear relationships. |
| **Streamlit** | Enables rapid, iterative development of interactive dashboards for data-driven storytelling. |
| **SHAP** | Essential for critical infrastructure (Smart Grids) to move from "Black Box" models to transparent, trustable AI. |

## 📊 Performance Metrics
The model was validated using a robust testing set derived from the London Smart Meter dataset:
* **RMSE (Root Mean Squared Error):** 0.3319 kWh
* **MAE (Mean Absolute Error):** 0.1669 kWh

## ⚙️ How to Deploy & Run
### 1. Training (The Lab)
The entire data ingestion, feature engineering, and model training workflow is documented in:
`final_project_aditi_mehta.ipynb`

### 2. Setup Dependencies
Install all required libraries before running the app:
```bash
pip install -r requirements.txt
```
### 3. Backend (The API)
To start the Flask middleware that serves prediction requests:
```bash
python app.py
```
### 4. Frontend (The Dashboard)
To launch the interactive dashboard, ensure your backend is running, then in a new terminal:
```bash
streamlit run dashboard.py
```

## 🏗 System Architecture
The platform is built on an MLOps-inspired architecture that decouples heavy model training from real-time inference:

* Cloud-Based Training: Experiments and model training were conducted on the full dataset within a Kaggle environment.

* Artifact Packaging: Only the optimized model (.json) and feature registry (.pkl) are deployed to the local inference layer.

* Inference Layer: The lightweight dashboard runs locally, providing real-time forecasting without requiring local data storage.

### Submitted By: Aditi Mehta

