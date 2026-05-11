'''
Criar um banco de dados relacional com SQLite/PostgreSQL e 
desenvolver uma interface de menu para operações completas.

1. Criar o banco de dados chamado "exercicio_pratico_BD.db".

2. Estruturar a tabela "clientes":
   - id (Inteiro, Chave Primária, Autoincremento)
   - nome (Texto, Obrigatório)
   - email (Texto, Obrigatório)

3. Estruturar a tabela "pedidos" (Relacional):
   - id (Inteiro, Chave Primária, Autoincremento)
   - cliente_id (Chave Estrangeira ligada a clientes.id)
   - produto (Texto)
   - quantidade (Inteiro)

4. Implementar um Menu Principal Interativo (Loop While).

5. Criar a função de Cadastro de Clientes (CREATE/INSERT).

6. Criar a função de Cadastro de Pedidos vinculado a um 
Cliente (Relacionamento).

7. Criar consulta de Pedidos com JOIN 
(Para exibir o nome do cliente e não apenas o ID).

8. Implementar a atualização de dados 
(UPDATE) para corrigir produtos ou quantidades.

9. Implementar a exclusão de registros 
(DELETE) de forma específica por ID.

10. Criar sistema de busca flexível utilizando o operador LIKE 
(Busca por nome).

11. Implementar a lógica de Backup automático do banco de dados 
(Cópia de segurança).

12. Consultar registros antes e depois de alterações para 
verificar a integridade.

13. Tratar entradas vazias para evitar erros durante 
a atualização de dados.

14. Utilizar Placeholders (?) para garantir a 
segurança contra SQL Injection.

15. Garantir o encerramento seguro da conexão 
com o banco de dados.

'''

import sqlite3
import shutil 

# --- ETAPA 1: CONFIGURAÇÃO INICIAL ---
conexao = sqlite3.connect('exercicio_cmd.db')
cursor = conexao.cursor()

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

# --- ETAPA 2: FUNÇÕES DE APOIO ---
def listar_pedidos_completo():
    print("\n--- RELATÓRIO DE PEDIDOS ---")
    cursor.execute('''
        SELECT pedidos.id, clientes.nome, pedidos.produto, pedidos.quantidade
        FROM pedidos
        JOIN clientes ON pedidos.cliente_id = clientes.id
    ''')
    dados = cursor.fetchall()
    if not dados:
        print("Nenhum pedido registado.")
    for p in dados:
        print(f"ID: {p[0]} | Cliente: {p[1]} | Produto: {p[2]} | Qtd: {p[3]}")

# --- ETAPA 3: LOOP DO MENU PRINCIPAL ---
while True:
    print("\n==========================")
    print("      MENU PRINCIPAL      ")
    print("==========================")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Pedido")
    print("3. Listar Todos os Pedidos")
    print("4. Excluir um Pedido")
    print("5. Atualizar um Pedido")
    print("6. BUSCAR CLIENTE POR NOME")
    print("7. CRIAR BACKUP DO BANCO")   
    print("0. Sair")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do cliente: ")
        email = input("E-mail do cliente: ")
        cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', (nome, email))
        conexao.commit()
        print(f"Cliente {nome} cadastrado!")

    elif opcao == '2':
        cursor.execute('SELECT id, nome FROM clientes')
        clientes = cursor.fetchall()
        if not clientes:
            print("Erro: Cadastre um cliente primeiro!")
            continue
        print("\nClientes disponíveis:")
        for c in clientes: print(f"ID: {c[0]} | Nome: {c[1]}")
        c_id = input("Digite o ID do cliente: ")
        prod = input("Nome do produto: ")
        qtd = input("Quantidade: ")
        cursor.execute('INSERT INTO pedidos (cliente_id, produto, quantidade) VALUES (?, ?, ?)', (c_id, prod, qtd))
        conexao.commit()
        print("Pedido registado!")

    elif opcao == '3':
        listar_pedidos_completo()

    elif opcao == '4':
        listar_pedidos_completo()
        id_del = input("\nID do pedido para EXCLUIR: ")
        cursor.execute('DELETE FROM pedidos WHERE id = ?', (id_del,))
        conexao.commit()
        print(f"Pedido {id_del} removido!")

    elif opcao == '5':
        listar_pedidos_completo()
        id_upd = input("\nID do pedido para ATUALIZAR: ")
        novo_p = input("Novo produto (vazio para manter): ")
        nova_q = input("Nova qtd (vazio para manter): ")
        if novo_p: cursor.execute('UPDATE pedidos SET produto = ? WHERE id = ?', (novo_p, id_upd))
        if nova_q: cursor.execute('UPDATE pedidos SET quantidade = ? WHERE id = ?', (nova_q, id_upd))
        conexao.commit()
        print("Atualizado!")

    elif opcao == '6':
        # --- BLOCO DE BUSCA ---
        termo = input("Digite o nome (ou parte dele) para buscar: ")
        # O % permite buscar qualquer texto antes ou depois do termo
        cursor.execute('SELECT * FROM clientes WHERE nome LIKE ?', ('%' + termo + '%',))
        resultados = cursor.fetchall()
        print("\n--- RESULTADOS DA BUSCA ---")
        if not resultados:
            print("Nenhum cliente encontrado.")
        for r in resultados:
            print(f"ID: {r[0]} | Nome: {r[1]} | E-mail: {r[2]}")

    elif opcao == '7':
        # --- BLOCO DE BACKUP ---
        try:
            nome_backup = "backup_exercicio_cmd.db"
            shutil.copyfile('exercicio_cmd.db', nome_backup)
            print(f"\nSucesso! Backup criado como: {nome_backup}")
        except Exception as e:
            print(f"Erro ao criar backup: {e}")

    elif opcao == '0':
        print("A encerrar o sistema... Até breve!")
        break
    else:
        print("Opção inválida!")

conexao.close()