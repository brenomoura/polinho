from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

from mashumaro import DataClassDictMixin


class TransactionKind(Enum):
    credit = "c"
    debit = "d"


@dataclass
class _TransactionBase(DataClassDictMixin):
    valor: int
    tipo: TransactionKind
    descricao: str


@dataclass
class CreateTransaction(_TransactionBase): ...


@dataclass
class Transaction(_TransactionBase):
    realizado_em: datetime = field(
        metadata={"serialize": lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%fZ")}
    )


@dataclass
class TransactionBalanceInfo(DataClassDictMixin):
    limite: int
    saldo: int
