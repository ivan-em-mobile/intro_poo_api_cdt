def validar_id(id_usuario):
    try:
        id_int = int(id_usuario)

        if id_int <= 0:
            raise ValueError(f"O ID deve ser um número inteiro positivo (maior que zero). O valor fornecido foi {id_int}.")
            

        return f"✅ ID {id_int} validado com sucesso!"

    except ValueError as e:     
        if "invalid literal" in str(e):
             return f"❌ ERRO na validação: '{id_usuario}' não é um número inteiro válido."
        else:
            return f"❌ ERRO na validação: {e}"


print(validar_id("123"))
print(validar_id("abc"))
print(validar_id("-5"))
print(validar_id("0"))