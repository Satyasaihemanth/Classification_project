from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Load model
model = pickle.load(open("model.pkl", "rb"))

# ✅ Input schema (this fixes Swagger issue)
class InputData(BaseModel):
    gender: str
    age: float
    hypertension: int
    heart_disease: int
    ever_married: str
    work_type: str
    Residence_type: str
    avg_glucose_level: float
    bmi: float
    smoking_status: str

# ✅ Mappings
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

# ✅ Predict API
@app.post("/predict")
def predict(data: InputData):
    try:
        features = np.array([
            gender_map.get(data.gender, 0),
            data.age,
            data.hypertension,
            data.heart_disease,
            married_map.get(data.ever_married, 0),
            work_map.get(data.work_type, 0),
            residence_map.get(data.Residence_type, 0),
            data.avg_glucose_level,
            data.bmi,
            smoking_map.get(data.smoking_status, 0)
        ]).reshape(1, -1)

        prediction = model.predict(features)

        return {
            "prediction": int(prediction[0]),
            "result": "High Risk of Stroke" if prediction[0] == 1 else "Low Risk of Stroke"
        }

    except Exception as e:
        return {"error": str(e)}