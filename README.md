# Sistema Acadêmico com Banco de Dados Distribuído

Este projeto foi desenvolvido no contexto da disciplina de Banco de Dados II, com o objetivo de aplicar, de forma prática, conceitos fundamentais de bancos de dados distribuídos, tais como fragmentação, replicação, controle de concorrência e transações.

A proposta consiste na modelagem e implementação de um sistema acadêmico, utilizando MySQL em ambiente Docker, com organização estruturada e execução de operações reais sobre os dados.

---

## Objetivos

O projeto tem como principal objetivo demonstrar a aplicação prática dos seguintes conceitos:

* Fragmentação horizontal de dados
* Replicação de tabelas
* Criação de visões globais
* Controle de acesso a usuários
* Transações com commit e rollback
* Simulação de ambiente distribuído

---

## Estrutura do Projeto

O projeto foi organizado seguindo boas práticas de desenvolvimento, separando responsabilidades em diretórios distintos:

```
escolaBD/
│
├── README.md
├── docker-compose.yml
├── .gitignore
│
├── sql/
│   ├── init.sql
│   ├── distribuido.sql
│   ├── consultas.sql
│
├── src/
│   └── transacoes.py
│
├── docs/
│   ├── respostas.md
│   ├── listas e materiais em PDF
```

---

## Modelagem do Banco de Dados

O banco de dados `universidade` é composto pelas seguintes tabelas principais:

* CURSOS: armazena informações sobre os cursos
* ALUNOS: contém dados dos alunos, incluindo o campus
* MATRICULAS: registra as matrículas dos alunos nas disciplinas

A tabela `ALUNOS` foi estendida com o atributo `Campus`, permitindo a aplicação de fragmentação horizontal.

---

## Fragmentação Horizontal

A fragmentação foi realizada com base no atributo `Campus`, resultando nas seguintes tabelas:

* alunos_goiania
* alunos_anapolis
* alunos_uruacu

Cada tabela armazena apenas os alunos pertencentes ao respectivo campus, reduzindo o custo de acesso e melhorando o desempenho em um ambiente distribuído.

---

## Visão Global

Foi criada uma visão global denominada `alunos_global`, que reúne todos os fragmentos por meio da operação `UNION ALL`.

Essa abordagem garante transparência ao usuário, permitindo consultas como se os dados estivessem centralizados.

---

## Replicação

A tabela de disciplinas pode ser replicada em todos os nós do sistema, garantindo maior disponibilidade e redução no tempo de resposta para consultas.

---

## Controle de Acesso

Foram definidos dois tipos de usuários no banco de dados:

* aluno: possui apenas permissão de leitura (SELECT)
* professor: possui permissões de leitura e atualização (SELECT, UPDATE)

Essa divisão garante maior segurança e controle sobre os dados.

---

## Transações

O sistema implementa transações com controle de:

* Commit: confirmação das operações
* Rollback: reversão em caso de erro

Além disso, são discutidos conceitos de transações distribuídas e o uso do protocolo Two-Phase Commit (2PC).

---

## Como Executar o Projeto

### 1. Subir o container do banco de dados

```
docker-compose up -d
```

### 2. Executar o script de inicialização

```
docker exec -i mysql_algebra mysql -u root -proot < sql/init.sql
```

### 3. Executar a fragmentação

```
docker exec -i mysql_algebra mysql -u root -proot universidade < sql/distribuido.sql
```

---

## Testes

Após a execução, é possível validar o funcionamento com os seguintes comandos:

```
USE universidade;

SELECT * FROM ALUNOS;
SELECT * FROM alunos_goiania;
SELECT * FROM alunos_global;
```

---

## Conceitos Aplicados

Este projeto aborda, na prática, os seguintes conceitos:

* Propriedades ACID
* Fragmentação de dados
* Replicação
* Controle de concorrência
* Transações distribuídas
* Integridade referencial

---

## Autor

Gustavo Henrique Costa Pinto
Projeto desenvolvido para fins acadêmicos na disciplina de Banco de Dados II.

