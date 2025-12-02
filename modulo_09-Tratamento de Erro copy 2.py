'''
Docstring para modulo_9-Tratamento de Erro
Este módulo demonstra técnicas de tratamento de 
erro em Python, 
incluindo o uso de blocos try-except, criação de exceções 
personalizadas e boas práticas para
manutenção de código robusto. 
'''

'''
Docstring para modulo_9-Tratamento de Erro
Este módulo demonstra técnicas de tratamento de 
erro em Python, 
incluindo o uso de blocos try-except, criação de exceções 
personalizadas e boas práticas para
manutenção de código robusto. 
'''

# CÓDIGO TRATANDO MÚLTIPLOS ERROS
# -------------------------------
def divisao_multi_segura(a, b):
    try:
        num1 = int(a)  # Tenta garantir que 'a' é um número
        num2 = int(b)  # Tenta garantir que 'b' é um número
        resultado = num1 / num2
        print(f"✅ O resultado da divisão é: {resultado}")
        
    # Captura a ZeroDivisionError e a ValueError em um só bloco
    except (ZeroDivisionError, ValueError):
        print("⚠️ ERRO: Certifique-se de que o divisor não é zero e de que ambos " \
        "os valores são números válidos.")
    
    # É possível também pegar a mensagem de erro específica
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado do tipo: {type(e).__name__}. Detalhes: {e}")


# Testes
divisao_multi_segura(10, 2)   # Saída normal: 5.0
divisao_multi_segura(10, 0)   # Saída tratada (ZeroDivisionError)
divisao_multi_segura("dez", 2) # Saída tratada (ValueError)