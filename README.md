# 🧠 Stroke Prediction System

## 📌 Overview
This project predicts the likelihood of a person having a stroke based on health and lifestyle factors using a Machine Learning classification model.

## 🚀 Features
- Predicts stroke risk (High / Low)
- User-friendly interface (Streamlit)
- FastAPI backend for model inference
- Real-time predictions

## 🛠 Tech Stack
- Python
- Scikit-learn (GaussianNB / Classification Model)
- Pandas, NumPy
- FastAPI (Backend)
- Streamlit (Frontend)

## 📂 Project Structure
- backend.py → API for prediction
- frontend.py → Streamlit UI
- model.pkl → Trained classification model
- healthcare-dataset-stroke-data.csv → Dataset
- train_model.ipynb → Model training

## ⚙️ How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run backend
uvicorn backend:app --reload

### 3. Run frontend
streamlit run frontend.py

## 📊 Input Features
- Gender
- Age
- Hypertension
- Heart Disease
- Ever Married
- Work Type
- Residence Type
- Average Glucose Level
- BMI
- Smoking Status

## 🎯 Output
- ✅ Low Risk of Stroke  
- ⚠️ High Risk of Stroke  

## 📌 Use Case
- Early risk detection
- Healthcare analysis
- ML-based decision support

## 🔮 Future Improvements
- Improve model accuracy
- Add more health parameters
- Deploy on cloud (Streamlit Cloud / Render)
- Add visualization dashboard

## ⚠️ Disclaimer
This project is for educational purposes only and should not be used for real medical diagnosis.
