from psycopg2cffi.pool import SimpleConnectionPool


def setup_pool():
    pool = SimpleConnectionPool(
        minconn=1, maxconn=100, dsn="postgresql://admin:123@db:5432/rinha"
    )
    return pool
