"""Core components for the job."""

from typing import Any, Callable, Dict, Iterable
from src.transform.csv_to_bq import Output, parse_input, transform


def job(
    extract: Callable[[], Iterable[Dict[str, Any]]], load: Callable[[Output], None]
):
    """Core logic for our ETL job."""
    for row in extract():
        data = parse_input(row)
        if data is None:
            continue
        output = transform(data)
        load([output])
