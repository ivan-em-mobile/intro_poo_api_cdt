'''
O seu objetivo é escrever uma função em Python chamada 
validar_id(id_usuario) que faz o seguinte:

Pede ao usuário para digitar um ID de usuário:
Usa o Tratamento de Erros para garantir que:
O ID digitado seja um número inteiro. (Tratar ValueError):
O ID digitado seja positivo (maior que zero):
Se for zero ou negativo, você deve forçar um erro (usando raise),
para o bloco except tratar.

'''

def validar_id(id_usuario):
    """
    Função para validar um ID de usuário, garantindo que é um número inteiro positivo.
    """
    try:
        # Tenta converter a entrada para inteiro
        id_int = int(id_usuario)

        # SE o ID for menor ou igual a zero, levante um erro (raise)
        if id_int <= 0:
            # TODO: Use 'raise ValueError' com uma mensagem personalizada
            # Ex: raise ValueError("O ID deve ser um número positivo.")
            pass # Substitua esta linha

        # Se tudo der certo
        return f"✅ ID {id_int} validado com sucesso!"

    except ValueError as e:
        # TODO: Trate o erro. Esta parte deve capturar 
        # a) entradas não numéricas e 
        # b) o 'ValueError' que você levantou.
        return f"❌ ERRO na validação: {e}"

# Exemplos de Teste (Descomente para testar após completar a função)
print(validar_id("123"))#Somente esse está correto
print(validar_id("abc"))
print(validar_id("-5"))
print(validar_id("0"))