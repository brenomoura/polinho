def get_customer_info(customer_id: int, db_handler) -> tuple:
    with db_handler.get_db_cursor() as cursor:
        cursor.execute(
            "SELECT * FROM clientes WHERE id = %s;" % customer_id
        )
        result = cursor.fetchone()
    return result


def update_customer_balance(customer_id: int, new_balance: int, db_handler) -> tuple:
    with db_handler.get_db_cursor(commit=True) as cursor:
        result = cursor.execute(
            "UPDATE clientes SET saldo = %s WHERE id = %s RETURNING saldo, limite;"
            % (new_balance, customer_id)
        )
        result = cursor.fetchone()
    balance, limit = result
    return balance, limit

