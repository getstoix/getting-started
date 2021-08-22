import unittest
from src.transform.csv_to_bq import parse_input, transform, Input, Output
from unittest.mock import Mock, patch
import io
from google.cloud import bigquery


class TestCsvToBQ(unittest.TestCase):
    def test_parse_input_wrong(self):
        input = parse_input({})
        self.assertIsNone(input)

    def test_parse_input_correct(self):
        input = parse_input(
            {
                "bronze": 1,
                "gold": 2,
                "noc": "4",
                "rank": 8,
                "ranktotal": 16,
                "silver": 32,
                "team": "64",
                "total": 128,
            }
        )
        self.assertEqual(
            input,
            Input(
                bronze=1,
                gold=2,
                noc="4",
                rank=8,
                ranktotal=16,
                silver=32,
                team="64",
                total=128,
            ),
        )

    def test_transform(self):
        input = Input(
            bronze=1,
            gold=2,
            noc="4",
            rank=8,
            ranktotal=16,
            silver=32,
            team="64",
            total=128,
        )
        output = transform(input)
        self.assertEqual(
            output,
            Output(
                bronze=1,
                country_code="4",
                country_name="64",
                gold=2,
                silver=32,
            ),
        )
