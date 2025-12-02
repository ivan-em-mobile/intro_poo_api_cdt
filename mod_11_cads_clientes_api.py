'''
Explicação do código:
Este código implementa um sistema de cadastro de clientes utilizando o paradigma de Programação Orientada a Objetos (POO) em Python, 
com integração a APIs externas para enriquecer os dados dos clientes. O sistema permite adicionar, listar e atualizar informações dos clientes, 
armazenando esses dados em um arquivo JSON para persistência.
Além disso, o sistema integra-se com a API ViaCEP para obter automaticamente dados de endereço a partir do CEP fornecido pelo usuário,
e com a API OpenWeatherMap para exibir o clima atual da cidade do cliente durante a listagem.

Principais componentes do código:
1. Classe Cliente: Representa um cliente com atributos como nome, idade, cidade, telefone, email, CPF e endereço. 
Inclui métodos para converter o objeto em dicionário,
   atualizar dados e validar o CPF.
2. Classe SistemaCadastro: Gerencia a lista de clientes, incluindo métodos para carregar e salvar dados em JSON,
   adicionar novos clientes, listar clientes (com dados de clima) e atualizar informações dos clientes.
    Também inclui métodos para consultar as APIs ViaCEP e OpenWeatherMap.
3. Funções de Interação: Fornecem uma interface de usuário simples via console para interagir com o sistema,
   incluindo a obtenção e validação de dados do cliente.
'''

import json
import os
import requests # NOVO: Biblioteca para requisições HTTP (APIs)

# --- Configurações de Persistência ---
PASTA_DADOS = "dados"
ARQUIVO_DADOS = os.path.join(PASTA_DADOS, "clientes.json")

# --- Configurações da API de Clima ---
# SUBSTITUA PELA SUA CHAVE REAL DA API OpenWeatherMap
OPENWEATHER_API_KEY = "SUA_API_KEY_AQUI" 
OPENWEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"


# CLASSE 1: CLIENTE (Modelando a Entidade de Dados)
class Cliente:
    """Representa um cliente com seus atributos, incluindo os novos: telefone, email, cpf e endereço."""
    
    def __init__(self, nome, idade, cidade, telefone, email, cpf, endereco=""): 
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.telefone = telefone
        self.email = email       
        self.cpf = cpf           
        self.endereco = endereco # NOVO atributo
        
    def to_dict(self):
        """Converte o objeto Cliente para um dicionário, ideal para JSON."""
        return {
            "nome": self.nome,
            "idade": self.idade,
            "cidade": self.cidade,
            "telefone": self.telefone,
            "email": self.email,
            "cpf": self.cpf,
            "endereco": self.endereco
        }
    
    def __str__(self):
        """Método para representação textual do objeto (útil na listagem)."""
        detalhes = f"Nome: {self.nome}, Idade: {self.idade}, Cidade: {self.cidade}"
        contato = f"Tel: {self.telefone}, Email: {self.email}, CPF: {self.cpf}"
        endereco = f"Endereço: {self.endereco or 'Não informado'}"
        return f"{detalhes}\n\t{contato}\n\t{endereco}"
    
    # NOVO MÉTODO: Atualizar dados (atualizado para incluir 'endereco')
    def atualizar_dados(self, nome, idade, cidade, telefone, email, cpf, endereco):
        """Atualiza os dados do cliente com os novos valores."""
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.endereco = endereco
        print(f"Dados de '{self.nome}' atualizados.")

    # NOVO MÉTODO ESTÁTICO: Validação Algorítmica do CPF
    @staticmethod
    def validar_cpf(cpf):
        """Verifica a validade do CPF através do algoritmo."""
        cpf = ''.join(filter(str.isdigit, str(cpf)))
        if not cpf or len(cpf) != 11 or len(set(cpf)) == 1:
            return False
        
        # Cálculo do primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        digito_1 = 11 - (soma % 11)
        digito_1 = 0 if digito_1 > 9 else digito_1
        
        # Validação do primeiro dígito
        if int(cpf[9]) != digito_1:
            return False
        
        # Cálculo do segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        digito_2 = 11 - (soma % 11)
        digito_2 = 0 if digito_2 > 9 else digito_2
        
        # Validação do segundo dígito
        if int(cpf[10]) != digito_2:
            return False
            
        return True

