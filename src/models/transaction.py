from dataclasses import dataclass
from typing import Any, Mapping, Type

from mashumaro import DataClassDictMixin


@dataclass
class CreateTransaction(DataClassDictMixin):
    valor: int
    tipo: str
    descricao: str


@dataclass
class BalanceInfo(DataClassDictMixin):
    limite: int
    saldo: int
