'''
Explicação do código:
Este código define uma API para gerenciar clientes usando o framework FastAPI. 
Ele inclui operações CRUD (Criar, Ler, Atualizar, Deletar) para clientes, 
utilizando um banco de dados SQLite para armazenamento dos dados. 
A API permite listar todos os clientes, obter detalhes de um cliente específico, 
criar novos clientes, atualizar informações de clientes existentes e deletar clientes. 
O código também inclui tratamento de erros para garantir que operações inválidas 
sejam corretamente gerenciadas.from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

'''
# app.py (Salve com este nome, como minha sugestão)

from fastapi import FastAPI, HTTPException # Importa FastAPI e HTTPException para erros
from pydantic import BaseModel             # Importa BaseModel para definir a estrutura dos dados
import sqlite3                             # Importa o módulo para interagir com o SQLite
from typing import List, Optional          # Importa tipos de dados avançados
import uvicorn                             # Importa o servidor web ASGI

# --- 1. Configuração e Inicialização ---
DATABASE = 'clientes.db'
app = FastAPI(title="API de Gerenciamento de Clientes") # Cria a instância da aplicação

# Definição do Modelo de Dados (Pydantic)
class Cliente(BaseModel):
    # 'Optional[int] = None' significa que o ID é opcional (quando estamos criando um cliente)
    id: Optional[int] = None
    nome: str
    email: str
    telefone: str

# Função para inicializar o banco de dados (cria a tabela se não existir)
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Executa a função de inicialização na hora que o script é carregado
init_db()

# --- 2. Rotas da API (Endpoints) ---

# Rota para LISTAR TODOS os clientes (GET)
@app.get("/clientes/", response_model=List[Cliente])
def listar_clientes():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, telefone FROM clientes")
    rows = cursor.fetchall()
    conn.close()
    # Converte as tuplas do banco de dados para o modelo Cliente
    return [Cliente(id=row[0], nome=row[1], email=row[2], telefone=row[3]) for row in rows]

# Rota para OBTER UM cliente por ID (GET)
@app.get("/clientes/{cliente_id}", response_model=Cliente)
def obter_cliente(cliente_id: int):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # O '?' é um placeholder para evitar ataques de injeção SQL
    cursor.execute("SELECT id, nome, email, telefone FROM clientes WHERE id = ?", (cliente_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Cliente(id=row[0], nome=row[1], email=row[2], telefone=row[3])
    else:
        # Se não encontrar, retorna um erro HTTP 404 (Não Encontrado)
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

# Rota para CRIAR um novo cliente (POST)
@app.post("/clientes/", response_model=Cliente)
def criar_cliente(cliente: Cliente):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
                   (cliente.nome, cliente.email, cliente.telefone))
    conn.commit()
    # Obtém o ID que foi gerado automaticamente
    cliente.id = cursor.lastrowid
    conn.close()
    return cliente

# Rota para ATUALIZAR um cliente (PUT)
@app.put("/clientes/{cliente_id}", response_model=Cliente)
def atualizar_cliente(cliente_id: int, cliente: Cliente): 
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nome = ?, email = ?, telefone = ? WHERE id = ?",
                   (cliente.nome, cliente.email, cliente.telefone, cliente_id))
    conn.commit()
    
    # Verifica se alguma linha foi realmente atualizada
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    conn.close()
    cliente.id = cliente_id
    return cliente

# Rota para DELETAR um cliente (DELETE)
@app.delete("/clientes/{cliente_id}")
def deletar_cliente(cliente_id: int):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
    conn.commit()
    
    # Verifica se alguma linha foi realmente deletada
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    conn.close()
    # Retorna uma mensagem de sucesso
    return {"detail": "Cliente deletado com sucesso"}

# --- 3. Execução do Servidor (Opcional, mas útil para testes) ---
# Este bloco permite que você execute o arquivo diretamente com 'python app.py'
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)