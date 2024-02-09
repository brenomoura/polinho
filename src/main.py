import logging

import ujson
from mashumaro import MissingField
from mashumaro.exceptions import InvalidFieldValue
from socketify import App

from models.transaction import CreateTransaction
from services.customer_service import get_customer_info
from services.transaction_service import process_transaction

app = App()

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO
)


def log(handler):
    async def log_route(res, req):
        logging.info(f"{req.get_method()}{req.get_full_url()} {req.get_headers()}")
        await handler(res, req)

    return log_route


@app.on_error
async def on_error(error, res, req):
    logging.exception("Something goes %s" % str(error))
    if res != None:
        res.write_status(500)
        res.end("Sorry something went wrong")


app.json_serializer(ujson)


@log
async def create_transaction(res, req):
    customer_id = int(req.get_parameter(0))
    transacation_data = await res.get_json()
    try:
        transaction_creation_data = CreateTransaction.from_dict(transacation_data)
        balance_info = process_transaction(customer_id, transaction_creation_data)
        res.write_status(200).cork_end(balance_info.to_dict())
    except (MissingField, InvalidFieldValue):
        error_msg = "validation fail, check if any missing field or wrongs types"
        logging.exception(error_msg)
        res.write_status(422).cork_end(error_msg)
    except Exception:
        res.write_status(500)


@log
async def get_customer_statement(res, req):
    customer_id = int(req.get_parameter(0))
    customer_info = get_customer_info(customer_id)
    res.write_status(200).cork_end(customer_info.to_dict())


def not_found(res, req):
    res.write_status(404).end("Not Found")


app.post("/clientes/:id/transacoes", create_transaction)
app.get("/clientes/:id/extrato", get_customer_statement)


app.listen(
    3000,
    lambda config: logging.info(
        "Listening on port http://localhost:%d now\n" % config.port
    ),
)

if __name__ == "__main__":
    app.run()
