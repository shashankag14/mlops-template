import math

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from fastapi.testclient import TestClient


def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.replace({np.nan: None}).to_dict(orient="records")
    }

    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["predictions"]
    assert prediction_data["errors"] is None

    _predictions = list(prediction_data["predictions"])
    y_true = test_data["survived"]
    accuracy = accuracy_score(y_true, _predictions)
    assert accuracy > 0.7