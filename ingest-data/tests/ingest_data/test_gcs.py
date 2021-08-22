"""Test src/extract/gcs.py"""

import io
import unittest
from unittest.mock import Mock
from src.extract.gcs import GCSExtractor


class TestGCSExtractor(unittest.TestCase):
    def test_csv(self):
        """Test extracted CSV match blob content."""
        bucket_name = ""
        blob_file = io.StringIO("a,b,c\n1,2,3\n4,5,6")
        blob = Mock()
        blob.open = Mock(return_value=blob_file)
        client = Mock()
        client.list_blobs = Mock(return_value=[blob])
        prefix = None
        gcs_extractor = GCSExtractor(
            bucket_name=bucket_name, client=client, prefix=prefix
        )
        rows = gcs_extractor.csv()
        self.assertEqual(
            list(rows), [{"a": "1", "b": "2", "c": "3"}, {"a": "4", "b": "5", "c": "6"}]
        )
