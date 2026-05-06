'''
Explicação sobre API

'''

# fazer a importação da API
import requests

# Criar uma função para definir o uso da API
def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

#Peço uma requisição - resposta
    resposta = requests.get(url)

#Pedir uma Verificação de Status 200 ou OK requests

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        return 'Error na Consulta. ⚠'
    

print('===Aula de API com Python: Consulta de CEP===')

# input(int(f'digite seu CEP:'))

meu_cep = '02849000'

resultado = consulta_cep(meu_cep)

if isinstance(resultado, dict):
    print(f'Endereço: {resultado['logradouro']}')
    print(f'Bairro: {resultado['bairro']}')
    print(f'Cidade: {resultado['localidade']}')