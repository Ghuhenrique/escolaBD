import mysql.connector
import os

# ==============================
# CONFIGURAÇÕES
# ==============================
CONTAINER_NAME = "mysql_algebra"
DB_NAME = "universidade"
DB_USER = "root"
DB_PASSWORD = "root"

# ==============================
# CONEXÃO COM O BANCO
# ==============================
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
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
# 2. TESTE DE ROLLBACK
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
# 3. TRANSAÇÃO COM CONCORRÊNCIA (FOR UPDATE)
# ==============================
print("=== TRANSAÇÃO COM CONTROLE DE CONCORRÊNCIA ===")

try:
    conexao.start_transaction()

    matr = 1
    disc = "BD"

    cursor.execute("""
        SELECT * FROM ALUNOS
        WHERE Matr = %s
        FOR UPDATE
    """, (matr,))

    aluno = cursor.fetchone()

    if not aluno:
        raise Exception("Aluno não existe")

    cursor.execute("""
        SELECT * FROM MATRICULAS
        WHERE Matr = %s AND Disc = %s
    """, (matr, disc))

    if cursor.fetchone():
        raise Exception("Aluno já matriculado nessa disciplina")

    cursor.execute("""
        INSERT INTO MATRICULAS (Matr, Disc, T, Sem)
        VALUES (%s, %s, %s, %s)
    """, (matr, disc, 1, "2026.2"))

    conexao.commit()
    print("Matrícula realizada com segurança!\n")

except Exception as e:
    conexao.rollback()
    print("Erro:", e, "\n")

# ==============================
# 4. LISTA DE ALUNOS
# ==============================
print("=== LISTA DE ALUNOS ===")
cursor.execute("SELECT * FROM ALUNOS")
for aluno in cursor.fetchall():
    print(aluno)
print()

# ==============================
# 5. LISTA DE DISCIPLINAS
# ==============================
print("=== LISTA DE DISCIPLINAS ===")
cursor.execute("SELECT DISTINCT Disc FROM MATRICULAS")
for disc in cursor.fetchall():
    print(disc)
print()

# ==============================
# 6. MATRÍCULAS POR SEMESTRE
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
# 7. CONSULTA POR ALUNO
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
# 8. CANCELAMENTO DE MATRÍCULA
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
# 9. BACKUP DO BANCO
# ==============================
print("=== BACKUP DO BANCO ===")

backup_cmd = f"docker exec {CONTAINER_NAME} mysqldump -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > backup.sql"

if os.system(backup_cmd) == 0:
    print("Backup realizado com sucesso!\n")
else:
    print("Erro ao fazer backup.\n")

# ==============================
# 10. RESTAURAÇÃO DO BANCO
# ==============================
print("=== RESTAURAÇÃO DO BANCO ===")

restaurar = input("Deseja restaurar o banco? (s/n): ")

if restaurar.lower() == 's':
    restore_cmd = f"docker exec -i {CONTAINER_NAME} mysql -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} < backup.sql"

    if os.system(restore_cmd) == 0:
        print("Banco restaurado com sucesso!\n")
    else:
        print("Erro ao restaurar.\n")

# ==============================
# ENCERRAMENTO
# ==============================
cursor.close()
conexao.close()
print("Conexão encerrada.")