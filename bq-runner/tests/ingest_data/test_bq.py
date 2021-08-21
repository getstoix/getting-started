import unittest
from src.bq import BQRunner
from unittest.mock import Mock


class TestBQRunner(unittest.TestCase):
    def test_run(self):
        input = [1, 2, 3]
        query_job = Mock()
        query_job.result = Mock(return_value=input)
        client = Mock()
        client.query = Mock(return_value=query_job)
        bqRunner = BQRunner(client=client)
        result = bqRunner.run("SELECT * FROM table")
        self.assertEqual(input, result)
