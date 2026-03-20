CREATE TABLE CURSOS (
    Cod VARCHAR(10) PRIMARY KEY,
    Nome VARCHAR(100),
    Depto VARCHAR(100),
    Coord VARCHAR(100)
);

CREATE TABLE ALUNOS (
    Matr INT PRIMARY KEY,
    Nome VARCHAR(100),
    Sexo CHAR(1),
    Cr VARCHAR(10),
    FOREIGN KEY (Cr) REFERENCES CURSOS(Cod)
);

CREATE TABLE MATRICULAS (
    Matr INT,
    Disc VARCHAR(50),
    T INT,
    Sem VARCHAR(10),
    PRIMARY KEY (Matr, Disc, Sem),
    FOREIGN KEY (Matr) REFERENCES ALUNOS(Matr)
);

INSERT INTO CURSOS VALUES
('CC', 'Ciencia da Computacao', 'Exatas', 'Joao'),
('SI', 'Sistemas de Informacao', 'Exatas', 'Maria'),
('ADM', 'Administracao', 'Humanas', 'Carlos');

INSERT INTO ALUNOS VALUES
(1, 'Ana', 'F', 'CC'),
(2, 'Bruno', 'M', 'SI'),
(3, 'Carla', 'F', 'CC'),
(4, 'Daniel', 'M', 'ADM'),
(5, 'Eduarda', 'F', 'SI'),
(6, 'Felipe', 'M', 'CC'),
(7, 'Gabriela', 'F', 'ADM'),
(8, 'Henrique', 'M', 'SI'),
(9, 'Isabela', 'F', 'CC'),
(10, 'Joao', 'M', 'ADM');

INSERT INTO MATRICULAS VALUES
(1, 'BD', 1, '2026.1'),
(1, 'POO', 1, '2026.1'),
(2, 'BD', 1, '2026.1'),
(2, 'ENG', 1, '2026.1'),
(3, 'POO', 1, '2026.1'),
(3, 'ED', 1, '2026.1'),
(4, 'ADM1', 1, '2026.1'),
(5, 'ENG', 1, '2026.1'),
(6, 'BD', 1, '2026.1'),
(6, 'ED', 1, '2026.1');
