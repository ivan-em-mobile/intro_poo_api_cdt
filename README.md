# 🚀 Curso de Python: POO, Tratamento de Erros e APIs

Este guia foi elaborado para consolidar os fundamentos da Programação Orientada a Objetos (POO), o tratamento rigoroso de exceções e a integração com serviços externos via APIs brasileiras. É um guia prático para dominar a segurança do código com **Tratamento de Exceções** (Módulo 09) e a comunicação externa via **APIs** (Módulo 10)

---
## 🌐 Módulo 10: Introdução a API
As APIs permitem que o Python receba dados de outros sites (formato JSON).
Uma **API (Application Programming Interface)** permite que seu código requisite informações de outros servidores na internet.

### 📦 Instalação do Requests
Antes de rodar os códigos abaixo, você deve instalar a biblioteca no terminal:
```bash
pip install requests
```

### 1. Consulta de Endereço (ViaCEP)
Busca dados reais de logradouro e cidade usando um CEP.
```python

import requests

def consulta_cep(cep):
    url = f'[https://viacep.com.br/ws/](https://viacep.com.br/ws/){cep}/json/'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        return 'Erro na Consulta. ⚠'

print('=== Consulta de CEP ===')
meu_cep = '02849000'
resultado = consulta_cep(meu_cep)

if isinstance(resultado, dict):
    print(f"Endereço: {resultado.get('logradouro')}")
    print(f"Bairro: {resultado.get('bairro')}")
    print(f"Cidade: {resultado.get('localidade')}")
```

### 2. Cotação do Dólar (AwesomeAPI)
Obtém o valor do Dólar em tempo real e faz a conversão monetária.
```python

import requests

def obter_cotacao_dolar():
    url = "[https://economia.awesomeapi.com.br/last/USD-BRL](https://economia.awesomeapi.com.br/last/USD-BRL)"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        valor_dolar = dados['USDBRL']['bid']
        return float(valor_dolar)
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return None

print("=== Conversor de Moedas Real ===")
cotacao = obter_cotacao_dolar()

if cotacao:
    print(f"Cotação atual: R$ {cotacao:.2f}")
    valor_usd = float(input("Quantos dólares deseja converter? US$ "))
    print(f"Total: R$ {valor_usd * cotacao:.2f}")
```
------

## 🛠️ Módulo 09: Tratamento de Erros (Exceptions)
Neste módulo, aprendemos a usar `try`, `except`, `else` e `finally` para evitar que o programa pare de funcionar ao encontrar um erro.

### 1. Captura de Erros Matemáticos (`explicacao_mod09.py`)
Focado em evitar erros de divisão por zero e entradas de texto onde deveriam ser números.

```python
def aula_tratamento_erros():
    print("--- Início da Aula de Exceções ---")
    try:
        numerador = int(input("Digita o numerador: "))
        denominador = int(input("Digita o denominador: "))
        resultado = numerador / denominador
    except ValueError:
        print("Erro: Digite apenas números inteiros!")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
    else:
        print(f"Sucesso! Resultado: {resultado}")
    finally:
        print("--- Operação finalizada ---")

aula_tratamento_erros()
```

### 2. Teste de Mesa com Classes (`exercicio_mod09_teste_de_mesa.py`)
Trata erros quando o usuário digita a duração de uma chamada por extenso.
```python
class Celular:
    def __init__(self, marca, modelo):
        self.marca, self.modelo, self.bateria = marca, modelo, 100

    def fazer_chamada(self, duracao):
        try:
            gasto = int(duracao) * 2
            if self.bateria >= gasto:
                self.bateria -= gasto
                print(f"Chamada de {duracao} min efetuada! Bateria: {self.bateria}%")
            else:
                print("Bateria insuficiente.")
        except ValueError:
            print("Erro: A duração deve ser um número inteiro!")
        except TypeError:
            print("Erro crítico: Sistema de bateria encontrou erro de tipo.")

meu_celular = Celular("Samsung", "S24")
meu_celular.fazer_chamada("Dez") # Simula erro de valor
```

### 3. Evitando Conflitos de Tipos (`exercicio_mod09_com_usuario.py`)
Usa `TypeError` para impedir subtrações entre textos e números.
```python
# Focado no uso do bloco else e finally para logs de sistema
def iniciar_chamada(celular, custo):
    try:
        celular.bateria -= custo
    except TypeError:
        print("ERRO: Você tentou usar um valor que não é um número!")
    else:
        print(f"Chamada concluída! Bateria restante: {celular.bateria}%")
    finally:
        print("Sistema de chamadas finalizado.")
```

### 4. Validação de Nível de Bateria (`exercicio_mod09_teste_com_programador.py`)
Mistura `float` com lógica `if/elif` para validar intervalos de 0 a 100[cite: 2].
```python
def verificar_status(nivel_texto):
    try:
        nivel = float(nivel_texto)
        if nivel < 0 or nivel > 100:
            print("Aviso: Digite um valor entre 0 e 100.")
        elif nivel < 15:
            print(f"⚠️ Bateria em {nivel}%! Carregue o telemóvel.")
        else:
            print(f"📱 Bateria em {nivel}%. Status normal.")
    except ValueError:
        print("Erro Crítico: Entrada inválida.")
```
---
## 🚀 Como implementar

1. **Instale o Requests**: Use o comando `pip` mencionado acima.

2. **Crie os arquivos**: Salve cada bloco de código em um arquivo `.py` (ex: `modulo09_aula.py`)

3. **Markdown**: Para usar este guia, basta copiar o texto acima e colar em um arquivo chamado `README.md`.
---

# intro_poo_api_cdt
Este repositório é seu guia completo para os **fundamentos da Programação Orientada a Objetos (POO)** e o **uso prático de APIs**, tudo com a **Python**.

* **Programação Orientada a Objetos (POO):** Explore os pilares da POO – **classes**, **objetos**, **herança**, **polimorfismo** e **encapsulamento**. Aprenda a organizar seu código de forma lógica e eficiente, criando programas mais fáceis de entender, manter e escalar. 

* **Integração com APIs:** Descubra como seu código Python pode "conversar" com outros sistemas na internet. Veja exemplos práticos de como **fazer requisições**, **receber dados** (geralmente em formato JSON) e **utilizá-los** em seus projetos, abrindo um mundo de possibilidades de integração.

* **Fundamentos Sólidos:** Este espaço é perfeito para **iniciantes** que buscam construir uma base robusta em **algoritmos e estruturas de dados essenciais**. Cada projeto é desenhado para ajudar você a pensar como um programador, resolver problemas e implementar soluções eficazes.

Sinta-se à vontade para mergulhar nos códigos, testar as implementações e solidificar seu conhecimento em POO e APIs com Python.
