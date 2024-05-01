import pandas as pd
import pytest

from model.processing.data_manager import load_dataset
from model.config.core import config


@pytest.fixture()
def sample_input_data() -> pd.DataFrame:
    return load_dataset(file_name=config.app_config.test_data_file)