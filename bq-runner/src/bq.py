from typing import Dict, Iterable
from google.cloud import bigquery
from time import sleep
from google.cloud.exceptions import GoogleCloudError


class BQRunner:
    """Runs a query in BigQuery."""

    client: bigquery.Client

    def __init__(self, *, client: bigquery.Client):
        self.client = client

    def run(self, query: str):
        """Run a SQL query."""
        query_job = self.client.query(query)
        query_job.result()
