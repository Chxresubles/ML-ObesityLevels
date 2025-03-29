from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle
import uvicorn
from mlobesitylevels.constants import OBESITY_LEVEL, COLUMN_ENCODING

# Initialize FastAPI app
app = FastAPI()

OBESITY_ENCODING_TO_STR = {
    value: key for key, value in COLUMN_ENCODING[OBESITY_LEVEL].items()
}

# Load the model and preprocessor
try:
    with open("./output/model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("./output/preprocessor.pkl", "rb") as f:
        preprocessor = pickle.load(f)
except FileNotFoundError:
    raise Exception("Model or preprocessor files not found")


# Define input data model
class PredictionInput(BaseModel):
    Age: float
    Gender: str
    Height: float
    Weight: float
    CALC: str
    FAVC: str
    FCVC: float
    NCP: float
    SCC: str
    SMOKE: str
    CH2O: float
    family_history_with_overweight: str
    FAF: float
    TUE: float
    CAEC: str
    MTRANS: str


@app.post("/predict")
async def predict(data: PredictionInput):
    try:
        # Convert input data to DataFrame
        X = pd.DataFrame([data.model_dump()])

        # Preprocess the data
        X_processed = preprocessor.transform(X)

        # Make prediction
        prediction = model.predict(X_processed)
        X[OBESITY_LEVEL] = [OBESITY_ENCODING_TO_STR[pred] for pred in prediction]

        return X.to_dict(orient="records")[0]

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
