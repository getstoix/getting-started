"""Test src/transform/csv_to_bq.py"""

import unittest
from transform.csv_to_bq import parse_input, transform, Input, Output


class TestCsvToBQ(unittest.TestCase):
    def test_parse_input_wrong(self):
        """Test that failed parse equals None."""
        data = parse_input({})
        self.assertIsNone(data)

    def test_parse_input_correct(self):
        """Test that correct parse returns valid class."""
        data = parse_input(
            {
                "date": "20210816",
                "type": "coffee",
            }
        )
        self.assertEqual(
            data,
            Input(date="20210816", beverage_type="coffee"),
        )

    def test_transform(self):
        """Test that given input produces wanted output."""
        data = Input(date="20210816", beverage_type="coffee")
        output = transform(data)
        self.assertEqual(
            output,
            Output(date="2021-08-16", beverage_type="coffee"),
        )
