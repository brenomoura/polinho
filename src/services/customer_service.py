from datetime import datetime

from models.customer import (
    CustomerBalanceInfo,
    CustomerBalanceStatement,
    CustomerStatement,
)
from models.transaction import Transaction, TransactionKind

from services.exceptions import CustomerNotFound


def get_customer_balance_info(customer_id: int, cursor) -> CustomerBalanceInfo:
    cursor.execute("SELECT * FROM clientes WHERE id = %s;" % customer_id)
    customer_info = cursor.fetchone()

    if not customer_info:
        raise CustomerNotFound("Customer not found")

    _, _, limit, balance = customer_info
    return CustomerBalanceInfo(limite=limit, saldo=balance)


def get_customer_statement(customer_id: int, db_handler) -> CustomerStatement:
    with db_handler.get_db_connection() as conn:
        cursor = conn.cursor()
        customer_balance = get_customer_balance_info(customer_id, cursor)
        balance_statement = CustomerBalanceStatement(
            **{
                "data_extrato": datetime.utcnow(),
                "total": customer_balance.saldo,
                "limite": customer_balance.limite,
            }
        )
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
        customer_last_transactions = cursor.fetchall()
        cursor.close()

    return CustomerStatement(
        saldo=balance_statement,
        ultimas_transacoes=[
            Transaction(
                tipo=TransactionKind(transaction[1]),
                valor=transaction[2],
                descricao=transaction[3],
                realizado_em=transaction[4],
            )
            for transaction in customer_last_transactions
        ],
    )
