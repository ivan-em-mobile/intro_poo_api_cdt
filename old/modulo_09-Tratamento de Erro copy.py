'''
Docstring para modulo_9-Tratamento de Erro
Este módulo demonstra técnicas de tratamento de 
erro em Python, 
incluindo o uso de blocos try-except, criação de exceções 
personalizadas e boas práticas para
manutenção de código robusto. 
'''

# CÓDIGO COM TRATAMENTO BÁSICO
# -----------------------------
def divisao_segura(a, b):
    # 1. Tente (try) executar este código
    try:
        resultado = a / b
        print(f"✅ O resultado da divisão é: {resultado}")
    
    # 2. Se (except) ocorrer um erro específico (ZeroDivisionError), faça isso
    except ZeroDivisionError:
        print("⚠️ ERRO: Não é possível dividir por zero! Por favor, use um divisor diferente de zero.")

# Testes
divisao_segura(10, 2)  # Saída normal: 5.0
divisao_segura(10, 0)  # Saída tratada: ERRO...