'''
##Atividade desafio, criar um sistema de cadastro de clientes utilizando POO
#  e persistência de dados em arquivo JSON.

##Explicação
#atributos -> Dados
##falta os seguintes atributos: telefone, email, cpf
##falta os seguintes métodos: atualizar dados do cliente
classe -> Clientes [nome, idade,cidade]
SistemaCadastro -> inserir; listar; excluir.mod_08_cads_clientes.py

'''

import json

ARQUIVO_DADOS = "clientes_data.json"

class Cliente:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def to_dict(self):
        return {"nome": self.nome, "idade": self.idade, "cidade": self.cidade}

class SistemaCadastro:
    def __init__(self, arquivo_dados):
        self.arquivo_dados = arquivo_dados
        self.clientes = self._carregar_dados()

    def _carregar_dados(self):
        try:
            with open(self.arquivo_dados, 'r') as f:
                dados = json.load(f)
                return [Cliente(**d) for d in dados]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def salvar_dados(self):
        dados_para_salvar = [cliente.to_dict() for cliente in self.clientes]
        with open(self.arquivo_dados, 'w') as f:
            json.dump(dados_para_salvar, f, indent=4)

    def adicionar_cliente(self, nome, idade, cidade):
        novo_cliente = Cliente(nome, idade, cidade)
        self.clientes.append(novo_cliente)
        self.salvar_dados()
        print(f"Cliente '{nome}' adicionado e dados salvos.")

    def listar_clientes(self):
        if not self.clientes:
            print("\nNenhum cliente cadastrado.")
            return

        print("\n--- Lista de Clientes ---")
        for i, cliente in enumerate(self.clientes, 1):
            print(f"{i}. Nome: {cliente.nome}, Idade: {cliente.idade}, Cidade: {cliente.cidade}")
        print("-------------------------")


def _obter_dados_cliente():
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
    sistema = SistemaCadastro(ARQUIVO_DADOS)

    while True:
        print("\n=== Menu do Sistema de Clientes (POO) ===")
        print("1. Adicionar Novo Cliente")
        print("2. Listar Clientes Cadastrados")
        print("3. Remover Cliente, por nome ")#(não implementado)
        print("9. Sair do Sistema")
        
        opcao = input("Escolha uma opção (1, 2, 3 ou 9): ").strip()
        
        if opcao == '1':
            nome, idade, cidade = _obter_dados_cliente()
            if nome:
                sistema.adicionar_cliente(nome, idade, cidade)
        elif opcao == '2':
            sistema.listar_clientes()
        elif opcao == '9':
            sistema.salvar_dados()
            print("\nObrigado por usar o sistema POO! Encerrando...")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2, ou 9.")

if __name__ == "__main__":
    menu_principal()