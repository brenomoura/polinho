from contextlib import contextmanager
from psycopg2cffi.pool import ThreadedConnectionPool
import os


class DatabaseHandler:
    def __init__(self) -> None:
        self.pool = self.setup_pool()

    def setup_pool(self):
        pool = ThreadedConnectionPool(
            minconn=1, maxconn=os.environ.get("MAX_CONN"), dsn=os.environ.get("DB_URL")
        )
        return pool

    @contextmanager
    def get_db_connection(self):
        try:
            connection = self.pool.getconn()
            yield connection
        finally:
            self.pool.putconn(connection)
