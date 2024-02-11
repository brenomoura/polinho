from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from mashumaro import DataClassDictMixin

from models.transaction import Transaction

@dataclass
class CustomerBalanceInfo(DataClassDictMixin):
    total: int
    limite: int


@dataclass
class CustomerBalanceStatement(CustomerBalanceInfo):
    data_extrato: datetime = field(
        metadata={"serialize": lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%fZ")}
    )


@dataclass
class CustomerStatement(DataClassDictMixin):
    saldo: CustomerBalanceStatement
    ultimas_transacoes: List[Transaction]


@dataclass
class GetCustomer(DataClassDictMixin):
    id: int
