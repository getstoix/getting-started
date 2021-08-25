"""Core components for the job."""

from typing import Any, Callable, Dict, Iterable
from transform.csv_to_bq import Output, parse_input, transform

BATCH_SIZE = 1024


def job(
    extract: Callable[[], Iterable[Dict[str, Any]]],
    load: Callable[[Iterable[Output]], None],
):
    """Core logic for our ETL job."""
    outputs = []
    for row in extract():
        data = parse_input(row)
        if data is None:
            continue
        output = transform(data)
        outputs.append(output)
        if len(outputs) > BATCH_SIZE:
            load(outputs)
            outputs = []
    if len(outputs) > 0:
        load(outputs)
