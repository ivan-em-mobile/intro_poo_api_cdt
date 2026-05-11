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
import tkinter as tk
from tkinter import messagebox

# --- FUNÇÃO DE LÓGICA (BANCO DE DADOS) ---
def cadastrar_cliente():
    nome = entry_nome.get()  # Captura o que foi digitado na tela
    email = entry_email.get()
    
    if nome == "" or email == "":
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    conexao = sqlite3.connect('exercicio_pratico_BD.db')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)',
                    (nome, email))
    conexao.commit()
    conexao.close()
    
    messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado!")
    entry_nome.delete(0, tk.END) # Limpa o campo após cadastrar
    entry_email.delete(0, tk.END)

# --- ETAPA DE INTERFACE (TKINTER) ---
janela = tk.Tk()
janela.title("Sistema de Gestão - Biblioteca")
janela.geometry("300x250")

# Rótulos e Campos de Entrada
tk.Label(janela, text="Nome do Cliente:").pack(pady=5)
entry_nome = tk.Entry(janela)
entry_nome.pack(pady=5)

tk.Label(janela, text="E-mail:").pack(pady=5)
entry_email = tk.Entry(janela)
entry_email.pack(pady=5)

# Botão de Ação
btn_cadastrar = tk.Button(janela, text="Cadastrar Cliente", 
                          command=cadastrar_cliente)
btn_cadastrar.pack(pady=20)

# Inicia o programa visual
janela.mainloop()