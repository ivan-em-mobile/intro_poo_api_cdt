'''
Docstring para modulo_9-Tratamento de Erro
Este módulo demonstra técnicas de tratamento de 
erro em Python, 
incluindo o uso de blocos try-except, criação de exceções 
personalizadas e boas práticas para
manutenção de código robusto. 
'''

# CÓDIGO COM ERRO (Sem tratamento)
# ----------------------------------
a = 10;
b = 0;
def divisao_simples(a, b):
    print(f"O resultado da divisão é: {a / b}")

# Chamada que irá causar o erro
# divisao_simples(10, 0)

# Ao tentar executar a linha acima, o programa pararia com o seguinte erro:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero