"""
its_my_dog, como nome orginal do arquivo
com o intuito de demonstrar POO por uma 
explicação de classe - animal(dog).
"""

# Definindo a classe Cachorro
class Cachorro:
    # O método __init__ é um construtor.
    
    # Ele é chamado automaticamente quando criamos um novo objeto (instância) da classe.
    
    # 'self' se refere ao próprio objeto que está sendo criado.
    
    def __init__(self, nome, raca, idade):
        self.nome = nome     # Atributo: nome do cachorro
        self.raca = raca     # Atributo: raça do cachorro
        self.idade = idade   # Atributo: idade do cachorro
        
        print(f"Um novo cachorro chamado {self.nome} foi criado!")

    # Método: comportamento do cachorro
    
    def latir(self):
        print(f"{self.nome} está latindo: Au Au!")

    # Método: comportamento do cachorro
    
    def comer(self, comida):
        print(f"{self.nome} está comendo {comida}.")
        
    #Método: brincar como cachorro

    def brincar(self, bola):
        print(f"O cachorro está brincando com a {bola}")
    

# Criando objetos (instâncias) da classe Cachorro

meu_cachorro = Cachorro("Buddy", "Golden Retriever", 3)

outro_cachorro = Cachorro("Rex", "Pastor Alemão", 5)

mais_cachorro = Cachorro("Totô", "Dachshund", 8)

print("-" * 30)

# Acessando atributos dos objetos

print(f"Meu cachorro se chama {meu_cachorro.nome} e tem {meu_cachorro.idade} anos.")

print(f"O outro cachorro é da raça {outro_cachorro.raca}.")

print(f"E esse cachorro é da raça {mais_cachorro.raca}.")

print("-" * 30)

# Chamando métodos dos objetos

meu_cachorro.latir()

outro_cachorro.comer("ração de frango")

mais_cachorro.brincar("bola de borracha")

# Buddy agora tem 4 anos (modificando um atributo)

meu_cachorro.idade = 4

print(f"Ops! {meu_cachorro.nome} fez aniversário e agora tem {meu_cachorro.idade} anos.")