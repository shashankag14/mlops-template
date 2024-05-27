import math
import pathlib
import pytest
import pandas as pd

from model.config import config as model_config
from model.predict import make_prediction
from model.processing.data_manager import load_dataset

PACKAGE_ROOT = pathlib.Path(__file__).parent.parent.parent

@pytest.mark.skip
@pytest.mark.differential
def test_model_prediction_differential(
        *,
        save_file: str ='test_data_predictions.csv'):
    """
    This test compares the prediction result similarity of
    the current model with the previous model's results.
    """
    # Given
    previous_model_df = pd.read_csv(f'{PACKAGE_ROOT}/{save_file}')
    previous_model_predictions = previous_model_df.predictions.values
    test_data = load_dataset(file_name=model_config.test_data_file)
    multiple_test_input = test_data[99:120]

    # When
    current_result = make_prediction(input_data=multiple_test_input)
    current_model_predictions = current_result.get('predictions')

    # Then
    # diff the current model vs. the old model
    assert len(previous_model_predictions) == len(
        current_model_predictions)

    # Perform the differential test
    for previous_value, current_value in zip(
            previous_model_predictions, current_model_predictions):

        # convert numpy float64 to Python float.
        previous_value = previous_value.item()
        current_value = current_value.item()

        # rel_tol is the relative tolerance – it is the maximum allowed
        # difference between a and b, relative to the larger absolute
        # value of a or b. For example, to set a tolerance of 5%, pass
        # rel_tol=0.05.
        assert math.isclose(previous_value,
                            current_value,
                            rel_tol=model_config.ACCEPTABLE_MODEL_DIFFERENCE)
