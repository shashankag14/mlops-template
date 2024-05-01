import math
import numpy as np

from model.predict import make_prediction


def test_prediction_against_truth_value(sample_input_data):
    # Given
    expected_first_prediction_value = 1

    # When
    estimated_results = make_prediction(input_data=sample_input_data)

    # Then
    predictions = estimated_results.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.float64)
    assert estimated_results.get("errors") is None
    # assert len(predictions) == expected_no_predictions
    assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=100)
