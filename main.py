from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DiabetesInput(BaseModel):
    age: float
    glucose: float
    insulin: float
    bmi: float
    bloodPressure: float
    hba1c: float

@app.post("/predict")
def predict(data: DiabetesInput):
    # Dummy logic — replace with ML model if needed
    score = data.glucose + data.hba1c + data.bmi

    if score < 200:
        category = "Healthy"
    elif score < 300:
        category = "Mild"
    elif score < 400:
        category = "Moderate"
    else:
        category = "Severe"

    return {"category": category}
