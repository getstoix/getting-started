import os
from src.main import get_config, env_require
from unittest import mock
import unittest


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
        config = get_config()
        self.assertEqual(config.credentials, {"name": "test"})
        self.assertEqual(config.project, "myproject")
        self.assertEqual(config.query, "SELECT * FROM table")

    @mock.patch.dict(os.environ, {"TEST": "ENABLED"})
    def test_env_require(self):
        try:
            env_require("DOES_NOT_EXIST")
        except SystemExit:
            pass
        env_require("TEST")
