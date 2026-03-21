import mysql.connector

# ==============================
# CONEXÃO COM O BANCO
# ==============================
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="universidade"
    )

    cursor = conexao.cursor()
    print("Conectado ao banco com sucesso!\n")

except Exception as e:
    print("Erro ao conectar:", e)
    exit()

# ==============================
# 1. TRANSAÇÃO COM COMMIT
# ==============================
print("=== TESTE DE COMMIT ===")
try:
    conexao.start_transaction()

    # Usa um aluno que EXISTE (ex: 1)
    cursor.execute("""
        INSERT INTO MATRICULAS (Matr, Disc, T, Sem)
        VALUES (%s, %s, %s, %s)
    """, (1, "BD", 1, "2026.2"))

    conexao.commit()
    print("Matrícula inserida com sucesso!\n")

except Exception as e:
    conexao.rollback()
    print("Erro (rollback executado):", e, "\n")

# ==============================
# 2. TESTE DE ROLLBACK (ERRO)
# ==============================
print("=== TESTE DE ROLLBACK ===")
try:
    conexao.start_transaction()

    cursor.execute("""
        INSERT INTO MATRICULAS (Matr, Disc, T, Sem)
        VALUES (%s, %s, %s, %s)
    """, (2, "BD", 1, "2026.2"))

    # ERRO proposital
    cursor.execute("UPDATE MATRICULAS SET coluna_errada = 10")

    conexao.commit()

except Exception as e:
    conexao.rollback()
    print("Rollback executado com sucesso!")
    print("Erro capturado:", e, "\n")

# ==============================
# 3. LISTA DE ALUNOS
# ==============================
print("=== LISTA DE ALUNOS ===")
cursor.execute("SELECT * FROM ALUNOS")
for aluno in cursor.fetchall():
    print(aluno)
print()

# ==============================
# 4. LISTA DE DISCIPLINAS
# ==============================
print("=== LISTA DE DISCIPLINAS ===")
cursor.execute("SELECT DISTINCT Disc FROM MATRICULAS")
for disc in cursor.fetchall():
    print(disc)
print()

# ==============================
# 5. MATRÍCULAS POR SEMESTRE
# ==============================
print("=== MATRÍCULAS POR SEMESTRE ===")
semestre = input("Digite o semestre (ex: 2026.1): ")

cursor.execute("""
    SELECT * FROM MATRICULAS
    WHERE Sem = %s
""", (semestre,))

resultados = cursor.fetchall()

if resultados:
    for m in resultados:
        print(m)
else:
    print("Nenhuma matrícula encontrada para esse semestre.")
print()

# ==============================
# 6. CONSULTA DE MATRÍCULAS POR ALUNO
# ==============================
print("=== CONSULTA POR ALUNO ===")
matricula_aluno = input("Digite a matrícula do aluno: ")

cursor.execute("""
    SELECT A.Nome, M.Disc, M.Sem
    FROM ALUNOS A
    JOIN MATRICULAS M ON A.Matr = M.Matr
    WHERE A.Matr = %s
""", (matricula_aluno,))

resultados = cursor.fetchall()

if resultados:
    print("\nMatrículas do aluno:")
    for r in resultados:
        print(r)
else:
    print("Nenhuma matrícula encontrada para esse aluno.")
print()

# ==============================
# 7. CANCELAMENTO DE MATRÍCULA
# ==============================
print("=== CANCELAMENTO DE MATRÍCULA ===")
try:
    conexao.start_transaction()

    cursor.execute("""
        DELETE FROM MATRICULAS
        WHERE Matr = %s AND Disc = %s
    """, (1, "BD"))

    conexao.commit()
    print("Matrícula cancelada com sucesso!\n")

except Exception as e:
    conexao.rollback()
    print("Erro ao cancelar matrícula:", e)

# ==============================
# ENCERRAMENTO
# ==============================
cursor.close()
conexao.close()
print("Conexão encerrada.")