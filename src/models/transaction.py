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
    def __post_deserialize__(cls, obj):
        # check orders and validate with the follwing payloads
        """
        {"valor": 1.2, "tipo": "d", "descricao": "devolve"}
        {"valor": 1, "tipo": "x", "descricao": "devolve"}
        {"valor": 1, "tipo": "c", "descricao": "123456789 e mais um pouco"}
        {"valor": 1, "tipo": "c", "descricao": ""}
        {"valor": 1, "tipo": "c", "descricao": null}
        """
        if obj.descricao is None:
            raise InvalidFieldValue(
                "descricao",
                "string",
                cls,
                "description can't be null",
            )

        if obj.descricao and len(obj.descricao) > 10:
            raise InvalidFieldValue(
                "descricao",
                "string",
                cls,
                "description can't be greater than 10 characters",
            )
        
        if not isinstance(obj.valor, int):
            raise InvalidFieldValue(
                "valor",
                "integer",
                cls,
                "valor must be an integer",
            )
        return obj


@dataclass
class Transaction(_TransactionBase):
    realizado_em: datetime = field(
        metadata={"serialize": lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%fZ")}
    )
