'''
Criando um sistema de cadastro de clientes utilizando POO
 e persistência de dados em arquivo JSON.


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
    """Representa um cliente com seus atributos, incluindo os novos: telefone, email, cpf."""
    # CORREÇÃO: Usando __init__
    def __init__(self, nome, idade, cidade, telefone, email, cpf): 
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.telefone = telefone # Novo atributo
        self.email = email       # Novo atributo
        self.cpf = cpf           # Novo atributo

    def to_dict(self):
        """Converte o objeto Cliente para um dicionário, ideal para JSON."""
        return {
            "nome": self.nome,
            "idade": self.idade,
            "cidade": self.cidade,
            "telefone": self.telefone,
            "email": self.email,
            "cpf": self.cpf
        }
    
    # CORREÇÃO: Usando __str__
    def __str__(self):
        """Método para representação textual do objeto (útil na listagem)."""
        return (f"Nome: {self.nome}, Idade: {self.idade}, Cidade: {self.cidade}, "
                f"Tel: {self.telefone}, Email: {self.email}, CPF: {self.cpf}")
    
    # NOVO MÉTODO: Atualizar dados
    def atualizar_dados(self, nome, idade, cidade, telefone, email, cpf):
        """Atualiza os dados do cliente com os novos valores."""
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        print(f"Dados de '{self.nome}' atualizados.")
    

# CLASSE 2: SISTEMACADASTRO (Gerenciando a Lógica de Negócio e JSON)
class SistemaCadastro:
    """Gerencia a lista de clientes e a persistência em arquivo JSON."""
    
    # CORREÇÃO: Usando __init__
    def __init__(self, arquivo_dados):
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
                # Adicionando tratamento para os novos campos (com valor padrão vazio caso não exista no JSON antigo)
                self.clientes = [
                    Cliente(
                        dado.get('nome'), 
                        dado.get('idade'), 
                        dado.get('cidade'),
                        dado.get('telefone', ''), # Novo campo com valor padrão
                        dado.get('email', ''),    # Novo campo com valor padrão
                        dado.get('cpf', '')       # Novo campo com valor padrão
                    ) 
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

    # Método modificado para receber os novos atributos
    def adicionar_cliente(self, nome, idade, cidade, telefone, email, cpf):
        """Cria e adiciona um novo objeto Cliente à lista e salva."""
        # Cria a instância do objeto Cliente
        novo_cliente = Cliente(nome, idade, cidade, telefone, email, cpf)
        self.clientes.append(novo_cliente)
        self.salvar_dados()
        print(f"\nNovo cliente '{nome}' adicionado!")

    def listar_clientes(self):
        """Exibe todos os clientes cadastrados com seus índices."""
        print("\n--- Clientes Cadastrados ---")
        
        if not self.clientes:
            print("Ainda não há clientes cadastrados.")
            return

        for i, cliente in enumerate(self.clientes, 1):
            # Usa o método __str__ do objeto Cliente para formatar a saída
            print(f"[{i}] {cliente}")
        
        print("-" * 30)

    # NOVO MÉTODO: Atualizar dados do cliente
    def atualizar_cliente(self, indice, nome, idade, cidade, telefone, email, cpf):
        """Localiza e chama o método de atualização do cliente no índice especificado."""
        try:
            # Índices da lista em Python começam em 0, o menu usa índice 1
            cliente_a_atualizar = self.clientes[indice - 1] 
            
            # Chama o método de atualização dentro do objeto Cliente
            cliente_a_atualizar.atualizar_dados(nome, idade, cidade, telefone, email, cpf)
            
            self.salvar_dados()
            
        except IndexError:
            print(f"\n❌ Erro: Não foi encontrado um cliente com o índice {indice}.")
        except Exception as e:
            print(f"\n❌ Erro ao atualizar cliente: {e}")


# FUNÇÕES DE INTERAÇÃO (Interface de Usuário)
def _obter_dados_cliente(modo='cadastro', dados_atuais=None):
    """Solicita e valida a entrada de dados do usuário, agora incluindo os novos campos."""
    print(f"\n--- Entrada de Dados ({modo.capitalize()}) ---")
    
    # Função auxiliar para pegar input com valor padrão
    def _prompt(campo, tipo=str, valor_padrao=''):
        prompt_texto = f"Digite o {campo}"
        if modo == 'atualizacao':
            prompt_texto += f" (Atual: {dados_atuais[campo]} | Deixe vazio para não mudar)"
        prompt_texto += ": "
        
        while True:
            entrada = input(prompt_texto).strip()
            if modo == 'atualizacao' and not entrada:
                return valor_padrao # Retorna o valor atual se vazio na atualização
            
            if tipo is int:
                try:
                    valor = int(entrada)
                    if 0 < valor <= 150:
                        return valor
                    print("Idade inválida (deve ser um número entre 1 e 150).")
                except ValueError:
                    print(f"Entrada inválida. Digite {campo} usando apenas números inteiros.")
            else:
                return entrada
    
    # Se for atualização, usa os dados atuais como padrão
    if modo == 'atualizacao' and dados_atuais:
        nome_padrao = dados_atuais.get('nome', '')
        idade_padrao = dados_atuais.get('idade', 0)
        cidade_padrao = dados_atuais.get('cidade', '')
        telefone_padrao = dados_atuais.get('telefone', '')
        email_padrao = dados_atuais.get('email', '')
        cpf_padrao = dados_atuais.get('cpf', '')
    else:
        nome_padrao = ''
        idade_padrao = 0
        cidade_padrao = ''
        telefone_padrao = ''
        email_padrao = ''
        cpf_padrao = ''


    nome = _prompt("Nome do Cliente", valor_padrao=nome_padrao)
    if modo == 'cadastro' and not nome:
        print("Nome não pode ser vazio. Operação cancelada.")
        return None, None, None, None, None, None
        
    idade = _prompt("Idade do Cliente", tipo=int, valor_padrao=idade_padrao)
    cidade = _prompt("Cidade do Cliente", valor_padrao=cidade_padrao)
    telefone = _prompt("Telefone do Cliente", valor_padrao=telefone_padrao)
    email = _prompt("Email do Cliente", valor_padrao=email_padrao)
    cpf = _prompt("CPF do Cliente", valor_padrao=cpf_padrao)
    
    return nome, idade, cidade, telefone, email, cpf


def menu_principal():
    """Função principal que gerencia o menu e interage com a classe SistemaCadastro."""
    
    # 1. INSTANCIAÇÃO: Cria o objeto gerenciador
    # CORREÇÃO CRÍTICA: Passando o argumento ARQUIVO_DADOS
    sistema = SistemaCadastro(ARQUIVO_DADOS)

    while True:
        print("\n=== Menu do Sistema de Clientes (POO) ===")
        print("1. Adicionar Novo Cliente")
        print("2. Listar Clientes Cadastrados")
        print("3. Atualizar Dados de Cliente") # Nova Opção
        print("4. Sair do Sistema")
        
        opcao = input("Escolha uma opção (1, 2, 3 ou 4): ").strip()
        
        if opcao == '1':
            # Chamada modificada para capturar os novos campos
            nome, idade, cidade, telefone, email, cpf = _obter_dados_cliente(modo='cadastro')
            if nome: # Se a validação do nome for bem-sucedida
                sistema.adicionar_cliente(nome, idade, cidade, telefone, email, cpf)
        
        elif opcao == '2':
            sistema.listar_clientes()
            
        elif opcao == '3': # Nova Opção
            sistema.listar_clientes()
            if not sistema.clientes:
                continue

            try:
                indice = int(input("Digite o NÚMERO do cliente para atualizar (ou 0 para cancelar): "))
                if indice == 0:
                    continue
                
                # Pega os dados atuais do cliente
                cliente_atual = sistema.clientes[indice - 1]
                dados_atuais = cliente_atual.to_dict()
                
                # Obtém os novos dados, usando os atuais como padrão
                nome, idade, cidade, telefone, email, cpf = _obter_dados_cliente(
                    modo='atualizacao', 
                    dados_atuais=dados_atuais
                )
                
                # Chama o método de atualização
                if nome:
                    sistema.atualizar_cliente(indice, nome, idade, cidade, telefone, email, cpf)
                    
            except ValueError:
                print("❌ Entrada inválida. Digite apenas o número (índice) do cliente.")
            except IndexError:
                print("❌ Índice de cliente não encontrado.")

        elif opcao == '4':
            # O sistema já salva automaticamente, mas chamamos para garantir e exibir a mensagem de sucesso.
            sistema.salvar_dados() 
            print("\nObrigado por usar o sistema POO! Encerrando...")
            break
        
        else:
            print("Opção inválida. Por favor, digite 1, 2, 3 ou 4.")


# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal()

