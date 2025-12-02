def validar_id(id_usuario):
    """
    Valida se o ID do usuário é um número inteiro e positivo (maior que zero).
    
    Args:
        id_usuario: O valor do ID fornecido pelo usuário.
        
    Returns:
        O ID do usuário, se a validação for bem-sucedida.
        
    Raises:
        ValueError: Se o ID não for um inteiro ou se for menor ou igual a zero.
    """
    
    # 1. Tenta converter o ID para inteiro. Se falhar, um ValueError já é levantado.
    try:
        # Tenta a conversão. Se 'id_usuario' não for convertível (ex: "abc"), 
        # o Python levanta um ValueError automaticamente.
        id_int = int(id_usuario) 
    except ValueError:
        # Captura o erro se a conversão falhar (ex: 'id_usuario' era uma string não numérica)
        # e levanta um novo ValueError personalizado.
        raise ValueError("O ID deve ser um número inteiro.")

    # 2. Verifica se o número inteiro é positivo (maior que zero).
    if id_int <= 0:
        # Se for zero ou negativo, levanta um ValueError personalizado.
        # Este é o erro que o bloco 'except' no código de teste deve tratar.
        raise ValueError("O ID deve ser positivo (maior que zero).")

    # 3. Se passou em ambas as checagens, retorna o ID inteiro validado.
    return id_int


# --- Bloco de Teste e Tratamento de Erro (Conforme Solicitado) ---
def print_validar_id(id_teste):
    """Função auxiliar para testar e imprimir o resultado da validação."""
    try:
        print(f"Tentando validar ID: '{id_teste}'")
        # Chama a função principal de validação
        id_validado = validar_id(id_teste)
        print(f"SUCESSO! ID '{id_validado}' validado com sucesso!")
    except ValueError as e:
        # O bloco 'except' trata o erro levantado (raise) pela função validar_id
        print(f"ERRO DE VALIDAÇÃO: {e}")
    finally:
        print("-" * 20)


# Exemplos de Teste:
print_validar_id(100)        # Deve passar (Inteiro e Positivo)
print_validar_id("150")      # Deve passar (String convertível e Positivo)
print_validar_id(0)          # Deve falhar (Zero)
print_validar_id(-5)         # Deve falhar (Negativo)
print_validar_id("abc")      # Deve falhar (Não é um número)
print_validar_id(10.5)       # Deve passar (Float é convertido para int 10, mas alguns casos podem querer impedir float)
print_validar_id(True)       # Deve passar (Booleano True é convertido para int 1)