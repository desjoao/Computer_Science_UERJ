-- Dados formatados em SQL (UNDERSCORES REMOVIDOS DAS COLUNAS)

INSERT INTO CLIENTE (NOME, EMAIL, CPF, ENDERECO, DATANASCIMENTO) VALUES
('Frodo Bolseiro', 'frodo_bolseiro@condado.com.br', '682.588.330-57', 'Bolsão, Condado, Terra Média', '2015-07-02'),
('Samwise Gangee', 'sam_jardinagem@condado.com.br', '058.612.680-53', 'Toca nº3, Condado, Terra Média', '2017-08-15'),
('Meriadoc Brandebuque', 'brandemerry@condado.com.br', '728.489.420-29', 'Toca nº1, Condado, Terra Média', '2012-05-22'),
('Peregrin Tuk', 'pippin_tuk@condado.com.br', '444.761.110-41', 'Toca nº2, Condado, Terra Média', '2005-12-11'),
('Gandalf', 'ocinzento@valfenda.com.br', '659.068.290-91', 'Casa cinza, Valfenda, Terra Média', '1025-01-01');

INSERT INTO TELEFONE_CLIENTE (CPF, TELEFONE) VALUES
('682.588.330-57', '99999-1111'),
('682.588.330-57', '99999-1112'),
('058.612.680-53', '99999-2221'),
('058.612.680-53', '99999-2222'),
('728.489.420-29', '99999-3331'),
('444.761.110-41', '99999-4441'),
('444.761.110-41', '99999-4442'),
('444.761.110-41', '99999-4443'),
('659.068.290-91', '99999-5551');

INSERT INTO FUNCIONARIO (NOME, EMAIL, CPF, ENDERECO, DATANASCIMENTO) VALUES
('Gandalf', 'ocinzento@valfenda.com.br', '659.068.290-91', 'Casa cinza, Valfenda, Terra Média', '1025-01-01'),
('Aragorn', 'passolargo@valfenda.com.br', '726.685.180-75', 'Estalagem Ponei Saltitante, Bri, Terra Média', '1961-06-22'),
('Arwen Undómiel', 'estrela_vespertina@valfenda.com.br', '638.163.030-21', 'Casa dourada, Valfenda, Terra Média', '1971-06-28'),
('Galadriel', 'senhora_da_luz@lothlorien.com.br', '305.465.920-82', 'Palácio real, Lothlórien, Terra Média', '1000-12-12');

INSERT INTO TELEFONE_FUNCIONARIO (CPF, TELEFONE) VALUES
('659.068.290-91', '99999-5551'),
('659.068.290-91', '99999-5552'),
('659.068.290-91', '99999-5553'),
('726.685.180-75', '99999-6661'),
('726.685.180-75', '99999-7771'),
('638.163.030-21', '99999-7771'),
('638.163.030-21', '99999-6661'),
('305.465.920-82', '99999-8881');

INSERT INTO DISTRIBUIDORA (NOME, CNPJ, ENDERECO) VALUES
('Montanha Solitária Games', '97.170.329/0001-32', 'Erebor, Mirkwood, Terra Média'),
('Jogos do Tom Bombadil', '56.621.637/0001-50', 'Casa de Tom Bombadil, Floresta Velha, Terra Média'),
('Brincadeiras de Mordor', '75.524.945/0001-01', 'Barad-dur, Mordor, Terra Média');

INSERT INTO TELEFONE_DISTRIBUIDORA (CNPJ, TELEFONE) VALUES
('97.170.329/0001-32', '2222-1111'),
('97.170.329/0001-32', '2222-2222'),
('56.621.637/0001-50', '3333-1111'),
('75.524.945/0001-01', '4444-1111'),
('75.524.945/0001-01', '4444-2222');

