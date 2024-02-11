from models.customer import CustomerBalanceInfo
from models.transaction import (
    CreateTransaction,
    TransactionKind,
)

from services.customer_service import get_customer_balance_info, update_customer_balance
from services.exceptions import BalanceInconsistency


def process_transaction(
    customer_id: int, transaction: CreateTransaction
) -> CustomerBalanceInfo:
    customer_balance = get_customer_balance_info(customer_id)

    if transaction.tipo == TransactionKind.debit:
        new_balance = customer_balance.total - transaction.valor
        if new_balance < -customer_balance.limite:
            raise BalanceInconsistency("Invalid transaction")
    else:
        new_balance = customer_balance.total + transaction.valor
    # TODO - LOCK HERE?
    create_transaction(customer_id, transaction)    
    updated_balance_info = update_customer_balance(customer_id, new_balance)

    return updated_balance_info


def create_transaction(customer_id: int, transaction: CreateTransaction):
    # TODO - ADD THE DB INTERACTION HERE
    ...
