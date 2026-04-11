-- ==============================
-- USAR O BANCO
-- ==============================
USE universidade;

-- ==============================
-- EXCLUINDO TABELAS
-- ==============================
DROP VIEW IF EXISTS alunos_global;
DROP TABLE IF EXISTS alunos_goiania;
DROP TABLE IF EXISTS alunos_anapolis;
DROP TABLE IF EXISTS alunos_uruacu;

-- ==============================
-- FRAGMENTAÇÃO HORIZONTAL
-- ==============================

CREATE TABLE alunos_goiania AS
SELECT * FROM ALUNOS
WHERE Campus = 'Goiania';

CREATE TABLE alunos_anapolis AS
SELECT * FROM ALUNOS
WHERE Campus = 'Anapolis';

CREATE TABLE alunos_uruacu AS
SELECT * FROM ALUNOS
WHERE Campus = 'Uruacu';

-- ==============================
-- VISÃO GLOBAL
-- ==============================

CREATE VIEW alunos_global AS
SELECT * FROM alunos_goiania
UNION
SELECT * FROM alunos_anapolis
UNION
SELECT * FROM alunos_uruacu;