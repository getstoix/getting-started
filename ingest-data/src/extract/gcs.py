from os import read
from typing import Any, Dict, Iterator, List, Optional
from google.cloud import storage
import csv


class GCSExtractor:
    """Extraction of data from Google Cloud Storage."""

    bucket_name: str
    client: storage.Client
    prefix: Optional[str]

    def __init__(
        self,
        *,
        bucket_name: str,
        client: storage.Client,
        prefix: Optional[str],
    ):
        self.bucket_name = bucket_name
        self.client = client
        self.prefix = prefix

    def csv(self) -> Iterator[Dict[str, Any]]:
        """Streams the content of all matching CSV files as dicts."""
        bucket = self.client.bucket(bucket_name=self.bucket_name)
        blobs = self.client.list_blobs(bucket, prefix=self.prefix)
        for blob in blobs:
            with blob.open("rt") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    yield row
