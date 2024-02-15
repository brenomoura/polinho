CREATE UNLOGGED TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    limite BIGINT NOT NULL DEFAULT 0,
    saldo BIGINT NOT NULL DEFAULT 0
);

CREATE UNLOGGED TABLE IF NOT EXISTS transacoes (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER,
    tipo CHAR(1) CHECK (tipo IN ('c', 'd')) NOT NULL,
    valor BIGINT NOT NULL,
    descricao VARCHAR(10),
    realizada_em TIMESTAMP NOT NULL DEFAULT NOW(),

    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE INDEX idx_clientes_id ON clientes(id);
CREATE INDEX idx_transacoes_cliente_id ON transacoes(cliente_id);
CREATE INDEX idx_transacoes_realizada_em ON transacoes(realizada_em DESC);


DO $$
BEGIN
  INSERT INTO clientes (nome, limite)
  VALUES
    ('o barato sai caro', 1000 * 100),
    ('zan corp ltda', 800 * 100),
    ('les cruders', 10000 * 100),
    ('padaria joia de cocaia', 100000 * 100),
    ('kid mais', 5000 * 100);
END; $$