from datetime import datetime

from db.repo.customer_repo import get_customer_info
from db.repo.transaction_repo import get_customer_last_transactions
from models.customer import (
    CustomerBalanceInfo,
    CustomerBalanceStatement,
    CustomerStatement,
)
from models.transaction import Transaction, TransactionKind

from services.exceptions import CustomerNotFound


def get_customer_balance_info(customer_id: int, db_handler) -> CustomerBalanceInfo:
    customer_info = get_customer_info(customer_id, db_handler)
    if not customer_info:
        raise CustomerNotFound("Customer not found")

    _, _, limit, balance = customer_info
    return CustomerBalanceInfo(limite=limit, saldo=balance)


def get_customer_statement(customer_id: int, db_handler) -> CustomerStatement:
    customer_balance = get_customer_balance_info(customer_id, db_handler)
    balance_statement = CustomerBalanceStatement(
        **{
            "data_extrato": datetime.utcnow(),
            "total": customer_balance.saldo,
            "limite": customer_balance.limite,
        }
    )
    customer_last_transactions = get_customer_last_transactions(customer_id, db_handler)
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
