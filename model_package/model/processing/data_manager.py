import re
import typing as t
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

from model import __version__ as _version
from model.config.core import DATASET_DIR, TRAINED_MODEL_DIR, config


def get_first_cabin(row):
    try:
        return row.split()[0]
    except:
        return np.nan

def get_title(passenger):
    line = passenger
    if re.search('Mrs', line):
        return 'Mrs'
    elif re.search('Mr', line):
        return 'Mr'
    elif re.search('Miss', line):
        return 'Miss'
    elif re.search('Master', line):
        return 'Master'
    else:
        return 'Other'

def preprocess_dataset(*, dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe = dataframe.replace('?', np.nan)

    dataframe['cabin'] = dataframe['cabin'].apply(get_first_cabin)
    dataframe['title'] = dataframe['name'].apply(get_title)

    dataframe['fare'] = dataframe['fare'].astype('float')
    dataframe['age'] = dataframe['age'].astype('float')

    dataframe.drop(labels=config.model_config.vars_to_drop, axis=1, inplace=True)

    return dataframe


def load_dataset(*, file_name: str) -> pd.DataFrame:
    dataframe = pd.read_csv(Path(f"{DATASET_DIR}/{file_name}"))

    # preprocess and clean the data before using it in the model
    preprocessed_dataframe = preprocess_dataset(dataframe=dataframe)
    return preprocessed_dataframe


def save_pipeline(*, pipeline_to_persist: Pipeline) -> None:
    """Persist the pipeline.
    Saves the versioned model, and overwrites any previous
    saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.
    """

    # Prepare versioned save file name
    save_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)


def load_pipeline(*, file_name: str) -> Pipeline:
    """Load a persisted pipeline."""

    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipelines(*, files_to_keep: t.List[str]) -> None:
    """
    Remove old model pipelines.
    This is to ensure there is a simple one-to-one
    mapping between the package version and the model
    version to be imported and used by other applications.
    """
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()
