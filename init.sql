-- ==============================
-- RESET DO BANCO
-- ==============================
DROP DATABASE IF EXISTS universidade;
CREATE DATABASE universidade;
USE universidade;

-- ==============================
-- TABELA: CURSOS
-- ==============================
CREATE TABLE IF NOT EXISTS CURSOS (
    Cod VARCHAR(10) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Depto VARCHAR(100),
    Coord VARCHAR(100)
);

-- ==============================
-- TABELA: ALUNOS (COM CAMPUS)
-- ==============================
CREATE TABLE IF NOT EXISTS ALUNOS (
    Matr INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Sexo CHAR(1) CHECK (Sexo IN ('M','F')),
    Cr VARCHAR(10),
    Campus VARCHAR(50),

    -- CHAVE ESTRANGEIRA (curso)
    FOREIGN KEY (Cr) REFERENCES CURSOS(Cod)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

-- ==============================
-- TABELA: MATRICULAS (COM CHECK EM SEMESTRE)
-- ==============================
CREATE TABLE IF NOT EXISTS MATRICULAS (
    Matr INT,
    Disc VARCHAR(50),
    T INT CHECK (T >= 1),
    Sem VARCHAR(10) CHECK (Sem IN ('2025.1','2025.2','2026.1')),

    -- CHAVE PRIMÁRIA COMPOSTA
    PRIMARY KEY (Matr, Disc, Sem),

    -- CHAVE ESTRANGEIRA
    FOREIGN KEY (Matr) REFERENCES ALUNOS(Matr)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- ==============================
-- INSERINDO CURSOS
-- ==============================
INSERT INTO CURSOS VALUES
('CC', 'Ciencia da Computacao', 'Exatas', 'Joao'),
('SI', 'Sistemas de Informacao', 'Exatas', 'Maria'),
('ADM', 'Administracao', 'Humanas', 'Carlos');

-- ==============================
-- INSERINDO ALUNOS (COM CAMPUS)
-- ==============================
INSERT INTO ALUNOS VALUES
(1, 'Ana', 'F', 'CC', 'Goiania'),
(2, 'Bruno', 'M', 'SI', 'Anapolis'),
(3, 'Carla', 'F', 'CC', 'Uruacu'),
(4, 'Daniel', 'M', 'ADM', 'Goiania'),
(5, 'Eduarda', 'F', 'SI', 'Anapolis'),
(6, 'Felipe', 'M', 'CC', 'Uruacu'),
(7, 'Gabriela', 'F', 'ADM', 'Goiania'),
(8, 'Henrique', 'M', 'SI', 'Anapolis'),
(9, 'Isabela', 'F', 'CC', 'Uruacu'),
(10, 'Joao', 'M', 'ADM', 'Goiania');

-- ==============================
-- INSERINDO MATRICULAS (COM SEMESTRES VARIADOS)
-- ==============================
INSERT INTO MATRICULAS VALUES
-- 2025.1
(1, 'BD', 1, '2025.1'),
(2, 'ENG', 1, '2025.1'),
(3, 'POO', 1, '2025.1'),

-- 2025.2
(1, 'POO', 1, '2025.2'),
(4, 'ADM1', 1, '2025.2'),
(5, 'ENG', 1, '2025.2'),

-- 2026.1
(2, 'BD', 1, '2026.1'),
(3, 'ED', 1, '2026.1'),
(6, 'BD', 1, '2026.1'),
(6, 'ED', 1, '2026.1');

-- ==============================
-- USUÁRIOS
-- ==============================
DROP USER IF EXISTS 'aluno'@'%';
DROP USER IF EXISTS 'professor'@'%';

CREATE USER 'aluno'@'%' IDENTIFIED BY '123';
CREATE USER 'professor'@'%' IDENTIFIED BY '123';

GRANT SELECT ON universidade.* TO 'aluno'@'%';
GRANT SELECT, UPDATE ON universidade.* TO 'professor'@'%';

FLUSH PRIVILEGES;
