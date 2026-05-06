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

    def verificar_status(self):
        try:
            # 1. Tentamos ler o que o utilizador digita
            entrada = input(f"Quanto de bateria tem o seu {self.modelo}? ")
            
            # 2. Convertemos para número (aqui pode ocorrer o erro!)
            nivel = float(entrada)

            # 3. Lógica de decisão baseada nos teus requisitos
            if nivel < 0 or nivel > 100:
                print("Aviso: Por favor, digite um valor entre 0 e 100.")
            
            elif nivel < 15:
                print(f"⚠️ Bateria em {nivel}%! Por favor, coloque o telemóvel a carregar.")
            
            elif nivel > 85:
                print(f"✅ Bateria em {nivel}%. Está com carga máxima, pronto para uso intenso!")
            
            else:
                print(f"📱 Bateria em {nivel}%. O telemóvel está normal para uso.")

        except ValueError:
            # Captura se o utilizador digitar "dez" em vez de "10"
            print("Erro Crítico: Você não digitou um número válido. Tente novamente.")

# --- Execução ---
meu_celular = Celular("Samsung", "S24")
meu_celular.verificar_status()