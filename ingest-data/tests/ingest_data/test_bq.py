"""Test src/load/bq.py"""

import unittest
from unittest.mock import Mock
from google.cloud import bigquery
from src.load.bq import BQLoader


class TestBQLoader(unittest.TestCase):
    def test_csv(self):
        """Test client called with provided data."""
        table_name = "stoix.gettingstarted.test"
        table = bigquery.Table(table_name)
        client = Mock()
        client.get_table = Mock(return_value=table)
        client.insert_rows = Mock()
        bq_loader = BQLoader(client=client, table=table_name)
        rows = [{"a": 1}, {"a": 2}]
        bq_loader.load(rows)
        client.insert_rows.assert_called_once_with(table=table, rows=rows)
