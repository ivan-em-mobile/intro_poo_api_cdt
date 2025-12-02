'''
#atributos -> Dados
##falta os seguintes atributos: telefone, email, cpf
##falta os seguintes métodos: atualizar dados do cliente
classe -> Clientes [nome, idade,cidade]
SistemaCadastro -> inserir; listar; excluir.mod_08_cads_clientes.py

'''

import json
import os

# --- Configurações de Persistência ---
PASTA_DADOS = "dados"
ARQUIVO_DADOS = os.path.join(PASTA_DADOS, "clientes.json")


# CLASSE 1: CLIENTE (Modelando a Entidade de Dados)
class Cliente:
    """Representa um cliente com seus atributos básicos."""
    def _init_(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def to_dict(self):
        """Converte o objeto Cliente para um dicionário, ideal para JSON."""
        return {
            "nome": self.nome,
            "idade": self.idade,
            "cidade": self.cidade
        }
    
    def _str_(self):
        """Método para representação textual do objeto (útil na listagem)."""
        return f"Nome: {self.nome}, Idade: {self.idade}, Cidade: {self.cidade}"
    

# CLASSE 2: SISTEMACADASTRO (Gerenciando a Lógica de Negócio e JSON)
class SistemaCadastro:
    """Gerencia a lista de clientes e a persistência em arquivo JSON."""
    
    def _init_(self, arquivo_dados):
        self.arquivo_dados = arquivo_dados
        self.clientes = [] # Armazena objetos Cliente
        self._carregar_dados() # Carrega dados automaticamente ao inicializar o sistema

    def _carregar_dados(self):
        """Carrega os dados do JSON. Método interno (por isso o '_')."""
        pasta = os.path.dirname(self.arquivo_dados)
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            print(f"Pasta '{pasta}' criada.")
            
        try:
            with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                dados_json = json.load(f)
                
                # Transforma cada dicionário lido do JSON de volta em um objeto Cliente
                self.clientes = [
                    Cliente(dado['nome'], dado['idade'], dado['cidade']) 
                    for dado in dados_json
                ]
                print(f"Dados carregados. Total de clientes: {len(self.clientes)}")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Arquivo JSON não encontrado ou vazio. Iniciando um novo cadastro.")
            self.clientes = []

    def salvar_dados(self):
        """Salva a lista de objetos Cliente no arquivo JSON."""
        try:
            # Converte a lista de objetos Cliente em uma lista de dicionários
            dados_para_salvar = [cliente.to_dict() for cliente in self.clientes]
            
            with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
                json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)
            print(f"\n✅ Dados salvos com sucesso em '{self.arquivo_dados}'.")
        except Exception as e:
            print(f"\n❌ Erro ao salvar dados: {e}")

    def adicionar_cliente(self, nome, idade, cidade):
        """Cria e adiciona um novo objeto Cliente à lista e salva."""
        # Cria a instância do objeto Cliente
        novo_cliente = Cliente(nome, idade, cidade)
        self.clientes.append(novo_cliente)
        self.salvar_dados()
        print(f"\nNovo cliente '{nome}' adicionado!")

    def listar_clientes(self):
        """Exibe todos os clientes cadastrados."""
        print("\n--- Clientes Cadastrados ---")
        
        if not self.clientes:
            print("Ainda não há clientes cadastrados.")
            return

        for i, cliente in enumerate(self.clientes, 1):
            # Usa o método _str_ do objeto Cliente para formatar a saída
            print(f"{i}. {cliente}")
        
        print("-" * 30)

# FUNÇÕES DE INTERAÇÃO (Interface de Usuário)
def _obter_dados_cliente():
    """Solicita e valida a entrada de dados do usuário."""
    print("\n--- Entrada de Dados ---")
    
    nome = input("Digite o Nome do Cliente: ").strip()
    if not nome:
        print("Nome não pode ser vazio. Operação cancelada.")
        return None, None, None

    while True:
        try:
            idade = int(input("Digite a Idade do Cliente: "))
            if 0 < idade <= 150:
                break
            print("Idade inválida.")
        except ValueError:
            print("Entrada inválida. Digite a idade usando apenas números inteiros.")

    cidade = input("Digite a Cidade do Cliente: ").strip()
    
    return nome, idade, cidade


def menu_principal():
    """Função principal que gerencia o menu e interage com a classe SistemaCadastro."""
    
    # 1. INSTANCIAÇÃO: Cria o objeto gerenciador
    # sistema = SistemaCadastro(ARQUIVO_DADOS)
    sistema = SistemaCadastro()

    while True:
        print("\n=== Menu do Sistema de Clientes (POO) ===")
        print("1. Adicionar Novo Cliente")
        print("2. Listar Clientes Cadastrados")
        print("3. Sair do Sistema")
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()
        
        if opcao == '1':
            nome, idade, cidade = _obter_dados_cliente()
            if nome: # Se a validação do nome for bem-sucedida
                sistema.adicionar_cliente(nome, idade, cidade)
        elif opcao == '2':
            sistema.listar_clientes()
        elif opcao == '3':
            # O sistema já salva automaticamente, mas chamamos para garantir e exibir a mensagem de sucesso.
            sistema.salvar_dados() 
            print("\nObrigado por usar o sistema POO! Encerrando...")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")


# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal()