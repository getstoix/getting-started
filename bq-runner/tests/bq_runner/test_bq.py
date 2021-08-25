"""Test src/bq.py"""

import unittest
from unittest.mock import Mock
from src.bq import BQRunner


class TestBQRunner(unittest.TestCase):
    def test_run(self):
        """Test run returning expected data from table."""
        data = [1, 2, 3]
        query_job = Mock()
        query_job.result = Mock(return_value=data)
        client = Mock()
        client.query = Mock(return_value=query_job)
        bq_runner = BQRunner(client=client)
        result = bq_runner.run("SELECT * FROM table")
        self.assertEqual(data, result)
