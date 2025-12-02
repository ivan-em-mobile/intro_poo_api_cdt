"""
Exercicio de POO, com o intuito de demonstrar a herança e polimorfismo em POO. 
Para isso, vamos criar um jogo de RPG do universo Harry Potter.
"""

# --- Classe Base: Personagem ---
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        print(f"{self.nome} (Vida: {self.vida}, Ataque: {self.ataque}) apareceu no mundo!")

    def atacar(self, alvo):
        """Método para o personagem atacar um alvo."""
        dano = self.ataque
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano!")
        print(f"{alvo.nome} agora tem {alvo.vida} de vida.")
        if alvo.vida <= 0:
            alvo.morrer()

    def morrer(self):
        """Método chamado quando o personagem morre."""
        print(f"{self.nome} foi derrotado!")

# --- Classes Derivadas (Herança): Jogador, Monstro ---

class Jogador(Personagem):
    def __init__(self, nome, vida, ataque, classe_jogador, nivel=1):
        super().__init__(nome, vida, ataque)
        self.classe_jogador = classe_jogador
        self.nivel = nivel
        self.experiencia = 0
        self.inventario = [] # Lista para guardar itens
        print(f"O jogador {self.nome}, um {self.classe_jogador}, começou sua jornada!")

    def ganhar_experiencia(self, pontos_exp):
        """Aumenta a experiência do jogador e verifica se ele subiu de nível."""
        self.experiencia += pontos_exp
        print(f"{self.nome} ganhou {pontos_exp} pontos de experiência!")
        if self.experiencia >= self.nivel * 100: # Exemplo simples de level up
            self.nivel += 1
            self.vida += 20 # Aumenta vida ao subir de nível
            self.ataque += 5 # Aumenta ataque ao subir de nível
            print(f"Parabéns! {self.nome} subiu para o Nível {self.nivel}!")
            print(f"Vida atual: {self.vida}, Ataque atual: {self.ataque}")
            self.experiencia = 0 # Reseta experiência para o próximo nível

    def coletar_item(self, item):
        """Adiciona um item ao inventário do jogador."""
        self.inventario.append(item)
        print(f"{self.nome} coletou {item.nome}.")

    def exibir_inventario(self):
        """Exibe os itens no inventário do jogador."""
        if self.inventario:
            print(f"Inventário de {self.nome}:")
            for item in self.inventario:
                item.exibir_info()
        else:
            print(f"O inventário de {self.nome} está vazio.")

class Monstro(Personagem):
    def __init__(self, nome, vida, ataque, tipo_monstro, recompensa_exp):
        super().__init__(nome, vida, ataque)
        self.tipo_monstro = tipo_monstro
        self.recompensa_exp = recompensa_exp
        print(f"Um {self.tipo_monstro} chamado {self.nome} espreita...")

    def rugir(self):
        """Método específico para monstros."""
        print(f"O {self.nome} ruge ameaçadoramente!")

    def morrer(self):
        """Sobrescreve o método morrer para monstros."""
        print(f"O {self.nome} ({self.tipo_monstro}) foi derrotado e desintegrou-se!")

# --- Classe para Itens ---
class Item:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def exibir_info(self):
        """Exibe informações do item."""
        print(f"- {self.nome}: {self.descricao}")

# --- Interagindo no Jogo de RPG ---
print("--- Começando a Aventura RPG! ---")
print("-" * 40)

# Criando personagens
heroi = Jogador("Artur", 100, 15, "Guerreiro")
goblin = Monstro("Goblin Fedorento", 50, 10, "Goblin", 30)
dragao = Monstro("Ignis, o Dragão", 500, 50, "Dragão", 500)

print("\n--- Primeiro Encontro: Artur vs Goblin ---")
heroi.atacar(goblin)
goblin.rugir()

# Loop de combate simples
while heroi.vida > 0 and goblin.vida > 0:
    if goblin.vida > 0: # Goblin só ataca se estiver vivo
        goblin.atacar(heroi)
    if heroi.vida > 0: # Herói só ataca se estiver vivo
        heroi.atacar(goblin)

    if goblin.vida <= 0:
        heroi.ganhar_experiencia(goblin.recompensa_exp)
        break # Sai do loop se o goblin morrer

print("-" * 40)

# Criando alguns itens
pocao_vida = Item("Poção de Vida Menor", "Restaura 30 de vida.")
espada_ferro = Item("Espada de Ferro", "Uma espada básica de combate.")

# Herói coleta itens
heroi.coletar_item(pocao_vida)
heroi.coletar_item(espada_ferro)
heroi.exibir_inventario()

print("-" * 40)

print("\n--- Encontro Lendário: Artur vs Dragão ---")
# Resetando vida do herói para nova batalha
heroi.vida = 100 + (heroi.nivel - 1) * 20 # Ajusta vida para o nível atual

# Demonstração de polimorfismo com ataque
def confronto(atacante, defensor):
    """Uma função genérica para simular um confronto."""
    print(f"\nConfronto iniciado entre {atacante.nome} e {defensor.nome}!")
    atacante.atacar(defensor)
    if defensor.vida > 0:
        defensor.atacar(atacante)
    else:
        print(f"{defensor.nome} foi derrotado antes de poder reagir.")

confronto(heroi, dragao) # Herói ataca o dragão
print("-" * 40)
confronto(dragao, heroi) # Dragão ataca o herói

# ... (o combate continuaria até um deles ser derrotado)