from fastapi import FastAPI
from pydantic import BaseModel
from pycaret.regression import load_model, predict_model
import pandas as pd
from asi_labs.lab3.dataset import dataset
import typing

app = FastAPI()
model = load_model(".models/output_model")


class InputsModel(BaseModel):
    gender: typing.Literal["male", "female"]
    ethnicity: str
    fcollege: typing.Literal["yes", "no"]
    mcollege: typing.Literal["yes", "no"]
    home: typing.Literal["yes", "no"]
    urban: typing.Literal["yes", "no"]
    unemp: float
    wage: float
    distance: float
    tuition: float
    education: int
    income: typing.Literal["high", "low"]
    region: str


@app.get("/sample", summary="Get a sample of inputs")
def read_inputs(count: int = 1):
    return dataset.drop(columns=["score"]).sample(count).to_dict(orient="records")


@app.post("/predict", summary="Predict the score")
def predict(inputs: list[dict]):
    df = pd.DataFrame(inputs)
    results = predict_model(model, df)
    results = results.rename(columns={"prediction_label": "score"})

    return results.to_dict(orient="records")
