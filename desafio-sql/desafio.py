# criando conexão com o sqlite

import sqlite3

conexao = sqlite3.connect('desafio-sql')

cursor = conexao.cursor()

# 1 - Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).

# cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')


# 2 - Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

# cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1, "João", 25, "Engenharia"), (2, "Maria", 22, "Medicina"), (3, "Pedro", 20, "Economia"), (4, "Ana", 24, "Direito"), (5, "Lucas", 21, "Administração"), (6, "Carolina", 18, "Psicologia"), (7, "André", 19, "Engenharia"), (8, "Felipe", 18, "Arquitetura"), (9, "Mariana", 24, "Biologia"), (10, "Camila", 20, "Jornalismo")')


# 3. Consultas Básicas

# a) Selecionar todos os registros da tabela "alunos".
# dados = cursor.execute('SELECT * FROM alunos')

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
# dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
# dados = cursor.execute('SELECT * FROM alunos WHERE curso == "Engenharia" ORDER BY nome')

# d) Contar o número total de alunos na tabela
# dados = cursor.execute('SELECT COUNT(*) FROM alunos')

#for alunos in dados:
 #   print(alunos)


# 4. Atualização e Remoção

# a) Atualize a idade de um aluno específico na tabela.
# cursor.execute('UPDATE alunos SET idade=28 WHERE nome = "Felipe"')

# b) Remova um aluno pelo seu ID.
# cursor.execute('DELETE FROM alunos WHERE id=7')


# 5. Criar uma Tabela e Inserir Dados - Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

# cursor.execute('CREATE TABLE clientes(id INT primary key, nome VARCHAR(100), idade INT, saldo REAL)')

# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "João da Silva", 35, 500.00), (2, "Maria Oliveira", 28, 1000.00), (3, "Pedro Santos", 45, 750.00), (4, "Ana Costa", 40, 1200.00), (5, "Luiza Pereira", 32, 900.00)')


# 6. Consultas e Funções Agregadas

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
# dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

# b) Calcule o saldo médio dos clientes.
# dados = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')

# c) Encontre o cliente com o saldo máximo
# dados = cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')

# d) Conte quantos clientes têm saldo acima de 1000.
# dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')


# 7. Atualização e Remoção com Condições

# a) Atualize o saldo de um cliente específico.
# cursor.execute('UPDATE clientes SET saldo = 350.90 WHERE nome = "Luiza Pereira"')

# b) Remova um cliente pelo seu ID.
# cursor.execute('DELETE FROM clientes WHERE id=2')

# for clientes in dados:
 #  print(clientes)


# 8. Junção de Tabelas - Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

# Criando tabela
# cursor.execute('CREATE TABLE compras(id INT primary key, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

# Inserindo compras associadas a clientes
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(101, 2, "Camiseta M", 50), (106, 4, "Calça Jeans 42", 79.90), (104, 3, "Tênis Nike", 120), (110, 5, "Relógio", 200), (112, 4, "Celular Samsung", 799.90), (103, 1, "Fone de Ouvindo JBL", 159.80)')

# consultando e exibindo o nome do cliente, produto e valor da compra
dados = cursor.execute('SELECT nome, produto, valor FROM compras INNER JOIN clientes ON compras.cliente_id = clientes.id')

for clientes in dados:
   print(clientes)

# enviando e fechando a conexão
conexao.commit()
conexao.close()
