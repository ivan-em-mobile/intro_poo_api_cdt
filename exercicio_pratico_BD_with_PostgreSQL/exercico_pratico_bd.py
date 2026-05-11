'''
Criando um banco de dados com PostgreSQL e realizando 
operações básicas utilizando o comando SQL.

1. Criar um banco de dados chamado "exercicio_pratico_BD.db".

2. Criar uma tabela chamada "clientes" com os seguintes campos:

    - id (inteiro, chave primária)
    - nome (texto)
    - email (texto)
3. Inserir alguns registros na tabela "clientes".

4. Consultar todos os registros da tabela "clientes".

5. Atualizar o email de um cliente específico.

6. Excluir um cliente específico da tabela "clientes".

7. Consultar novamente todos os registros da tabela "clientes" 
para verificar as alterações.

8. Criar uma tabela chamada "pedidos" com os seguintes campos:
    - id (inteiro, chave primária)
    - cliente_id (inteiro, chave estrangeira referenciando clientes.id)
    - produto (texto)
    - quantidade (inteiro)

9. Inserir alguns registros na tabela "pedidos".

10. Consultar todos os pedidos, incluindo o nome do cliente 
associado a cada pedido.
11. Atualizar a quantidade de um pedido específico.

12. Excluir um pedido específico da tabela "pedidos".

13. Consultar novamente todos os pedidos para verificar as alterações.

'''
# Importar a biblioteca para trabalhar com PostgreSQL, 
# já vem instalada no Python

import sqlite3

# Conectar ao banco de dados (ou criar se não existir), 
# podemos usar o nome do banco de dados que desejamos criar. 
# E trocar o nome do banco de dados para "exercicio_pratico_BD.db" 
# para seguir o enunciado. E trocar conn por conexao para 
# seguir a convenção de nomeação.

#conexao = sqlite3.connect('exercicio_pratico_BD.db')

conn = sqlite3.connect('exercicio_pratico_BD.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar a tabela "clientes"
# O comando SQL para criar a tabela "clientes" é o seguinte:
# CREATE TABLE IF NOT EXISTS clientes (
#     id INTEGER PRIMARY KEY,
#     nome TEXT NOT NULL,
#     email TEXT NOT NULL
# );

# O comando "IF NOT EXISTS" é usado para evitar erros caso a 
# tabela já exista.

# Executar o comando SQL para criar a tabela "clientes"
#
cursor.execute('''

    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )

''')
# Inserir alguns registros na tabela "clientes"
# O comando SQL para inserir um registro na tabela "clientes" 
# é o seguinte:
# INSERT INTO clientes (nome, email) VALUES ('Nome do Cliente', 
# 'email@dominio.com')
# Podemos usar o método "execute" para inserir registros na tabela
# clientes. E usar o método "commit" para salvar as alterações no 
# banco de dados.

cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES 
    ('João Silva', 'joao.silva@mail.com'),
    ('Maria Oliveira', 'maria.oliveira@mail.com'),
    ('Carlos Santos', 'carlos.santos@mail.com')

''')

conn.commit()

# Consultar todos os registros da tabela "clientes"
# O comando SQL para consultar todos os registros da tabela 
# "clientes" é o seguinte:SELECT * FROM clientes 

cursor.execute('SELECT * FROM clientes')

# O método "fetchall" retorna todos os registros da consulta 
# em forma de lista de tuplas.

## Temos aqui um exemplo de como imprimir os registros de 
# forma mais legível, mas para seguir o enunciado, 
# vamos apenas imprimir o resultado da consulta diretamente. 
# Mas não é um metodo recomendado para produção, pois pode 
# ser difícil de ler e interpretar os dados.

#print(cursor.fetchall()) ## Metodo recomendado para produção, pois pode ser 
# difícil de ler e interpretar os dados.

# Para seguir o enunciado, vamos apenas imprimir o resultado 
# da consulta diretamente, mas para isso, precisamos armazenar 
# o resultado da consulta em uma variável, para depois imprimir.

clientes = cursor.fetchall()

print("Clientes:")
for cliente in clientes:
    print(cliente)

# Atualizar o email de um cliente específico
# O comando SQL para atualizar o email de um cliente específico é o seguinte:
# UPDATE clientes SET email = 'novo_email@dominio.com' WHERE id = 1;

cursor.execute('''

    UPDATE clientes SET email = 'novo_email@dominio.com' WHERE id = 1

''')

conn.commit()

# Excluir um cliente específico da tabela "clientes"
# O comando SQL para excluir um cliente específico da tabela "clientes" é o seguinte:
# DELETE FROM clientes WHERE id = 2;

cursor.execute('''

    DELETE FROM clientes WHERE id = 2

''')
conn.commit()
# Consultar novamente todos os registros da tabela "clientes" para verificar as alterações

cursor.execute('SELECT * FROM clientes')

clientes = cursor.fetchall()

print("Clientes após as alterações:")
for cliente in clientes:
    print(cliente)

# Criar a tabela "pedidos"
# O comando SQL para criar a tabela "pedidos" é o seguinte:
# CREATE TABLE IF NOT EXISTS pedidos (
#     id INTEGER PRIMARY KEY,
#     cliente_id INTEGER,
#     produto TEXT NOT NULL,
#     quantidade INTEGER NOT NULL,
#     FOREIGN KEY (cliente_id) REFERENCES clientes(id)
# );
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY,
        cliente_id INTEGER,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )

''')

# Inserir alguns registros na tabela "pedidos"
# O comando SQL para inserir um registro na tabela "pedidos" é o seguinte:
# INSERT INTO pedidos (cliente_id, produto, quantidade) VALUES (1, 'Produto A', 2);

cursor.execute('''
    INSERT INTO pedidos (cliente_id, produto, quantidade) VALUES (1, 'Produto A', 2)
''')
conn.commit()

# Consultar todos os pedidos, incluindo o nome do cliente associado a cada pedido
# O comando SQL para consultar todos os pedidos, incluindo o nome do cliente 
# associado a cada pedido é o seguinte:
# SELECT pedidos.id, clientes.nome, pedidos.produto, pedidos.quantidade
# FROM pedidos
# JOIN clientes ON pedidos.cliente_id = clientes.id;

cursor.execute('''
    SELECT pedidos.id, clientes.nome, pedidos.produto, pedidos.quantidade
    FROM pedidos
    JOIN clientes ON pedidos.cliente_id = clientes.id
''')

pedidos = cursor.fetchall()

print("Pedidos:")
for pedido in pedidos:
    print(pedido)

# Atualizar a quantidade de um pedido específico
# O comando SQL para atualizar a quantidade de um pedido específico é o seguinte:
# UPDATE pedidos SET quantidade = 5 WHERE id = 1;

cursor.execute('''
    UPDATE pedidos SET quantidade = 5 WHERE id = 1
''')

conn.commit()

# Agora como contuniar o código para excluir um pedido específico da tabela 
# "pedidos" e consultar novamente todos os pedidos para verificar as alterações?