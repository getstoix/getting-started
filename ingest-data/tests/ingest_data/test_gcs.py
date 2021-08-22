import unittest
from src.extract.gcs import GCSExtractor
from src.job import job
from unittest.mock import Mock, patch
import io


class TestGCSExtractor(unittest.TestCase):
    def test_csv(self):
        bucket_name = ""
        f = io.StringIO("a,b,c\n1,2,3\n4,5,6")
        blob = Mock()
        blob.open = Mock(return_value=f)
        client = Mock()
        client.list_blobs = Mock(return_value=[blob])
        prefix = None
        gcsExtractor = GCSExtractor(
            bucket_name=bucket_name, client=client, prefix=prefix
        )
        rows = gcsExtractor.csv()
        self.assertEqual(
            list(rows), [{"a": "1", "b": "2", "c": "3"}, {"a": "4", "b": "5", "c": "6"}]
        )
