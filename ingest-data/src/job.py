from typing import Any, Callable, Dict, Iterable
from src.transform.csv_to_bq import Output, parse_input, transform


def job(
    extract: Callable[[], Iterable[Dict[str, Any]]], load: Callable[[Output], None]
):
    """Core logic for our ETL job."""
    for value in extract():
        input = parse_input(value)
        if input is None:
            continue
        output = transform(input)
        load(output)