# CLASSE 2: SISTEMACADASTRO (Gerenciando a Lógica de Negócio e JSON/APIs)
class SistemaCadastro:
    """Gerencia a lista de clientes e a persistência em arquivo JSON, e as integrações com APIs."""
    
    def __init__(self, arquivo_dados):
        self.arquivo_dados = arquivo_dados
        self.clientes = []
        self._carregar_dados()

    def _carregar_dados(self):
        """Carrega os dados do JSON, ajustado para o novo campo 'endereco'."""
        pasta = os.path.dirname(self.arquivo_dados)
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            print(f"Pasta '{pasta}' criada.")
            
        try:
            with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                dados_json = json.load(f)
                
                self.clientes = [
                    Cliente(
                        dado.get('nome'), 
                        dado.get('idade'), 
                        dado.get('cidade'),
                        dado.get('telefone', ''),
                        dado.get('email', ''),
                        dado.get('cpf', ''),
                        dado.get('endereco', '') # Novo campo
                    ) 
                    for dado in dados_json
                ]
                print(f"Dados carregados. Total de clientes: {len(self.clientes)}")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Arquivo JSON não encontrado ou vazio. Iniciando um novo cadastro.")
            self.clientes = []

    def salvar_dados(self):
        """Salva a lista de objetos Cliente no arquivo JSON."""
        # ... (Mantido o código de salvar) ...
        try:
            dados_para_salvar = [cliente.to_dict() for cliente in self.clientes]
            
            with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
                json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)
            print(f"\n✅ Dados salvos com sucesso em '{self.arquivo_dados}'.")
        except Exception as e:
            print(f"\n❌ Erro ao salvar dados: {e}")

    # Método modificado para aceitar o novo atributo 'endereco'
    def adicionar_cliente(self, nome, idade, cidade, telefone, email, cpf, endereco):
        """Cria e adiciona um novo objeto Cliente à lista e salva."""
        novo_cliente = Cliente(nome, idade, cidade, telefone, email, cpf, endereco)
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
            print(f"[{i}] {cliente}")
            # NOVO: Tenta obter e exibir o clima da cidade do cliente
            if cliente.cidade:
                clima = self.obter_clima_cidade(cliente.cidade)
                print(f"\tClima em {cliente.cidade}: {clima}")
            else:
                print("\tClima: Cidade não informada.")
        
        print("-" * 30)

    def atualizar_cliente(self, indice, nome, idade, cidade, telefone, email, cpf, endereco):
        """Localiza e chama o método de atualização do cliente no índice especificado."""
        try:
            cliente_a_atualizar = self.clientes[indice - 1] 
            cliente_a_atualizar.atualizar_dados(nome, idade, cidade, telefone, email, cpf, endereco)
            self.salvar_dados()
        except IndexError:
            print(f"\n❌ Erro: Não foi encontrado um cliente com o índice {indice}.")
        except Exception as e:
            print(f"\n❌ Erro ao atualizar cliente: {e}")

    # NOVO MÉTODO: Integração com ViaCEP
    def buscar_dados_por_cep(self, cep):
        """Consulta a API ViaCEP para obter dados de endereço."""
        url = f"https://viacep.com.br/ws/{cep}/json/"
        print(f"Consultando CEP: {url}")
        try:
            response = requests.get(url, timeout=5) # Timeout de 5 segundos
            response.raise_for_status() # Lança exceção para erros HTTP (4xx ou 5xx)
            dados = response.json()
            
            if dados.get('erro'):
                print("⚠️ CEP não encontrado pela API.")
                return None
            
            return {
                'cidade': dados.get('localidade'),
                'endereco': f"{dados.get('logradouro')} - {dados.get('bairro')}/{dados.get('uf')}"
            }
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro na comunicação com a API ViaCEP: {e}")
            return None

    # NOVO MÉTODO: Integração com OpenWeatherMap
    def obter_clima_cidade(self, cidade):
        """Consulta a API OpenWeatherMap para obter o clima de uma cidade."""
        if OPENWEATHER_API_KEY == "SUA_API_KEY_AQUI":
            return "Chave da API de Clima não configurada."
            
        params = {
            'q': cidade,
            'appid': OPENWEATHER_API_KEY,
            'units': 'metric', # Para temperatura em Celsius
            'lang': 'pt_br'
        }
        try:
            response = requests.get(OPENWEATHER_URL, params=params, timeout=5)
            response.raise_for_status()
            dados = response.json()
            
            temperatura = dados['main']['temp']
            descricao = dados['weather'][0]['description']
            
            return f"{descricao.capitalize()}, {temperatura:.1f}°C"
            
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                return "Cidade não encontrada na API de Clima."
            return f"Erro HTTP ao buscar clima: {e}"
        except requests.exceptions.RequestException as e:
            return f"Erro de conexão ao buscar clima: {e}"
        except Exception:
            return "Erro ao processar dados do clima."


