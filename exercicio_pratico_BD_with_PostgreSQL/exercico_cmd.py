import sqlite3

# --- PASSO 1: CONEXÃO E CRIAÇÃO DAS TABELAS ---
# Estabelecemos a conexão com o arquivo de banco de dados
conexao = sqlite3.connect('exercicio_cmd.db')

cursor = conexao.cursor()

# Criamos as tabelas com suporte a Chave Estrangeira (Foreign Key)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
''')
conexao.commit()

print("--- SISTEMA DE GESTÃO DE PEDIDOS ---")

# --- PASSO 2: INSERÇÃO DINÂMICA (ENTRADA DO UTILIZADOR) ---
# Solicitamos dados para a tabela Clientes

nome_usuario = input("Digite o nome do cliente: ")

email_usuario = input("Digite o e-mail do cliente: ")

# Guardamos o ID gerado para usar no pedido
cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', 
               (nome_usuario, email_usuario))
id_cliente_criado = cursor.lastrowid 

conexao.commit()

# Solicitamos dados para a tabela Pedidos usando o ID do cliente acima
produto_nome = input(f"Qual produto o(a) {nome_usuario} está comprando? ")

qtd = int(input("Quantidade: "))

cursor.execute('INSERT INTO pedidos (cliente_id, produto, quantidade) VALUES (?, ?, ?)', 
               (id_cliente_criado, produto_nome, qtd))

conexao.commit()

# --- PASSO 3: CONSULTA COM JOIN ---

def exibir_pedidos():

    print("\n--- LISTA DE PEDIDOS ATUALIZADA ---")

    cursor.execute('''
        SELECT pedidos.id, clientes.nome, pedidos.produto, pedidos.quantidade
        FROM pedidos
        JOIN clientes ON pedidos.cliente_id = clientes.id
    ''')

    for p in cursor.fetchall():

        print(f"ID Pedido: {p[0]} | Cliente: {p[1]} | Produto: {p[2]} | Qtd: {p[3]}")

exibir_pedidos()

# --- PASSO 4: EXCLUSÃO DE UM PEDIDO ---
# O utilizador escolhe qual pedido apagar

id_excluir = input("\nDigite o ID do pedido que deseja excluir (ou Enter para pular): ")

if id_excluir:

    cursor.execute('DELETE FROM pedidos WHERE id = ?', (id_excluir,))

    conexao.commit()

    print(f"Pedido {id_excluir} removido com sucesso.")

# --- PASSO 5: CONSULTA FINAL ---
exibir_pedidos()

# Fechamos a conexão para segurança dos dados
conexao.close()

print("\nSessão finalizada.")