"""
Exercicio de POO, com o intuito de demonstrar a herança e polimorfismo em POO. 
Para isso, vamos criar uma loja de produtos do universo Harry Potter.
"""

# --- Classe Base: ProdutoHogwarts ---
class ProdutoHogwarts:
    def __init__(self, nome, preco, ano_lancamento, unidade_monetaria="Galeões"):
        self.nome = nome
        self.preco = preco
        self.ano_lancamento = ano_lancamento
        self.unidade_monetaria = unidade_monetaria
        print(f"Produto '{self.nome}' criado com sucesso!")

    def exibir_info(self):
        """Exibe as informações básicas do produto."""
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco} {self.unidade_monetaria}")
        print(f"Lançamento: {self.ano_lancamento}")

    def aplicar_desconto(self, percentual):
        """Aplica um desconto ao preço do produto."""
        if 0 < percentual <= 100:
            self.preco -= self.preco * (percentual / 100)
            print(f"Desconto de {percentual}% aplicado! Novo preço: {self.preco:.2f} {self.unidade_monetaria}")
        else:
            print("Percentual de desconto inválido. Use um valor entre 1 e 100.")

# --- Classes Derivadas (Herança): Livros, Varinhas, Poções ---

class Livro(ProdutoHogwarts):
    def __init__(self, nome, preco, ano_lancamento, autor, casa_associada=None):
        super().__init__(nome, preco, ano_lancamento) # Chama o construtor da classe pai
        self.autor = autor
        self.casa_associada = casa_associada # Ex: Grifinória, Sonserina, etc.

    def exibir_info(self):
        """Sobrescreve o método para adicionar informações de livro."""
        super().exibir_info() # Chama a exibição de info do ProdutoHogwarts
        print(f"Autor: {self.autor}")
        if self.casa_associada:
            print(f"Casa Associada: {self.casa_associada}")

    def ler_trecho(self):
        """Método específico para livros."""
        print(f"Lendo um trecho de '{self.nome}': 'Era uma vez, em um castelo mágico...'")

class Varinha(ProdutoHogwarts):
    def __init__(self, nome, preco, ano_lancamento, madeira, nucleo, tamanho_cm):
        super().__init__(nome, preco, ano_lancamento)
        self.madeira = madeira
        self.nucleo = nucleo
        self.tamanho_cm = tamanho_cm

    def exibir_info(self):
        """Sobrescreve o método para adicionar informações de varinha."""
        super().exibir_info()
        print(f"Madeira: {self.madeira}")
        print(f"Núcleo: {self.nucleo}")
        print(f"Tamanho: {self.tamanho_cm} cm")

    def acender_luz(self):
        """Método específico para varinhas."""
        print(f"'{self.nome}' brilha com 'Lumos'!")

class Pocao(ProdutoHogwarts):
    def __init__(self, nome, preco, ano_lancamento, efeito, duracao_horas):
        super().__init__(nome, preco, ano_lancamento)
        self.efeito = efeito
        self.duracao_horas = duracao_horas

    def exibir_info(self):
        """Sobrescreve o método para adicionar informações de poção."""
        super().exibir_info()
        print(f"Efeito: {self.efeito}")
        print(f"Duração: {self.duracao_horas} horas")

    def beber(self):
        """Método específico para poções."""
        print(f"Você bebe a poção '{self.nome}'. Sente um efeito de {self.efeito}!")

# --- Criando e interagindo com os produtos da Loja ---
print("--- Produtos Disponíveis na Loja Hogwarts ---")
print("-" * 40)

# Criando instâncias dos produtos
livro_pedra = Livro("Harry Potter e a Pedra Filosofal", 35.99, 1997, "J.K. Rowling", "Grifinória")
varinha_sabugueiro = Varinha("Varinha das Varinhas (Réplica)", 250.00, 2011, "Sabugueiro", "Pelo de Testrálio", 38)
pocao_felix = Pocao("Felix Felicis", 150.00, 2005, "Sorte Extrema", 12)

# Exibindo informações de cada produto (Polimorfismo em ação!)
print("\n--- Informações Detalhadas dos Produtos ---")
livro_pedra.exibir_info()
livro_pedra.ler_trecho()
livro_pedra.aplicar_desconto(10) # Aplica um desconto
print("-" * 40)

varinha_sabugueiro.exibir_info()
varinha_sabugueiro.acender_luz()
print("-" * 40)

pocao_felix.exibir_info()
pocao_felix.beber()
print("-" * 40)

# --- Exemplo de Polimorfismo: Processando diferentes produtos ---
print("\n--- Verificando Estoque e Preço (Polimorfismo Genérico) ---")
def verificar_estoque_e_preco(produto):
    """Função que aceita qualquer ProdutoHogwarts e exibe seu nome e preço."""
    print(f"Verificando: {produto.nome} - Preço: {produto.preco} {produto.unidade_monetaria}")

verificar_estoque_e_preco(livro_pedra)
verificar_estoque_e_preco(varinha_sabugueiro)
verificar_estoque_e_preco(pocao_felix)