INSERT INTO JOGO (
    IDJOGO, NOMEJOGO, DESCRICAO, FAIXAETARIA, VALORVENDA, DESCONTO,
    CNPJDISTRIBUIDORA, DATAENTREGA, CPFFUNCIONARIO, CODIGOENCOMENDA, DATAENCOMENDA, VALORENCOMENDA
) VALUES
('0001', 'O Senhor dos Anéis: Jornadas na Terra Média',
 'Assuma o papel de um dos grandes heróis do povo livre da Terra Média, testando seu poder e sabedoria em aventuras desafiadoras por um mundo épico de fantasia. Pelas suas jornadas, você enfrentará inimigos poderosos e poderá customizar suas habilidades de acordo com seu papel na Sociedade do Anel. Enquanto a escuridão avança, unificando o mal, as sombras e a corrupção, é chegada a hora de novos heróis surgirem e iniciar suas jornadas pela Terra Média. Dê vida a seus personagens nesse cenário fabuloso e transforme suas aventuras épicas em parte história em O Senhor dos Anéis: Jornadas na Terra Média.',
 14, 899.99, 15, '97.170.329/0001-32', '2025-10-19', '659.068.290-91', 'AAA-001', '2025-10-01', 499.99),

('0002', 'War',
 'Sinta-se no papel de um verdadeiro general. Sorteie seu objetivo e defina a sua estratégia. Ataque na hora certa, defenda seus territórios e proteja suas fronteiras.',
 10, 199.99, 5, '97.170.329/0001-32', '2025-09-05', '659.068.290-91', 'OAE-951', '2025-09-20', 89.99),

('0003', 'War',
 'Sinta-se no papel de um verdadeiro general. Sorteie seu objetivo e defina a sua estratégia. Ataque na hora certa, defenda seus territórios e proteja suas fronteiras.',
 10, 199.99, 5, '97.170.329/0001-32', '2025-09-05', '659.068.290-91', 'OAE-951', '2025-09-20', 89.99),

('0004', 'War',
 'Sinta-se no papel de um verdadeiro general. Sorteie seu objetivo e defina a sua estratégia. Ataque na hora certa, defenda seus territórios e proteja suas fronteiras.',
 10, 199.99, 5, '97.170.329/0001-32', '2025-09-05', '659.068.290-91', 'OAE-951', '2025-09-20', 89.99),

('0005', 'Detetive',
 'Em uma cidade, um crime abala a tranquilidade de seus moradores: o milionário Carlos Fortuna foi vítima de assassinato! Todos são suspeitos do crime, inclusive você! Percorra a cidade e colete as provas que apontem (ou inocentem) o assassino, a cena e a arma do crime.',
 8, 119.99, 0, '56.621.637/0001-50', '2025-07-10', '726.685.180-75', 'AAC-123', '2025-07-12', 69.99),

('0006', 'Detetive',
 'Em uma cidade, um crime abala a tranquilidade de seus moradores: o milionário Carlos Fortuna foi vítima de assassinato! Todos são suspeitos do crime, inclusive você! Percorra a cidade e colete as provas que apontem (ou inocentem) o assassino, a cena e a arma do crime.',
 8, 119.99, 0, '56.621.637/0001-50', '2025-07-10', '726.685.180-75', 'AAC-123', '2025-07-12', 69.99),

('0007', 'Detetive',
 'Em uma cidade, um crime abala a tranquilidade de seus moradores: o milionário Carlos Fortuna foi vítima de assassinato! Todos são suspeitos do crime, inclusive você! Percorra a cidade e colete as provas que apontem (ou inocentem) o assassino, a cena e a arma do crime.',
 8, 119.99, 0, '56.621.637/0001-50', '2025-07-10', '726.685.180-75', 'AAC-123', '2025-07-12', 69.99),

('0008', 'Detetive',
 'Em uma cidade, um crime abala a tranquilidade de seus moradores: o milionário Carlos Fortuna foi vítima de assassinato! Todos são suspeitos do crime, inclusive você! Percorra a cidade e colete as provas que apontem (ou inocentem) o assassino, a cena e a arma do crime.',
 8, 119.99, 0, '56.621.637/0001-50', '2025-07-10', '726.685.180-75', 'AAC-123', '2025-07-12', 69.99),

