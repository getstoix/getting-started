from collections import namedtuple
from typing import Any, Dict, Optional

Input = namedtuple(
    "Input", ["bronze", "gold", "noc", "rank", "ranktotal", "silver", "team", "total"]
)
Output = namedtuple(
    "Output", ["bronze", "country_code", "country_name", "gold", "silver"]
)


def parse_input(value: Dict[str, Any]) -> Optional[Input]:
    """Parse a dict to expected input.

    Returns:
        Parsed input, None if parsing failed.
    """
    try:
        bronze = int(value["bronze"])
        gold = int(value["gold"])
        noc = value["noc"]
        rank = int(value["rank"])
        ranktotal = int(value["ranktotal"])
        silver = int(value["silver"])
        team = value["team"]
        total = int(value["total"])
    except KeyError:
        return None

    if bronze + silver + gold is not total:
        return None

    return Input(
        bronze=bronze,
        gold=gold,
        noc=noc,
        rank=rank,
        ranktotal=ranktotal,
        silver=silver,
        team=team,
        total=total,
    )


def transform(input: Input) -> Output:
    """Transform our CSV data to the format we have in BigQuery."""
    return Output(
        bronze=input.bronze,
        country_code=input.noc,
        country_name=input.team,
        gold=input.gold,
        silver=input.silver,
    )
