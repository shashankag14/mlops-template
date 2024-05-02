from typing import Any, List, Optional

from pydantic import BaseModel
from model.processing.validation import TitanicInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class TitanicDataInputs(BaseModel):
    inputs: List[TitanicInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Sex": "female",
                        "Age": 20,
                        "Sibsp": 0,
                        "Parch": 2,
                        "Fare": 78.9,
                        "Cabin": "B",
                        "Embarked": "Q",
                        "Title": "Miss"
                    }
                ]
            }
        }
