class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        print(f"Um animal, {self.nome} ({self.especie}), foi criado.")

    def emitir_som(self):
        print(f"{self.nome} está emitindo um som genérico.")

# Cachorro herda de Animal
class Cachorro(Animal): # Cachorro é a subclasse, Animal é a superclasse
    def __init__(self, nome, raca, idade):
        # Chama o construtor da classe pai (Animal)
        super().__init__(nome, "Cachorro")
        self.raca = raca
        self.idade = idade
        print(f"Um cachorro chamado {self.nome} ({self.raca}) foi criado!")

    # Sobrescreve o método emitir_som da classe Animal
    def emitir_som(self):
        print(f"{self.nome} está latindo: Au Au!")

    def brincar(self):
        print(f"{self.nome} está brincando de pegar a bolinha.")

# CachorroDeServico herda de Cachorro
class CachorroDeServico(Cachorro):
    def __init__(self, nome, raca, idade, funcao):
        # Chama o construtor da classe pai (Cachorro)
        super().__init__(nome, raca, idade)
        self.funcao = funcao
        self.em_servico = False
        print(f"Um cachorro de serviço, {self.nome}, foi treinado para {self.funcao}.")

    # Método específico de CachorroDeServico
    def ativar_servico(self):
        self.em_servico = True
        print(f"{self.nome} agora está em serviço como {self.funcao}.")

    # Sobrescreve o método emitir_som da classe Cachorro (polimorfismo!)
    def emitir_som(self):
        if self.em_servico:
            print(f"{self.nome} está alerta e latindo baixinho para indicar algo.")
        else:
            super().emitir_som() # Chama o latido normal do cachorro

# Criando objetos
animal_generico = Animal("Fred", "Gato")
animal_generico.emitir_som()
print("-" * 30)

carlos = Cachorro("Carlos", "Poodle", 2)
carlos.emitir_som()
carlos.brincar()
print("-" * 30)

policial_k9 = CachorroDeServico("Max", "Pastor Belga Malinois", 4, "busca e resgate")
policial_k9.emitir_som() # Max está latindo: Au Au! (porque ainda não está em serviço)
policial_k9.ativar_servico()
policial_k9.emitir_som() # Max está alerta e latindo baixinho para indicar algo.
policial_k9.brincar() # Max ainda sabe brincar, pois herdou de Cachorro


# Classes do exemplo anterior: Animal, Cachorro, CachorroDeServico

def fazer_barulho(animal):
    """
    Esta função aceita qualquer objeto que seja um Animal (ou uma subclasse de Animal)
    e chama seu método emitir_som.
    """
    animal.emitir_som()

print("--- Demonstrando Polimorfismo ---")

# Criando objetos de diferentes classes
animal_generico_2 = Animal("Piu", "Pássaro")
cachorro_exemplo = Cachorro("Bob", "Beagle", 1)
cachorro_servico_exemplo = CachorroDeServico("Lassie", "Collie", 6, "resgate")

# Lassie ativa o serviço para demonstrar a mudança de comportamento
cachorro_servico_exemplo.ativar_servico()

# Chamando a mesma função 'fazer_barulho' com diferentes tipos de objetos
fazer_barulho(animal_generico_2)       # Piu está emitindo um som genérico.
fazer_barulho(cachorro_exemplo)        # Bob está latindo: Au Au!
fazer_barulho(cachorro_servico_exemplo) # Lassie está alerta e latindo baixinho para indicar algo.

print("\nPerceba que a mesma função 'fazer_barulho' produz resultados diferentes para cada tipo de animal!")