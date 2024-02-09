from models.transaction import CreateTransaction, TransactionBalanceInfo


def process_transaction(
    customer_id: int, transaction: CreateTransaction
) -> TransactionBalanceInfo:
    balance_info_data = {"limite": 100000, "saldo": -9098}
    return TransactionBalanceInfo(**balance_info_data)
