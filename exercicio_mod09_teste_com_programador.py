'''
# Aula de Tratamento de Erros em Python

exception é um termo técnico para um erro que ocorre durante a execução de um programa. 
Em Python, podemos usar blocos `try`, `except`, `else` e `finally` para lidar com esses erros de forma elegante 
e evitar que o programa quebre inesperadamente.

try (Tentar): Coloca aqui apenas o código que pode falhar. Não coloques o programa inteiro aqui dentro, 
apenas a parte sensível (cálculos, inputs, conexões).

except (Exceção): É como um filtro. Podes ter vários. O ValueError serve para problemas de tipo de dado, 
e o ZeroDivisionError é específico para divisões impossíveis.

as erro: Usamos isto para guardar a mensagem oficial do sistema numa variável, caso queiras mostrar exatamente 
o que o Python diz que correu mal.

finally: Muito usado em níveis avançados para fechar ficheiros ou bases de dados, 
garantindo que os recursos não ficam "presos" se o programa falhar.

 ##Como testar:
 
Teste 1: Digita 10 e 2. O programa deve mostrar o resultado e saltar para o finally.

Teste 2: Digita 10 e 0. Vais ver a mensagem personalizada sobre divisão por zero.

Teste 3: Digita dez e 2. Vais ver o erro de valor.

'''
class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = True
        self.bateria = 100

    def fazer_chamada(self, custo_bateria):
        print(f"\n--- Iniciando chamada no {self.modelo} ---")
        
        try:
            # PASSO 1: Tentar fazer a conta
            # Se 'custo_bateria' não for um número, o Python gera um erro aqui!
            self.bateria -= custo_bateria
            
        except TypeError:
            # PASSO 2: Capturar o erro se o valor for inválido (ex: uma letra)
            print("ERRO: Você tentou usar um valor que não é um número!")
            print("Dica: Use números inteiros para o custo da bateria.")
            
        else:
            # PASSO 3: Se a conta deu certo, avisamos o utilizador
            print(f"Chamada concluída com sucesso!")
            print(f"Bateria restante: {self.bateria}%")
            
        finally:
            # PASSO 4: Acontece sempre (bom para logs ou fechar processos)
            print("Sistema de chamadas finalizado.")

# --- TESTANDO NA PRÁTICA ---

meu_celular = Celular("Samsung", "S24")

# CASO 1: Tudo certo (passando o número 10)
meu_celular.fazer_chamada(10)

# CASO 2: Erro propositado (passando uma palavra em vez de número)
meu_celular.fazer_chamada("muito")