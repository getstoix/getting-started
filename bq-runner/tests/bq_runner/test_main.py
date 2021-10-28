"""Test src/main.py"""

import unittest
import os
from unittest import mock
from main import get_config, env_require


class TestMain(unittest.TestCase):
    @mock.patch.dict(
        os.environ,
        {
            "GCP_SERVICE_ACCOUNT_CREDENTIALS": "eyJuYW1lIjoidGVzdCJ9",
            "GCP_PROJECT": "myproject",
            "BQ_QUERY": "U0VMRUNUICogRlJPTSB0YWJsZQ==",
        },
    )
    def test_get_config(self):
        """Test that get config parses environment variables correctly."""
        config = get_config()
        self.assertEqual(config.credentials, {"name": "test"})
        self.assertEqual(config.project, "myproject")
        self.assertEqual(config.query, "SELECT * FROM table")

    @mock.patch.dict(os.environ, {"TEST": "ENABLED"})
    def test_env_require(self):
        """Test that env require handles both missing and existing environment variables."""
        try:
            env_require("DOES_NOT_EXIST")
        except SystemExit:
            pass
        env_require("TEST")
