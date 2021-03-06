#!/usr/bin/env python3
"""Script to share common functions for data manipulation."""
import csv
from typing import TextIO

import pandas as pd


def load_dataframe(path: TextIO) -> pd.DataFrame:
    """
    Load a dataframe from a CSV file.

    Parameters
    ----------
    path : TextIO
        Path to CSV file.

    Returns
    -------
    df : pd.DataFrame
        Loaded dataframe.
    """
    return pd.read_csv(path, compression="infer", header=0, sep=",", low_memory=False)


def save_dataframe(dataframe: pd.DataFrame, file_path: TextIO) -> None:
    """
    Save dataframe to CSV file.

    Parameters
    ----------
    dataframe : pd.DataFrame
        Dataframe to save.
    file_path : TextIO
        Path to save dataframe.
    """
    dataframe.to_csv(
        file_path,
        index=False,
        header=True,
        sep=",",
        compression="infer",
        quoting=csv.QUOTE_ALL,
    )
