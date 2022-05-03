#!/usr/bin/env python3
"""Script to predict with flat approach."""
import argparse
import pickle
import sys
from argparse import Namespace

import numpy as np
import pandas as pd

from data import load_dataframe, save_dataframe


def parse_args(args: list) -> Namespace:
    """
    Parse a list of arguments.

    Parameters
    ----------
    args : list
        Arguments to parse.

    Returns
    -------
    _ : Namespace
        Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Predict")
    parser.add_argument(
        "--trained-model",
        type=str,
        required=True,
        help="Path to trained model",
    )
    parser.add_argument(
        "--x-test",
        type=str,
        required=True,
        help="Input CSV file with test features",
    )
    parser.add_argument(
        "--predictions",
        type=str,
        required=True,
        help="Output CSV file to write predictions",
    )
    parser.add_argument(
        "--classifier",
        type=str,
        required=True,
        help="Algorithm used for predicting",
    )
    return parser.parse_args(args)


def separate(y: np.ndarray, separator: str = ":sep:") -> pd.DataFrame:
    """
    Separate flat labels back into hierarchical labels.

    Parameters
    ----------
    y : np.ndarray
        Flat labels.
    separator : str, default=":sep:"
        Separator used to differentiate between columns.

    Returns
    -------
    y : pd.DataFrame
        Hierarchical labels.
    """
    y = pd.Series(y)
    y = y.str.split(
        separator,
        expand=True,
    )
    return y


def main():  # pragma: no cover
    """Predict with flat approach."""
    args = parse_args(sys.argv[1:])
    classifier = pickle.load(open(args.trained_model, "rb"))
    x_test = load_dataframe(args.x_test).squeeze()
    predictions = classifier.predict(x_test)
    if args.classifier == "flat":
        predictions = separate(predictions)
    else:
        predictions = pd.DataFrame(predictions)
    save_dataframe(predictions, args.predictions)


if __name__ == "__main__":
    main()  # pragma: no cover
