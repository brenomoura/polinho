from datetime import datetime
from models.customer import BalanceInfo, CustomerInfo
from models.transaction import Transaction, TransactionKind


def get_customer_balance_info(customer_id: int) -> BalanceInfo:
    balance_info_data = {
        "limite": 100000,
        "total": -9098,
        "data_extrato": datetime.now(),
    }
    return BalanceInfo(**balance_info_data)


def get_customer_info(customer_id: int) -> CustomerInfo:
    customer_balance = get_customer_balance_info(customer_id)
    customer_last_transactions = get_customer_last_transactions(customer_id)
    return CustomerInfo(
        saldo=customer_balance, ultimas_transacoes=customer_last_transactions
    )


def get_customer_last_transactions(customer_id: int) -> list[Transaction]:
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
