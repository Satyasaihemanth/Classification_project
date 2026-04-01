from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))

# Safe mappings
gender_map = {"Male": 1, "Female": 0, "Other": 2}
married_map = {"Yes": 1, "No": 0}
work_map = {
    "Private": 2,
    "Self-employed": 3,
    "Govt_job": 0,
    "children": 4,
    "Never_worked": 1
}
residence_map = {"Urban": 1, "Rural": 0}
smoking_map = {
    "formerly smoked": 1,
    "never smoked": 2,
    "smokes": 3,
    "Unknown": 0
}

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/predict")
def predict(data: dict):
    try:
        features = np.array([
            gender_map.get(data.get("gender"), 0),
            data.get("age", 0),
            data.get("hypertension", 0),
            data.get("heart_disease", 0),
            married_map.get(data.get("ever_married"), 0),
            work_map.get(data.get("work_type"), 0),
            residence_map.get(data.get("Residence_type"), 0),
            data.get("avg_glucose_level", 0),
            data.get("bmi", 0),
            smoking_map.get(data.get("smoking_status"), 0)
        ]).reshape(1, -1)

        prediction = model.predict(features)

        return {"prediction": int(prediction[0])}

    except Exception as e:
        return {"error": str(e)}