# FUNÇÕES DE INTERAÇÃO (Interface de Usuário)
def _obter_dados_cliente(sistema_cadastro, modo='cadastro', dados_atuais=None):
    """Solicita e valida a entrada de dados do usuário, agora com CEP e CPF."""
    
    print(f"\n--- Entrada de Dados ({modo.capitalize()}) ---")
    
    # ... (Função auxiliar _prompt mantida/adaptada) ...
    def _prompt(campo, tipo=str, valor_padrao=''):
        prompt_texto = f"Digite o {campo}"
        if modo == 'atualizacao':
            # Adaptação para campos com acento na chave do dicionário
            chave_campo = campo.split()[0].lower() if 'endereço' not in campo.lower() else 'endereco'
            if chave_campo == 'cpf': chave_campo = 'cpf'

            prompt_texto += f" (Atual: {dados_atuais.get(chave_campo, '')} | Deixe vazio para não mudar)"
        prompt_texto += ": "
        
        while True:
            entrada = input(prompt_texto).strip()
            if modo == 'atualizacao' and not entrada:
                # Retorna o valor atual
                if campo == 'Idade': return dados_atuais.get('idade', 0)
                if campo == 'Nome': return dados_atuais.get('nome', '')
                if campo == 'Cidade': return dados_atuais.get('cidade', '')
                if campo == 'Telefone': return dados_atuais.get('telefone', '')
                if campo == 'Email': return dados_atuais.get('email', '')
                if campo == 'CPF': return dados_atuais.get('cpf', '')
                if campo == 'Endereço': return dados_atuais.get('endereco', '')
            
            if not entrada and modo == 'cadastro':
                return '' # Permite vazio no cadastro, exceto Nome e CPF

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
    # ... (Fim da função auxiliar) ...
    
    # 1. Obtenção dos Dados
    nome = _prompt("Nome do Cliente")
    if modo == 'cadastro' and not nome:
        print("Nome não pode ser vazio. Operação cancelada.")
        return None, None, None, None, None, None, None
        
    idade = _prompt("Idade do Cliente", tipo=int)
    telefone = _prompt("Telefone do Cliente")
    email = _prompt("Email do Cliente")

    # 2. Obtenção e Validação do CPF
    cpf_valido = False
    cpf = ''
    while not cpf_valido:
        cpf = _prompt("CPF do Cliente")
        if not cpf: break # Permite sair se vazio na atualização
        if Cliente.validar_cpf(cpf):
            cpf_valido = True
        else:
            print("❌ CPF inválido! Por favor, digite um CPF válido.")
            if modo == 'atualizacao': break
    
    # 3. Obtenção do Endereço (Priorizando CEP)
    cep_valido = False
    cep = input("Digite o CEP (opcional, ou deixe vazio): ").strip()

    cidade = ''
    endereco = ''

    if cep:
        dados_cep = sistema_cadastro.buscar_dados_por_cep(cep)
        if dados_cep:
            cidade = dados_cep['cidade']
            endereco = dados_cep['endereco']
            print(f"✅ Endereço preenchido: {cidade} - {endereco}")
            cep_valido = True

    # Se não usou CEP ou falhou, pede a cidade/endereço manualmente
    if not cep_valido and modo == 'atualizacao':
        cidade_padrao = dados_atuais.get('cidade', '')
        endereco_padrao = dados_atuais.get('endereco', '')
    elif not cep_valido and modo == 'cadastro':
        cidade_padrao = ''
        endereco_padrao = ''
    
    if not cep_valido:
        # Pede cidade e endereço separadamente, usando o padrão na atualização
        cidade = _prompt("Cidade do Cliente", valor_padrao=cidade_padrao)
        endereco = _prompt("Endereço Completo", valor_padrao=endereco_padrao)


    return nome, idade, cidade, telefone, email, cpf, endereco


def menu_principal():
    """Função principal que gerencia o menu e interage com a classe SistemaCadastro."""
    
    sistema = SistemaCadastro(ARQUIVO_DADOS)

    while True:
        print("\n=== Menu do Sistema de Clientes (POO com APIs) ===")
        print("1. Adicionar Novo Cliente")
        print("2. Listar Clientes Cadastrados (tempo real)")
        print("3. Atualizar Dados de Cliente")
        print("4. Sair do Sistema")
        
        opcao = input("Escolha uma opção (1, 2, 3 ou 4): ").strip()
        
        if opcao == '1':
            nome, idade, cidade, telefone, email, cpf, endereco = _obter_dados_cliente(sistema, modo='cadastro')
            if nome: # Se a validação do nome for bem-sucedida
                sistema.adicionar_cliente(nome, idade, cidade, telefone, email, cpf, endereco)
        
        elif opcao == '2':
            sistema.listar_clientes()
            
        elif opcao == '3':
            sistema.listar_clientes()
            if not sistema.clientes: continue

            try:
                indice = int(input("Digite o NÚMERO do cliente para atualizar (ou 0 para cancelar): "))
                if indice == 0: continue
                
                cliente_atual = sistema.clientes[indice - 1]
                dados_atuais = cliente_atual.to_dict()
                
                nome, idade, cidade, telefone, email, cpf, endereco = _obter_dados_cliente(
                    sistema,
                    modo='atualizacao', 
                    dados_atuais=dados_atuais
                )
                
                if nome:
                    sistema.atualizar_cliente(indice, nome, idade, cidade, telefone, email, cpf, endereco)
                    
            except ValueError:
                print("❌ Entrada inválida. Digite apenas o número (índice) do cliente.")
            except IndexError:
                print("❌ Índice de cliente não encontrado.")

        elif opcao == '4':
            sistema.salvar_dados() 
            print("\nObrigado por usar o sistema POO com APIs! Encerrando...")
            break
        
        else:
            print("Opção inválida. Por favor, digite 1, 2, 3 ou 4.")


# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal()