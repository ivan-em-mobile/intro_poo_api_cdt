'''
Docstring para modulo_9-Tratamento de Erro
Este módulo demonstra técnicas de tratamento de 
erro em Python, 
incluindo o uso de blocos try-except, criação de exceções 
personalizadas e boas práticas para
manutenção de código robusto. 
'''

def validar_id(id_usuario):
    """
    Função para validar um ID de usuário, garantindo que é um número inteiro positivo.
    
    Parâmetros:
    - id_usuario (str): A entrada do usuário, que será tentada a conversão para int.
    
    Retorno:
    - str: Mensagem de sucesso ou mensagem de erro detalhada.
    """
    try:
        # 1. Tenta converter a entrada para inteiro (Ponto de risco 1: texto não numérico)
        # Se 'id_usuario' for, por exemplo, "abc", o Python levanta um ValueError
        id_int = int(id_usuario)

        # 2. Verifica a regra de negócio (Ponto de risco 2: número não positivo)
        if id_int <= 0:
            # Se a condição for violada, nós levantamos (raise) a nossa própria exceção.
            # Essa exceção será capturada pelo bloco 'except ValueError' abaixo.
            raise ValueError(f"O ID digitado ({id_int}) deve ser um número positivo (maior que zero).")

        # 3. Se tudo correu bem, retorna o sucesso
        return f"✅ SUCESSO! ID {id_int} validado e aceito."

    # 4. Captura e Trata
    # Este bloco captura: 
    # a) O ValueError nativo da função int() (se for texto).
    # b) O ValueError que nós levantamos (se for zero ou negativo).
    except ValueError as e:
        # 'e' contém a mensagem de erro detalhada (ou a nossa mensagem personalizada)
        return f"❌ ERRO na validação: {e}"
    
    except Exception as e:
        # Captura qualquer outro erro inesperado (boa prática)
        return f"❓ ERRO INESPERADO: {type(e).__name__} - {e}"

# --- Testando a Solução ---

print("--- Testes de Validação ---")
print(f"Teste 1 (Válido): {validar_id('123')}")
print("-" * 30)
print(f"Teste 2 (Texto Inválido): {validar_id('abc')}")
print("-" * 30)
print(f"Teste 3 (Negativo): {validar_id('-5')}")
print("-" * 30)
print(f"Teste 4 (Zero): {validar_id('0')}")
print("-" * 30)