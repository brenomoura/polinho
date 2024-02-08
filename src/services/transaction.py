from models.transaction import BalanceInfo, CreateTransaction


def process_transaction(transaction: CreateTransaction) -> BalanceInfo:
    balance_info_data = {"limite": 100000, "saldo": -9098}
    return BalanceInfo(**balance_info_data)
