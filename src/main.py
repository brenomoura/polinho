import asyncio
import logging

import ujson
from mashumaro import MissingField
from mashumaro.exceptions import InvalidFieldValue
from socketify import App

from models.transaction import CreateTransaction
from services.transaction import process_transaction

app = App()

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO
)

app.json_serializer(ujson)


async def create_transaction(res, req):
    transacation_data = await res.get_json()
    try:
        transaction = CreateTransaction.from_dict(transacation_data)
    except (MissingField, InvalidFieldValue):
        res.write_status(422).cork_end(
            "validation fail, check if any missing field or wrongs types"
        )
    except Exception:
        res.write_status(500)

    balance_info = process_transaction(transaction)
    res.write_status(200).cork_end(balance_info.to_dict())


async def get_customer_statement(res, req):
    res.write_status(200).cork_end({"ola": "amigos!"})


def not_found(res, req):
    res.write_status(404).end("Not Found")


app.post("/clientes/:id/transacoes", create_transaction)
app.get("/clientes/:id/extrato", get_customer_statement)


app.listen(
    3000,
    lambda config: print(
        "Listening on port http://localhost:%s now\n" % str(config.port)
    ),
)

if __name__ == "__main__":
    app.run()
