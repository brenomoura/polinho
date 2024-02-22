from contextlib import contextmanager

from psycopg2cffi.pool import ThreadedConnectionPool


class DatabaseHandler:
    def __init__(self) -> None:
        self.pool = self.setup_pool()

    def setup_pool(self):
        pool = ThreadedConnectionPool(
            minconn=1, maxconn=100, dsn="postgresql://admin:123@db:5432/rinha"
        )
        return pool

    @contextmanager
    def get_db_connection(self):
        try:
            connection = self.pool.getconn()
            yield connection
        finally:
            self.pool.putconn(connection)

    @contextmanager
    def get_db_cursor(self, commit=False):
        with self.get_db_connection() as connection:
            cursor = connection.cursor()
            try:
                yield cursor
                if commit:
                    connection.commit()
            finally:
                cursor.close()
