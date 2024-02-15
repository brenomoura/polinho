from models.transaction import CreateTransaction


def create_transaction(customer_id: int, transaction: CreateTransaction, db_handler):
    with db_handler.get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO transacoes (cliente_id, tipo, valor, descricao) VALUES (%s, %s, %s, %s);",
            (
                customer_id,
                transaction.tipo.value,
                transaction.valor,
                transaction.descricao,
            ),
        )


def get_customer_last_transactions(customer_id: int, db_handler) -> tuple:
    with db_handler.get_db_cursor(commit=True) as cursor:
        query = """
            SELECT
                cliente_id,
                tipo,
                valor,
                descricao,
                realizada_em
            FROM
                transacoes
            WHERE
                cliente_id = %s
            ORDER BY
                realizada_em DESC
            LIMIT 10;
        """ % (customer_id)
        cursor.execute(query)
        result = cursor.fetchall()
    return result
