from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from pycaret.regression import load_model, predict_model
import pandas as pd
from asi_labs.lab3.dataset import dataset, transform_df
import typing

app = FastAPI()
model = load_model("models/output_model")


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


@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get("/sample", summary="Get a sample of inputs")
def read_inputs(count: int = 1):
    return dataset.drop(columns=["score"]).sample(count).to_dict(orient="records")


@app.post("/predict", summary="Predict the score")
def predict(inputs: list[dict]):
    df = pd.DataFrame(inputs)
    df_safe = transform_df(df)
    results = predict_model(model, df_safe)
    results = results.rename(columns={"prediction_label": "score"})

    return results.to_dict(orient="records")
