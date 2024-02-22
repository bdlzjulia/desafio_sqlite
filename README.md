# Exercício da semana 5 - Banco de dados SQL

Neste exercício, trabalhei com a criação de tabelas, inserção de dados, consultas básicas, atualização, remoção, uso de funções agregadas e junção de tabelas em um banco de dados relacional. 

## Passo a passo do exercício:

- A. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
     
- B. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

<img src="./assets_sql/exercicio_1_2.png"/>

     
- C. Consultas Básicas
  - Escreva consultas SQL para realizar as seguintes tarefas:
     - Selecionar todos os registros da tabela "alunos".
<img src="./assets_sql/exercicio_3A.png" />
     - Selecionar o nome e a idade dos alunos com mais de 20 anos.
<img src="./assets_sql/exercicio_3B.png" />
     - Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
<img src="./assets_sql/exercicio_3C.png" />
     - Contar o número total de alunos na tabela
<img src="./assets_sql/exercicio_3D.png" />
       
- D. Atualização e Remoção
  - Atualize a idade de um aluno específico na tabela.
<img src="./assets_sql/exercicio_4A.png" />
  - Remova um aluno pelo seu ID.
    
- E. Criar uma Tabela e Inserir Dados
  - Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float).
  - Insira alguns registros de clientes na tabela.
<img src="./assets_sql/exercicio_5.png" />
    
- F. Consultas e Funções Agregadas
     Escreva consultas SQL para realizar as seguintes tarefas:
     - Selecione o nome e a idade dos clientes com idade superior a 30 anos.
<img src="./assets_sql/exercicio_6A.png" />
     - Calcule o saldo médio dos clientes.
<img src="./assets_sql/exercicio_6B.png" />
     - Encontre o cliente com o saldo máximo.
<img src="./assets_sql/exercicio_6C.png" />
     - Conte quantos clientes têm saldo acima de 1000.
<img src="./assets_sql/exercicio_6D.png" />
       
- G. Atualização e Remoção com Condições
  - Atualize o saldo de um cliente específico.
<img src="./assets_sql/exercicio_7A.png" />
  - Remova um cliente pelo seu ID.
    
- H. Junção de Tabelas
  - Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real).
    Insira algumas compras associadas a clientes existentes na tabela "clientes".Escreva uma consulta para exibir o nome do cliente, o produto e ovalor de cada compra.

- Criando a tabela:
<img src="./assets_sql/exercicio_8A.png" />

- Consultando a tabela e exibindo o nome do cliente, o produto e ovalor de cada compra:
  <img src="./assets_sql/exercicio_8B.png" />