('0009', 'Detetive',
 'Em uma cidade, um crime abala a tranquilidade de seus moradores: o milionário Carlos Fortuna foi vítima de assassinato! Todos são suspeitos do crime, inclusive você! Percorra a cidade e colete as provas que apontem (ou inocentem) o assassino, a cena e a arma do crime.',
 8, 119.99, 0, '56.621.637/0001-50', '2025-07-10', '726.685.180-75', 'AAC-123', '2025-07-12', 69.99),

('0010', 'Rummikub',
 'Jogue Rummikub com seus amigos e tenha toda a atenção e raciocínio para sair como o grande vencedor! O desafio de Rummikub está em se livrar de todas as pedras em suas mãos antes dos seus oponentes.',
 7, 279.99, 10, '56.621.637/0001-50', '2025-10-09', '305.465.920-82', 'ABC-123', '2025-10-01', 129.99),

('0011', 'Rummikub',
 'Jogue Rummikub com seus amigos e tenha toda a atenção e raciocínio para sair como o grande vencedor! O desafio de Rummikub está em se livrar de todas as pedras em suas mãos antes dos seus oponentes.',
 7, 279.99, 10, '56.621.637/0001-50', '2025-10-09', '305.465.920-82', 'ABC-123', '2025-10-01', 129.99),

('0012', 'Rummikub',
 'Jogue Rummikub com seus amigos e tenha toda a atenção e raciocínio para sair como o grande vencedor! O desafio de Rummikub está em se livrar de todas as pedras em suas mãos antes dos seus oponentes.',
 7, 279.99, 10, '56.621.637/0001-50', '2025-10-09', '305.465.920-82', 'ABC-123', '2025-10-01', 129.99),

('0013', 'Rummikub',
 'Jogue Rummikub com seus amigos e tenha toda a atenção e raciocínio para sair como o grande vencedor! O desafio de Rummikub está em se livrar de todas as pedras em suas mãos antes dos seus oponentes.',
 7, 279.99, 10, '56.621.637/0001-50', '2025-08-05', '305.465.920-82', 'ABC-123', '2025-07-22', 129.99),
 
('0014', 'Dungeons & Dragons Basic Set (First Edition)', 'Este livro introduz os conceitos e regras básicas de Dungeons & Dragons, permitindo que jogadores iniciem suas primeiras aventuras até o 3º nível. Ele apresenta orientações simplificadas para o Mestre do Jogo e destaca a natureza aberta e expansível do RPG, incentivando a criatividade e adaptação das regras. Para experiências mais avançadas, recomenda-se a série Advanced Dungeons & Dragons.',
 500, 999.99, 0, '56.621.637/0001-50', '2008-10-05', '659.068.290-91', 'DND-999', '2008-06-12', 599.99),

('0015', 'Avanced Dungeons & Dragons (First Edition)', 'Advanced Dungeons & Dragons (1ª Edição) é o clássico que definiu o RPG de mesa moderno. Publicado originalmente entre 1977 e 1979, este sistema apresenta regras detalhadas para criação de personagens, combate, magia e exploração, permitindo aventuras épicas em mundos de fantasia. Ideal para mestres e jogadores que buscam a experiência autêntica e desafiadora das origens do D&D.',
 1000, 1999.99, 0, '56.621.637/0001-50', '2008-10-05', '659.068.290-91', 'DND-999', '2008-06-12', 1299.99);

INSERT INTO COMPRA (IDJOGO, CPFCLIENTE, DATACOMPRA) 
VALUES
('0013', '682.588.330-57', '2025-08-20'),
('0002', '682.588.330-57', '2025-10-02'),
('0005', '058.612.680-53', '2025-08-21'),
('0010', '728.489.420-29', '2025-10-17'),
('0001', '444.761.110-41', '2025-10-19'),
('0014', '659.068.290-91', '2025-02-17'),
('0015', '659.068.290-91', '2025-02-17');

