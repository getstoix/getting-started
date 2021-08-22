"""Extracting data from Google Cloud Storage."""

import csv
from typing import Any, Dict, Iterator, Optional
from google.cloud import storage


class GCSExtractor:  # pylint: disable=too-few-public-methods
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
            with blob.open("rt") as blob_file:
                reader = csv.DictReader(blob_file)
                for row in reader:
                    yield row
