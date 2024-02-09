from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from mashumaro import DataClassDictMixin

from models.transaction import Transaction


@dataclass
class BalanceInfo(DataClassDictMixin):
    total: int
    data_extrato: datetime = field(
        metadata={"serialize": lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%fZ")}
    )
    limite: int


@dataclass
class CustomerInfo(DataClassDictMixin):
    saldo: BalanceInfo
    ultimas_transacoes: List[Transaction]


@dataclass
class GetCustomer(DataClassDictMixin):
    id: int
