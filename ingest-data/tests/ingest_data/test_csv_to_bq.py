"""Test src/transform/csv_to_bq.py"""

import unittest
from src.transform.csv_to_bq import parse_input, transform, Input, Output


class TestCsvToBQ(unittest.TestCase):
    def test_parse_input_wrong(self):
        """Test that failed parse equals None."""
        data = parse_input({})
        self.assertIsNone(data)

    def test_parse_input_correct(self):
        """Test that correct parse returns valid class."""
        data = parse_input(
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
            data,
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
        """Test that given input produces wanted output."""
        data = Input(
            bronze=1,
            gold=2,
            noc="4",
            rank=8,
            ranktotal=16,
            silver=32,
            team="64",
            total=128,
        )
        output = transform(data)
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
