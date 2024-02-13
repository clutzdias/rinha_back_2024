CREATE TABLE clientes (
    id integer,
    limite integer,
    saldo integer
);

CREATE TABLE transacao (
    valor integer,
    tipo varchar(1),
    descricao varchar(100),
    realizada_em datetime,
    id_cliente integer
);

INSERT INTO clientes 
    (id, limite, saldo)
VALUES 
    (1, 100000, 0),
    (2, 80000, 0),
    (3, 1000000, 0),
    (4, 10000000, 0),
    (5, 500000, 0);

