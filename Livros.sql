----- path: Livros.sql

--- CRIAÇÃO DA TABELA LIVROS ---
CREATE TABLE Livros (
    id INT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    ano INT,
    genero VARCHAR(100),
    disponivel BOOLEAN DEFAULT TRUE
);

--- INSERÇÃO DE DADOS NA TABELA LIVROS ---
INSERT INTO Livros (id, titulo, autor, ano, genero, disponivel) VALUES
(1, 'Dom Casmurro', 'Machado de Assis', 1899, 'Romance', TRUE),
(2, 'O Alquimista', 'Paulo Coelho', 1988, 'Ficção', TRUE),
(3, '1984', 'George Orwell', 1949, 'Distopia', FALSE),
(4, 'O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943, 'Infantil', TRUE),
(5, 'Cem Anos de Solidão', 'Gabriel García Márquez', 1967, 'Realismo Mágico', FALSE);

--- CONSULTAS E OPERAÇÕES NA TABELA LIVROS ---
SELECT * FROM Livros WHERE disponivel = TRUE;

--- ATUALIZAÇÃO DE DADOS NA TABELA LIVROS ---
UPDATE Livros SET disponivel = FALSE WHERE id = 1;

--- CONSULTA DE LIVROS ORDENADOS POR ANO ---
SELECT * FROM Livros ORDER BY ano DESC;

--- EXCLUSÃO DE LIVROS ANTERIORES A 1940 ---
DELETE FROM Livros WHERE ano < 1940;

--- EXCLUSÃO DA TABELA LIVROS ---
DROP TABLE Livros;

--- CRIAÇÃO DA TABELA LIVROS NOVAMENTE ---
CREATE TABLE Livros (
    id INT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    ano INT,
    genero VARCHAR(100),
    disponivel BOOLEAN DEFAULT TRUE
);

