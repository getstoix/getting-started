"""Test src/job.py"""

import unittest
from unittest.mock import Mock, patch
from job import job


class TestJob(unittest.TestCase):
    @patch("src.job.parse_input")
    @patch("src.job.transform")
    def test_job(self, transform: Mock, parse_input: Mock):
        """Test job runs the ETL flow."""
        extract = Mock(return_value=[1])
        load = Mock()
        parse_input.return_value = 2
        transform.return_value = 3
        job(extract=extract, load=load)
        parse_input.assert_called_once_with(1)
        transform.assert_called_once_with(2)
        load.assert_called_once_with([3])
