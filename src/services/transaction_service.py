from models.customer import CustomerBalanceInfo
from models.transaction import (
    CreateTransaction,
    TransactionKind,
)

from services.customer_service import get_customer_balance_info
from services.exceptions import BalanceInconsistency


def process_transaction(
    customer_id: int, transaction: CreateTransaction, db_handler
) -> CustomerBalanceInfo:
    with db_handler.get_db_connection() as conn:
        cursor = conn.cursor()
        customer_balance = get_customer_balance_info(customer_id, cursor)

        if transaction.tipo == TransactionKind.debit:
            new_balance = customer_balance.saldo - transaction.valor
            if new_balance < -customer_balance.limite:
                raise BalanceInconsistency("Invalid transaction")
        else:
            new_balance = customer_balance.saldo + transaction.valor
        cursor.execute(
            "INSERT INTO transacoes (cliente_id, tipo, valor, descricao) VALUES (%s, %s, %s, %s);",
            (
                customer_id,
                transaction.tipo.value,
                transaction.valor,
                transaction.descricao,
            ),
        )
        result = cursor.execute(
            "UPDATE clientes SET saldo = %s WHERE id = %s RETURNING saldo, limite;"
            % (new_balance, customer_id)
        )
        result = cursor.fetchone()
        updated_balance, limit = result
        cursor.close()
        conn.commit()
    return CustomerBalanceInfo(saldo=updated_balance, limite=limit)
