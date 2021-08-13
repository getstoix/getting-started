from typing import Dict, Iterable
from google.cloud import bigquery


class BQLoader:
    """Insertion of data in BigQuery."""

    client: bigquery.Client
    table: bigquery.Table

    def __init__(self, *, client: bigquery.Client, table: str):
        self.client = client
        self.table = client.get_table(table=table)

    def load(self, row: Iterable[Dict]):
        """Insert rows into a table via the streaming API.

        Raises:
            ValueError: if table's schema is not set or `rows` is not a `Sequence`.
        """
        self.client.insert_rows(table=self.table, rows=[row])
