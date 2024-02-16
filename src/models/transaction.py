from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

from mashumaro import DataClassDictMixin
from mashumaro.exceptions import InvalidFieldValue


class TransactionKind(Enum):
    credit = "c"
    debit = "d"


@dataclass
class _TransactionBase(DataClassDictMixin):
    valor: int
    tipo: TransactionKind
    descricao: str


@dataclass
class CreateTransaction(_TransactionBase):
    ...

    @classmethod
    def __pre_deserialize__(cls, d):
        errors = []
        descricao = d.get("descricao")
        valor = d.get("valor")
        if not descricao:
            errors.append("description can't be null or empty")

        if descricao and len(descricao) > 10:
            errors.append("description can't be greater than 10 characters")
        
        if valor and not isinstance(valor, int):
            errors.append("valor must be an integer")
        if errors:
            raise InvalidFieldValue("", "", "", cls, str(errors))
        return d


@dataclass
class Transaction(_TransactionBase):
    realizado_em: datetime = field(
        metadata={"serialize": lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%fZ")}
    )
