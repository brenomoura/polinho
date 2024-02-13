def get_customer_info(customer_id: int, db_conn) -> tuple:
    with db_conn.cursor() as cursor:
        result = cursor.execute(
            "SELECT * FROM clientes WHERE id = %s;" % customer_id
        ).fetchone()
    return result


def update_customer_balance(customer_id: int, new_balance: int, db_conn) -> tuple:
    with db_conn.cursor() as cursor:
        result = cursor.execute(
            "UPDATE clientes SET saldo = %s WHERE id = %s RETURNING saldo, limite;"
            % (new_balance, customer_id)
        ).fetchone()
    balance, limit = result
    return balance, limit

