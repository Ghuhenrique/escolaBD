# Projeto Banco de Dados com Docker

## Como rodar

1. Clone o repositório
2. Execute:

docker-compose up -d

3. Acesse:

docker exec -it mysql_algebra mysql -u root -p

Senha: root

4. Rode consultas:

USE universidade;
SELECT * FROM ALUNOS;
