import asyncio

import ujson
from socketify import App

app = App()

app.json_serializer(ujson)


async def make_transaction(res, req):
    info = await res.get_json()
    print(info)
    res.cork_end({"ola": "amigos!"})


async def get_statement(res, req):
    print(req)
    res.cork_end({"ola": "amigos!"})


def not_found(res, req):
    res.write_status(404).end("Not Found")


app.post("/clientes/:id/transacoes", make_transaction)
app.get("/clientes/:id/extrato", get_statement)
# app.any("/*", not_found)


app.listen(
    3000,
    lambda config: print(
        "Listening on port http://localhost:%s now\n" % str(config.port)
    ),
)

if __name__ == "__main__":
    app.run()
