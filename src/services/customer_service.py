from datetime import datetime

from models.customer import (
    CustomerBalanceInfo,
    CustomerBalanceStatement,
    CustomerStatement,
)
from models.transaction import Transaction, TransactionKind
from services.exceptions import CustomerNotFound


def get_customer_balance_info(customer_id: int) -> CustomerBalanceInfo:
    balance_info_data = {
        "limite": 100000,
        "total": -9098,
    }
    # TODO - ADD THE DB INTERACTION HERE
    if None:
        raise CustomerNotFound("Customer not found")
    return CustomerBalanceInfo(**balance_info_data)


def get_customer_statement(customer_id: int) -> CustomerStatement:
    customer_balance = get_customer_balance_info(customer_id)
    balance_statement = CustomerBalanceStatement(
        **{"data_extrato": datetime.now(), **customer_balance.to_dict()}
    )
    customer_last_transactions = get_customer_last_transactions(customer_id)
    return CustomerStatement(
        saldo=balance_statement, ultimas_transacoes=customer_last_transactions
    )


def update_customer_balance(customer_id: int, new_balance: int) -> CustomerBalanceInfo:
    # TODO - ADD THE DB INTERACTION HERE
    updated_customer_balance = CustomerBalanceInfo(
        **{"total": new_balance, "limite": 1000}
    )
    return updated_customer_balance


def get_customer_last_transactions(customer_id: int) -> list[Transaction]:
    # TODO - ADD THE DB INTERACTION HERE
    last_transactions = [
        Transaction(
            **{
                "valor": 10,
                "tipo": TransactionKind.credit,
                "descricao": "aa",
                "realizado_em": datetime.now(),
            }
        ),
        Transaction(
            **{
                "valor": 200,
                "tipo": TransactionKind.debit,
                "descricao": "aa",
                "realizado_em": datetime.now(),
            }
        ),
        Transaction(
            **{
                "valor": 10,
                "tipo": TransactionKind.credit,
                "descricao": "aa",
                "realizado_em": datetime.now(),
            }
        ),
        Transaction(
            **{
                "valor": 120,
                "tipo": TransactionKind.debit,
                "descricao": "aa",
                "realizado_em": datetime.now(),
            }
        ),
        Transaction(
            **{
                "valor": 10,
                "tipo": TransactionKind.credit,
                "descricao": "aa",
                "realizado_em": datetime.now(),
            }
        ),
        Transaction(
            **{
                "valor": 100,
                "tipo": TransactionKind.debit,
                "descricao": "aa",
                "realizado_em": datetime.now(),
            }
        ),
        Transaction(
            **{
                "valor": 10,
                "tipo": TransactionKind.credit,
                "descricao": "aa",
                "realizado_em": datetime.now(),
            }
        ),
        Transaction(
            **{
                "valor": 440,
                "tipo": TransactionKind.debit,
                "descricao": "aa",
                "realizado_em": datetime.now(),
            }
        ),
        Transaction(
            **{
                "valor": 320,
                "tipo": TransactionKind.credit,
                "descricao": "aa",
                "realizado_em": datetime.now(),
            }
        ),
        Transaction(
            **{
                "valor": 777,
                "tipo": TransactionKind.debit,
                "descricao": "aa",
                "realizado_em": datetime.now(),
            }
        ),
    ]
    return last_transactions
