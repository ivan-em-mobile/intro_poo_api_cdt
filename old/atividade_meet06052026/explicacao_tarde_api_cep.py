'''

Explicação sobre API

'''
# fazer a importação da API
import requests

# criar uma função para definir o uso da API
def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

# peço uma requisição - resposta
    resposta = requests.get(url)

# pedir uma verificação do status 200 ou Ok requests

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        return 'Error na Consulta ⚠'
    
print('= Aula de API com Python: Consulta de CEP =')

# fazer teste de mesa

meu_cep = '05349000'

resultado = consulta_cep(meu_cep)

if isinstance(resultado, dict):
    print(f'Endereço: {resultado['logradouro']}')
    print(f'Bairro: {resultado['bairro']}')
    print(f'Cidade: {resultado['localidade']}')