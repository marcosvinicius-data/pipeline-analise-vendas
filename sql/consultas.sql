SELECT * FROM vendas;

SELECT
    categoria,
    SUM(total) AS faturamento
FROM vendas
GROUP BY categoria;

SELECT
    regiao,
    SUM(total) AS total_vendas
FROM vendas
GROUP BY regiao;