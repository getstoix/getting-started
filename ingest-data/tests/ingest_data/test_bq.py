import unittest
from src.load.bq import BQLoader
from src.job import job
from unittest.mock import Mock, patch
import io
from google.cloud import bigquery


class TestBQLoader(unittest.TestCase):
    def test_csv(self):
        table_name = "stoix.gettingstarted.test"
        table = bigquery.Table(table_name)
        client = Mock()
        client.get_table = Mock(return_value=table)
        client.insert_rows = Mock()
        bqLoader = BQLoader(client=client, table=table_name)
        rows = [{"a": 1}, {"a": 2}]
        bqLoader.load(rows)
        client.insert_rows.assert_called_once_with(table=table, rows=rows)
