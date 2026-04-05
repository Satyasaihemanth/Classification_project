# app.py
import streamlit as st
import requests

st.set_page_config(page_title="Stroke Prediction", page_icon="🧠")

st.title("🧠 Stroke Prediction App")

# ---------------- INPUTS ---------------- #
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=0, max_value=120)

hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])

ever_married = st.selectbox("Ever Married", ["Yes", "No"])

work_type = st.selectbox(
    "Work Type",
    ["Private", "Self-employed", "Govt_job", "children", "Never_worked"]
)

residence = st.selectbox("Residence Type", ["Urban", "Rural"])

glucose = st.number_input("Avg Glucose Level", min_value=0.0)

bmi = st.number_input("BMI", min_value=0.0)

smoking = st.selectbox(
    "Smoking Status",
    ["formerly smoked", "never smoked", "smokes", "Unknown"]
)

# ---------------- BUTTON ---------------- #
if st.button("Predict"):

    # ✅ VALIDATION (REALISTIC)
    if age <= 0 or age > 120:
        st.warning("⚠️ Enter valid age (1–120)")
        st.stop()

    if glucose < 50 or glucose > 300:
        st.warning("⚠️ Glucose should be between 50–300")
        st.stop()

    if bmi < 10 or bmi > 70:
        st.warning("⚠️ BMI should be between 10–70")
        st.stop()

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
        with st.spinner("Predicting..."):
            response = requests.post(url, json=data)
            result = response.json()

        if result["prediction"] == 1:
            st.error("⚠️ High Risk of Stroke")
        else:
            st.success("✅ Low Risk of Stroke")

    except:
        st.error("❌ Connection Error: Backend not running")