'''
Docstring para modulo_9-Tratamento de Erro
Este módulo demonstra técnicas de tratamento de 
erro em Python, 
incluindo o uso de blocos try-except, criação de exceções 
personalizadas e boas práticas para
manutenção de código robusto. 
'''

def processar_arquivo(nome_arquivo):
    """
    Demonstra o fluxo completo de tratamento de erros usando try, except, else e finally.
    Tenta ler um arquivo e garante que o recurso seja fechado.

    Parâmetros:
    - nome_arquivo (str): O nome do arquivo a ser processado.
    """
    # Inicializa 'arquivo' como None. Isso é importante para o bloco 'finally'.
    arquivo = None 
    
    try:
        # 1. Tente (try) abrir e ler o arquivo
        print(f"Tentando abrir o arquivo: {nome_arquivo}...")
        
        # 'r' é para leitura (read)
        arquivo = open(nome_arquivo, 'r') 
        conteudo = arquivo.read()
    
    except FileNotFoundError:
        # 2. Se (except) o arquivo não existir
        print(f"❌ ERRO na leitura: O arquivo '{nome_arquivo}' NÃO foi encontrado.")
        
    except Exception as e:
        # 3. Qualquer outro erro (permissão, etc.)
        print(f"❌ ERRO INESPERADO: Ocorreu um erro ao ler o arquivo: {e}")
        
    else:
        # 4. else: SÓ executa se TUDO no 'try' funcionar SEM erro
        print("✅ ARQUIVO LIDO COM SUCESSO!")
        print("--- Conteúdo lido (Primeiros 50 caracteres) ---")
        # Se o conteúdo for longo, mostra só o começo para a demonstração
        print(conteudo[:50] + "..." if len(conteudo) > 50 else conteudo) 
        
    finally:
        # 5. finally: SEMPRE executa, independentemente de erro
        print("🔧 Fim da tentativa de processamento de arquivo.")
        
        # Garante que o recurso (o arquivo) seja fechado, se ele foi aberto
        if arquivo:
            print("🔧 Fechando o arquivo para liberar o recurso.")
            arquivo.close()


# --- INSTRUÇÕES DE TESTE (AGORA DESCOMENTADAS) ---
print("--- TESTE 1: ARQUIVO INEXISTENTE (Trigga 'except') ---")
# Vai falhar, pois esse arquivo provavelmente não existe
processar_arquivo("arquivo_invisivel.xyz") 

print("\n" + "=" * 40 + "\n")

# Para que o Teste 2 funcione, você deve criar um arquivo chamado 'exemplo.txt'
# na mesma pasta deste código e colocar algum texto dentro dele!
# Se você não criar o arquivo, ele também cair