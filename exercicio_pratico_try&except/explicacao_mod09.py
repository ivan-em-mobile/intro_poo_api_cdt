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
def aula_tratamento_erros():
    print("--- Início da Aula de Exceções ---")
    
    try:
        # 1. Tentamos obter dados do utilizador
        numerador = int(input("Digita o numerador (número em cima): "))
        denominador = int(input("Digita o denominador (número em baixo): "))
        
        # 2. Tentamos realizar a operação
        resultado = numerador / denominador

    except ValueError:
        # Este bloco corre se o utilizador digitar algo que não seja um número inteiro
        print("Erro: Por favor, digita apenas números inteiros!")

    except ZeroDivisionError:
        # Este bloco corre se o denominador for zero
        print("Erro: Matemática básica! Não pode dividir um número por zero.")

    except Exception as erro:
        # Este é um 'apanha-tudo' para erros inesperados
        print(f"Ocorreu um erro inesperado: {erro}")

    else:
        # Só corre se o bloco 'try' NÃO disparar nenhum erro
        print(f"Sucesso! O resultado da divisão é: {resultado}")

    finally:
        # Corre SEMPRE, independentemente de ter havido erro ou não
        print("--- Fim da operação de tratamento ---")

# Executar a função
aula_tratamento_erros()