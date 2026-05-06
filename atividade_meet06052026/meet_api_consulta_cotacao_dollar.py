'''
Explicação sobre API

'''
# fazer a importação da API
import requests

# Criar uma função para definir o uso da API, URL da API brasileira AwesomeAPI para Dólar -> Real
def obter_cotacao_dolar():

    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    
    try:
    # Fazendo a requisição
        resposta = requests.get(url)
        
    # Convertendo para formato que o Python entende (Dicionário)
        dados = resposta.json()
        
    # Acessando a informação específica do Dólar (USDBRL)
    # O campo 'bid' é o preço de compra atual

        valor_dolar = dados['USDBRL']['bid']
        
        return float(valor_dolar)
    
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return None

# Testando tela
print("=== Aula de API com Python:Conversor de Moedas (Dados Reais) ===")

cotacao = obter_cotacao_dolar()

if cotacao:
    print(f"A cotação atual do Dólar é: R$ {cotacao:.2f}")
    
    # Pedindo um valor ao aluno
    valor_usd = float(input("Quantos dólares você tem na carteira? US$ "))
    
    # Calculando a conversão
    total_reais = valor_usd * cotacao
    
    print(f"\nCom US$ {valor_usd:.2f}, você teria R$ {total_reais:.2f} hoje!")
else:

    print("Não foi possível obter a cotação agora.")

