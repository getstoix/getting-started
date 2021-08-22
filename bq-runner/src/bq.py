"""Interact with BigQuery."""

from google.cloud import bigquery


class BQRunner:  # pylint: disable=too-few-public-methods
    """Runs a query in BigQuery."""

    client: bigquery.Client

    def __init__(self, *, client: bigquery.Client):
        self.client = client

    def run(self, query: str):
        """Run a SQL query."""
        query_job = self.client.query(query)
        return query_job.result()
