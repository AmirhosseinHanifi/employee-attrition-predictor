import gradio as gr
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

# Load trained model
model = load_model("best_model.h5")

# Define features
feature_names = [
    'Age', 'DailyRate', 'DistanceFromHome', 'Education',
    'EnvironmentSatisfaction', 'HourlyRate', 'JobInvolvement',
    'JobLevel', 'JobSatisfaction', 'MonthlyIncome', 'NumCompaniesWorked',
    'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction',
    'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
    'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
    'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

# Temporary scaler (Ideally, load from training)
scaler = StandardScaler()

# Prediction function
def predict_attrition(*inputs):
    df = pd.DataFrame([inputs], columns=feature_names)
    df_scaled = scaler.fit_transform(df)  # Replace with trained scaler if available
    prob = model.predict(df_scaled)[0][0]
    label = "🔴 Likely to leave" if prob > 0.5 else "🟢 Likely to stay"
    return f"{label} (Confidence: {prob:.2f})"

# Gradio interface
inputs = [gr.Slider(minimum=0, maximum=60, step=1, label=feature) for feature in feature_names]
output = gr.Textbox(label="Prediction Result")

interface = gr.Interface(fn=predict_attrition, inputs=inputs, outputs=output,
                         title="Employee Attrition Prediction (AI-based)",
                         description="Enter employee features to estimate likelihood of resignation.")

interface.launch()
