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
        self.ligado = True # Vamos começar com ele ligado
        self.bateria = 100 

    def fazer_chamada(self, duracao):
        try:
            # Tenta converter a duração para número (pode dar erro se for texto)
            gasto = int(duracao) * 2 
            
            if self.bateria >= gasto:
                self.bateria -= gasto
                print(f"Chamada de {duracao} min efetuada! Bateria: {self.bateria}%")
            else:
                print("Bateria insuficiente para esta chamada.")

        except ValueError:
            # Se o utilizador passar "muito tempo" em vez de "10"
            print("Erro: A duração da chamada deve ser um número inteiro!")
            
        except TypeError:
            # Se o atributo bateria estiver corrompido (ex: for uma string)
            print("Erro crítico: O sistema de bateria encontrou um erro de tipo.")
            
        except Exception as e:
            # Qualquer outro erro inesperado
            print(f"Ocorreu um erro desconhecido: {e}")

# --- IMPLEMENTAÇÃO ---
meu_celular = Celular("Samsung", "S24")

# Teste com erro de valor (mandando uma letra onde devia ser número)
meu_celular.fazer_chamada("15")