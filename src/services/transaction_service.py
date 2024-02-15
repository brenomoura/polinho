from db.repo.customer_repo import update_customer_balance
from db.repo.transaction_repo import create_transaction
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
    customer_balance = get_customer_balance_info(customer_id, db_handler)

    if transaction.tipo == TransactionKind.debit:
        new_balance = customer_balance.saldo - transaction.valor
        if new_balance < -customer_balance.limite:
            raise BalanceInconsistency("Invalid transaction")
    else:
        new_balance = customer_balance.saldo + transaction.valor
    # lock here - procedure maybe
    create_transaction(customer_id, transaction, db_handler)
    updated_balance, limit = update_customer_balance(customer_id, new_balance, db_handler)
    return CustomerBalanceInfo(saldo=updated_balance, limite=limit)
