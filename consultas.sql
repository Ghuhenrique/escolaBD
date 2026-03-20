-- Consulta 1:

SELECT Nome FROM ALUNOS WHERE Cr = 'CC';

-- ALGEBRA RELACIONAL:
-- πNome(σCr='CC'(ALUNOS))

-- EXPLICAÇÃO:
-- Primeiro filtramos os alunos que pertencem ao curso CC (σ).
-- Depois selecionamos apenas o atributo Nome (π), retornando só os nomes.

-- Consulta 2:

SELECT Nome FROM ALUNOS WHERE Sexo = 'F' AND Cr = 'CC';

-- ALGEBRA RELACIONAL:
-- πNome(σSexo='F' ∧ Cr='CC'(ALUNOS))

-- EXPLICAÇÃO:
-- Filtramos apenas as alunas (Sexo = F) que estão no curso CC.
-- Depois projetamos apenas os nomes.

-- Consulta 3:

SELECT A.Nome, C.Nome
FROM ALUNOS A
JOIN CURSOS C ON A.Cr = C.Cod;

-- ALGEBRA RELACIONAL:
-- πALUNOS.Nome, CURSOS.Nome (ALUNOS ▷◁Cr=Cod CURSOS)

-- EXPLICAÇÃO:
-- Primeiro fazemos uma junção entre ALUNOS e CURSOS usando Cr = Cod.
-- Depois selecionamos apenas o nome do aluno e o nome do curso.

-- Consulta 4:

SELECT DISTINCT A.Nome
FROM ALUNOS A
JOIN MATRICULAS M ON A.Matr = M.Matr
WHERE M.Sem = '2026.1';

-- ALGEBRA RELACIONAL:
-- πNome(σSem='2026.1'(ALUNOS ▷◁Matr=MATRICULAS.Matr MATRICULAS))

-- EXPLICAÇÃO:
-- Relacionamos alunos com suas matrículas (junção).
-- Filtramos apenas as do semestre 2026.1 e retornamos os nomes.

-- Consulta 5:

SELECT A.Nome, M.Disc
FROM ALUNOS A
JOIN MATRICULAS M ON A.Matr = M.Matr
WHERE M.Sem = '2026.1';

-- ALGEBRA RELACIONAL:
-- πALUNOS.Nome, MATRICULAS.Disc 
-- (σSem='2026.1'(ALUNOS ▷◁Matr=MATRICULAS.Matr MATRICULAS))

-- EXPLICAÇÃO:
-- Primeiro juntamos alunos e matrículas.
-- Depois filtramos pelo semestre e exibimos nome + disciplina.
