"""Transformation of data."""

from collections import namedtuple
from typing import Any, Dict, Optional
import datetime

Input = namedtuple("Input", ["date", "beverage_type"])
Output = namedtuple("Output", ["date", "beverage_type"])


def parse_input(value: Dict[str, Any]) -> Optional[Input]:
    """Parse a dict to expected input.

    Returns:
        Parsed input, None if parsing failed.
    """
    try:
        date = value["date"]
        beverage_type = value["type"]
    except KeyError:
        return None

    return Input(date=date, beverage_type=beverage_type)


def transform(data: Input) -> Output:
    """Transform our CSV data to the format we have in BigQuery."""
    cleaned_date = datetime.datetime.strptime(data.date, "%Y%m%d").date().isoformat()
    return Output(date=cleaned_date, beverage_type=data.beverage_type)
