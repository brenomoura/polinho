from psycopg_pool import ConnectionPool


def setup_pool():
    pool = ConnectionPool(
        "postgresql://admin:123@localhost:5432/rinha", min_size=1, max_size=1000
    )
    return pool
