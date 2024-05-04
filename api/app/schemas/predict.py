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
                        "sex": "female",
                        "age": 20,
                        "sibsp": 0,
                        "parch": 2,
                        "fare": 78.9,
                        "cabin": "B",
                        "embarked": "Q",
                        "title": "Miss"
                    }
                ]
            }
        }
