select * from compra;

SELECT
    Cli.nome as nomecliente,  
    J.nomejogo,              
    Com.datacompra
FROM
    Cliente AS Cli
INNER JOIN
    Compra AS Com
    ON Com.cpfcliente = Cli.cpf
INNER JOIN
    Jogo AS J
    ON Com.idjogo = J.idjogo
;

Select * from Jogo

SELECT
    nomejogo,               
    COUNT(idjogo) AS Quantidade 
FROM
    Jogo
GROUP BY
    nomejogo                  
;

SELECT
    J.NOMEJOGO,                                   
    AVG(J.VALORVENDA) AS ValorMedioDeVenda,        
    COUNT(J.IDJOGO) AS TotalDeItensNoGrupo         
FROM
    JOGO AS J
GROUP BY
    J.NOMEJOGO                                     
HAVING
    AVG(J.VALORVENDA) > 200.00                    
ORDER BY
    ValorMedioDeVenda DESC;

SELECT
    Cli.nome,
    Com.datacompra
FROM
    CLIENTE AS Cli
INNER JOIN
    COMPRA AS Com ON Com.cpfcliente = Cli.cpf
WHERE
    Cli.cpf IN ( -- Filtra a compra apenas se o CPF estiver nesta lista
        SELECT
            C.cpf
        FROM
            CLIENTE AS C
        WHERE
            C.nome < 'I' -- <<-- SUBCONSULTA: Lista os CPFs dos clientes com nome < 'I'
    )
ORDER BY
    Cli.nome;
