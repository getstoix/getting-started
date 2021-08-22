"""Test src/main.py"""

import unittest
import os
from unittest import mock
from src.main import get_config, env_require


class TestMain(unittest.TestCase):
    @mock.patch.dict(
        os.environ,
        {
            "GCS_BUCKET_NAME": "bucket_name",
            "GCS_BUCKET_PREFIX": "bucket_prefix",
            "GCP_SERVICE_ACCOUNT_CREDENTIALS": "eyJuYW1lIjoidGVzdCJ9",
            "GCP_PROJECT": "project",
            "BQ_TABLE": "table",
        },
    )
    def test_get_config(self):
        """Test that get config parses environment variables correctly."""
        config = get_config()
        self.assertEqual(config.bucket_name, "bucket_name")
        self.assertEqual(config.bucket_prefix, "bucket_prefix")
        self.assertEqual(config.credentials, {"name": "test"})
        self.assertEqual(config.project, "project")
        self.assertEqual(config.table, "table")

    @mock.patch.dict(os.environ, {"TEST": "ENABLED"})
    def test_env_require(self):
        """Test that env require handles both missing and existing environment variables."""
        try:
            env_require("DOES_NOT_EXIST")
        except SystemExit:
            pass
        env_require("TEST")
