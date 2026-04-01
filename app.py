import streamlit as st
import requests

st.title("🧠 Stroke Prediction App")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=1)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
ever_married = st.selectbox("Ever Married", ["Yes", "No"])
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
residence = st.selectbox("Residence Type", ["Urban", "Rural"])
glucose = st.number_input("Avg Glucose Level")
bmi = st.number_input("BMI")
smoking = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])

if st.button("Predict"):
    url = "http://127.0.0.1:8000/predict"

    data = {
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "ever_married": ever_married,
        "work_type": work_type,
        "Residence_type": residence,
        "avg_glucose_level": glucose,
        "bmi": bmi,
        "smoking_status": smoking
    }

    try:
        response = requests.post(url, json=data)
        result = response.json()

        st.write(result)  # debug output

        if "prediction" in result:
            if result["prediction"] == 1:
                st.error("⚠️ High Risk of Stroke")
            else:
                st.success("✅ Low Risk of Stroke")
        else:
            st.error(result["error"])

    except Exception as e:
        st.error(f"Connection Error: {e}")